from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .appName("Demo") \
            .master("local[*]") \
            .getOrCreate()

    sc1 = spark.sparkContext
    rdd = sc1.parallelize([1, 2, 3, 4, 5])
    print(rdd.collect())
