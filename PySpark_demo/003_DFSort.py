import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, array


if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .appName("PySpark_Demo") \
            .master("local[*]") \
            .getOrCreate()

    sc = spark.sparkContext

    df = (spark.read.format("csv")
                    .option("path", "Data.csv")
                    .option("header", True)
                    .option("inferSchema", True)
          ).load()

    # df.show(5)
    columns = df.columns
    # df.select(columns[0:2]).show(3)
    # df.select(columns[1::]).show(3)
    lst = [310, 346, 336]
    df.filter(col("ProducName").like('%oa%')).sort(col("Sales").desc()).sort(col("ProductKey").asc()).show(10)
    #df.select(array(df.ProductKey, df.ProducName).alias("Product")).show(5)
    df1 = (df.withColumn("Product", array(df.ProductKey, df.ProducName))
             .withColumn("Sales_Status", when(df.Sales < 2000, "Less").when((df.Sales >= 2000) & (df.Sales < 4000), "Moderate").when(df.Sales > 4000, "Heigh").otherwise(df.Sales))
             .drop(df.ProductKey,df.ProducName,df.Sales)
           )
    #df1.show(20)
    path = os.getcwd() + "\\OS"
    print(path)
    df2 = df.withColumn("Sales_Status", when(df.Sales < 2000, "Less")
                        .when((df.Sales >= 2000) & (df.Sales < 4000), "Moderate")
                        .when(df.Sales > 4000, "High")
                        .otherwise(df.Sales))
    df2.write.csv(path=path, header=True)
