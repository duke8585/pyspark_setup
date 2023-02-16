def get_spark_context():
    from pyspark import SparkConf, SparkContext
    from pyspark.sql import SparkSession

    # spark multiple jars: https://stackoverflow.com/questions/57862801/spark-shell-add-multiple-drivers-jars-to-classpath-using-spark-defaults-conf/65799134#65799134
    conf = SparkConf()
    packages = [
        "org.apache.hadoop:hadoop-aws:3.2.0",
        "com.amazonaws:aws-java-sdk-bundle:1.12.370",
        # "com.amazonaws:aws-java-sdk-s3:1.11.375", # lighter but more problems
        # "com.amazonaws:aws-java-sdk-core:1.11.375", # lighter but more problems
    ]
    conf.set("spark.jars.packages", ",".join(packages))

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    spark._jsc.hadoopConfiguration().set(
        "fs.s3a.aws.credentials.provider",
        "com.amazonaws.auth.profile.ProfileCredentialsProvider",
    )
    spark._jsc.hadoopConfiguration().set(
        "fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    spark._jsc.hadoopConfiguration().set(
        "fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem"
    )

    return spark


def to_base_path(s3_url):
    """strip any partition and file parts from s3 url"""
    s = "/"
    comps = s3_url.split(s)

    def part_valid(s: str):
        for p in ["=", "date", "hour", "parquet", "earnings_type"]:
            if p in s:
                return False
        return True

    return s.join([p for p in comps if part_valid(p)])


def read_with_pyspark(spark, s3_path):
    df = spark.read.option(
        "basePath",
        to_base_path(s3_path),
    ).parquet(s3_path, inferSchema=True)

    return df
