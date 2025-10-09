"""
Read Parquet Files Example

This script demonstrates how to read and display Parquet files created by the
penguins analytics script.
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("ReadParquetExample") \
    .getOrCreate()

print("="*60)
print("READING PARQUET FILES EXAMPLE")
print("="*60)

# Read the original penguins data
print("\n1. Reading original penguins data from Parquet:")
print("-" * 60)
penguins = spark.read.parquet("data/penguins.parquet")
print(f"Total records: {penguins.count()}")
print("\nSchema:")
penguins.printSchema()
print("\nSample data (first 5 rows):")
penguins.show(5)

# Read the species averages
print("\n2. Reading species averages from Parquet:")
print("-" * 60)
species_avg = spark.read.parquet("data/species_averages.parquet")
print("Species averages:")
species_avg.show()

# Read the species-island distribution
print("\n3. Reading species-island distribution from Parquet:")
print("-" * 60)
species_island = spark.read.parquet("data/species_island_distribution.parquet")
print("Species distribution by island:")
species_island.show()

# Demonstrate a query on the Parquet data
print("\n4. Example Query - Penguins with body mass > 4000g:")
print("-" * 60)
heavy_penguins = penguins.filter(penguins.body_mass_g > 4000) \
    .select("species", "island", "body_mass_g") \
    .orderBy("body_mass_g", ascending=False)
heavy_penguins.show(10)

print("\n" + "="*60)
print("DONE! Parquet files read successfully.")
print("="*60)

# Stop Spark
spark.stop()
