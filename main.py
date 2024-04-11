from typing import List, Dict, Any
import pandas as pd
from pprint import pprint as pp
from utils import get_spark_context, read_with_pyspark


DUMMY_S3_FILE = "s3a://some-bucket-eu-central-1/some_prefix/some_date_partition=2023-01-02/some_file.snappy.parquet"


def read_from_s3():
    sc = get_spark_context()
    df = read_with_pyspark(sc, DUMMY_S3_FILE)
    df.show(10, 100, True)
    return df


def make_dummy_df():
    """from https://sparkbyexamples.com/pyspark-tutorial/"""
    sc = get_spark_context()
    data = [
        ("James", "", "Smith", "1991-04-01", "M", 3000),
        ("Michael", "Rose", "", "2000-05-19", "M", 4000),
        ("Robert", "", "Williams", "1978-09-05", "M", 4000),
        ("Maria", "Anne", "Jones", "1967-12-01", "F", 4000),
        ("Jen", "Mary", "Brown", "1980-02-17", "F", -1),
    ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
    df = sc.createDataFrame(data=data, schema=columns)
    df.show(10)
    df.show(2, vertical=True)
    return df


if __name__ == "__main__":
    # df = make_dummy_df()
    df = read_from_s3()
