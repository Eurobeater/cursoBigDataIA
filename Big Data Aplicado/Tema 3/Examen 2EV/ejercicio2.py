# Cargar el archivo de ratings
ratings_df = spark.read.csv("/FileStore/u.data", sep="\t", inferSchema=True)
ratings_df = ratings_df.toDF("user_id", "movie_id", "rating", "timestamp")

# Cargar el archivo de películas
movies_df = spark.read.csv("/FileStore/u.item", sep="|", inferSchema=True, encoding="ISO-8859-1")
movies_df = movies_df.toDF("movie_id", "title", "release_date", "video_release_date", "IMDb_URL", 
                            "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", 
                            "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", 
                            "Romance", "Sci-Fi", "Thriller", "War", "Western")

# Cargar el archivo de usuarios
users_df = spark.read.csv("/FileStore/u.user", sep="|", inferSchema=True)
users_df = users_df.toDF("user_id", "age", "gender", "occupation", "zip_code")

######

from pyspark.sql.functions import col

# Filtrar solo los ratings positivos (4 y 5)
positive_ratings_df = ratings_df.filter(col("rating") >= 4)

######

# Unir con movies_df para obtener los títulos de las películas
ratings_movies_df = positive_ratings_df.join(movies_df, "movie_id")

# Unir con users_df para obtener la información de los usuarios
ratings_users_df = ratings_movies_df.join(users_df, "user_id")


######

from pyspark.sql.functions import count
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Contar votos positivos por película y género
most_voted_by_gender = ratings_users_df.groupBy("title", "gender").agg(count("rating").alias("count"))

# Encontrar la película con más votos por género
window_spec = Window.partitionBy("gender").orderBy(col("count").desc())

top_movies_by_gender = most_voted_by_gender.withColumn("rank", row_number().over(window_spec)).filter(col("rank") == 1)

# Mostrar el resultado
top_movies_by_gender.select("gender", "title", "count").show()

######

from pyspark.sql.functions import when

# Crear una nueva columna para agrupar por rangos de edad
ratings_users_df = ratings_users_df.withColumn(
    "age_group",
    when(col("age") <= 25, "0-25")
    .when((col("age") > 25) & (col("age") <= 45), "25-45")
    .when((col("age") > 45) & (col("age") <= 65), "45-65")
    .otherwise(">65")
)

# Contar votos positivos por película y grupo de edad
most_voted_by_age = ratings_users_df.groupBy("title", "age_group").agg(count("rating").alias("count"))

# Encontrar la película con más votos por edad
window_spec_age = Window.partitionBy("age_group").orderBy(col("count").desc())

top_movies_by_age = most_voted_by_age.withColumn("rank", row_number().over(window_spec_age)).filter(col("rank") == 1)

# Mostrar el resultado
top_movies_by_age.select("age_group", "title", "count").show()

######

# Contar votos positivos por película y ocupación
most_voted_by_occupation = ratings_users_df.groupBy("title", "occupation").agg(count("rating").alias("count"))

# Encontrar la película con más votos por ocupación
window_spec_occ = Window.partitionBy("occupation").orderBy(col("count").desc())

top_movies_by_occupation = most_voted_by_occupation.withColumn("rank", row_number().over(window_spec_occ)).filter(col("rank") == 1)

# Mostrar el resultado
top_movies_by_occupation.select("occupation", "title", "count").show()
