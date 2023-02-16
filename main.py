from typing import List, Dict, Any
from pprint import pprint as pp
from utils import get_spark_context, read_with_pyspark


S3_FILE = "s3a://some-bucket-eu-central-1/some_prefix/some_date_partition=2023-01-02/some_file.snappy.parquet"


if __name__ == "__main__":
    sc = get_spark_context()
    df = read_with_pyspark(sc, S3_FILE)
    df.show(10, 100, True)
