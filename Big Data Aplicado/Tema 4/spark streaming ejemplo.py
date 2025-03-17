from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession \
        .builder \
        .appName("Streaming IABD WordCount") \
        .master("local[8]") \
        .getOrCreate()

# Creamos un flujo de escucha sobre netcat en localhost:9999
# En Spark Streaming, la lectura se realiza mediante readStream
lineasDF = spark.readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", "9999") \
        .load()

# Leemos las líneas y las pasamos a palabras.
# Sobre ellas, realizamos la agrupación count (transformación)
from pyspark.sql.functions import explode, split
palabrasDF = lineasDF.select(explode(split(lineasDF.value, ' ')).alias('palabra'))
cantidadDF = palabrasDF.groupBy("palabra").count()

# Mostramos las palabras por consola (sink)
# En Spark Streaming, la persistencia se realiza mediante writeStream
#  y en vez de realizar un save, ahora utilizamos start
wordCountQuery = cantidadDF.writeStream \
        .format("console") \
        .outputMode("complete") \
        .start()

# dejamos Spark a la escucha
wordCountQuery.awaitTermination()