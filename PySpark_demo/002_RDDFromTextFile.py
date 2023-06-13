from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .appName("PySpark_Demo") \
            .master("local[*]")\
            .getOrCreate()

    rdd = spark.sparkContext.textFile("001-Wordcount.txt")
    print(rdd.collect())

    rdd1 = rdd.flatMap(lambda x: x.split(" "))

    rdd2 = rdd1.map(lambda x: (x, 1))
    print(rdd2.collect())
