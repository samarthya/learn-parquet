"""
Penguins Dataset Analytics with PySpark and Parquet

This script demonstrates how to:
1. Load the Palmer Penguins dataset
2. Save it to Parquet format using PySpark
3. Load and process the Parquet data
4. Perform analytics operations
5. Create visualizations
"""

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, round as spark_round
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Create output directory
os.makedirs("output", exist_ok=True)

# Initialize Spark Session
print("Initializing Spark Session...")
spark = SparkSession.builder \
    .appName("PenguinsParquetAnalytics") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

print(f"Spark Version: {spark.version}")

# Step 1: Load the penguins dataset
print("\n=== Step 1: Loading Penguins Dataset ===")
# Load penguins dataset from seaborn
penguins_pd = sns.load_dataset('penguins')
print(f"Loaded {len(penguins_pd)} records")
print("\nDataset Preview:")
print(penguins_pd.head())

# Step 2: Convert to Spark DataFrame and save as Parquet
print("\n=== Step 2: Converting to Spark DataFrame and Saving as Parquet ===")
penguins_spark = spark.createDataFrame(penguins_pd)

# Show schema
print("\nSpark DataFrame Schema:")
penguins_spark.printSchema()

# Save to Parquet format
parquet_path = "data/penguins.parquet"
print(f"\nSaving to Parquet: {parquet_path}")
penguins_spark.write.mode("overwrite").parquet(parquet_path)
print("✓ Data saved to Parquet format successfully!")

# Step 3: Load from Parquet
print("\n=== Step 3: Loading Data from Parquet ===")
penguins_loaded = spark.read.parquet(parquet_path)
print(f"Loaded {penguins_loaded.count()} records from Parquet")

# Step 4: Data Analytics with PySpark
print("\n=== Step 4: Performing Data Analytics ===")

# Remove rows with null values for cleaner analysis
penguins_clean = penguins_loaded.dropna()
print(f"\nRecords after removing nulls: {penguins_clean.count()}")

# Analysis 1: Average measurements by species
print("\n--- Analysis 1: Average Measurements by Species ---")
species_avg = penguins_clean.groupBy("species").agg(
    spark_round(avg("bill_length_mm"), 2).alias("avg_bill_length"),
    spark_round(avg("bill_depth_mm"), 2).alias("avg_bill_depth"),
    spark_round(avg("flipper_length_mm"), 2).alias("avg_flipper_length"),
    spark_round(avg("body_mass_g"), 2).alias("avg_body_mass"),
    count("*").alias("count")
).orderBy("species")

species_avg.show()

# Analysis 2: Count by species and island
print("\n--- Analysis 2: Distribution by Species and Island ---")
species_island = penguins_clean.groupBy("species", "island").agg(
    count("*").alias("count")
).orderBy("species", "island")

species_island.show()

# Analysis 3: Sex distribution
print("\n--- Analysis 3: Sex Distribution by Species ---")
sex_distribution = penguins_clean.groupBy("species", "sex").agg(
    count("*").alias("count")
).orderBy("species", "sex")

sex_distribution.show()

# Step 5: Create Visualizations
print("\n=== Step 5: Creating Visualizations ===")

# Convert back to Pandas for visualization
penguins_viz = penguins_clean.toPandas()

# Visualization 1: Seaborn - Bill Length vs Depth by Species
print("\nCreating Seaborn visualization: Bill Length vs Depth...")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins_viz, x='bill_length_mm', y='bill_depth_mm', 
                hue='species', style='species', s=100)
plt.title('Penguin Bill Dimensions by Species', fontsize=16, fontweight='bold')
plt.xlabel('Bill Length (mm)', fontsize=12)
plt.ylabel('Bill Depth (mm)', fontsize=12)
plt.legend(title='Species', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/bill_dimensions_seaborn.png', dpi=150)
print("✓ Saved: output/bill_dimensions_seaborn.png")
plt.close()

# Visualization 2: Seaborn - Body Mass Distribution
print("\nCreating Seaborn visualization: Body Mass Distribution...")
plt.figure(figsize=(10, 6))
sns.boxplot(data=penguins_viz, x='species', y='body_mass_g', hue='sex')
plt.title('Penguin Body Mass Distribution by Species and Sex', fontsize=16, fontweight='bold')
plt.xlabel('Species', fontsize=12)
plt.ylabel('Body Mass (g)', fontsize=12)
plt.legend(title='Sex', fontsize=10)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('output/body_mass_distribution_seaborn.png', dpi=150)
print("✓ Saved: output/body_mass_distribution_seaborn.png")
plt.close()

# Visualization 3: Plotly - Interactive 3D Scatter
print("\nCreating Plotly visualization: 3D Interactive Scatter...")
fig = px.scatter_3d(penguins_viz, 
                    x='bill_length_mm', 
                    y='bill_depth_mm', 
                    z='flipper_length_mm',
                    color='species',
                    symbol='island',
                    title='3D Penguin Measurements by Species and Island',
                    labels={
                        'bill_length_mm': 'Bill Length (mm)',
                        'bill_depth_mm': 'Bill Depth (mm)',
                        'flipper_length_mm': 'Flipper Length (mm)'
                    },
                    hover_data=['body_mass_g', 'sex'])
fig.write_html('output/3d_scatter_plotly.html')
print("✓ Saved: output/3d_scatter_plotly.html")

# Visualization 4: Plotly - Species Count by Island
print("\nCreating Plotly visualization: Species Count by Island...")
species_island_pd = species_island.toPandas()
fig = px.bar(species_island_pd, 
             x='island', 
             y='count', 
             color='species',
             title='Penguin Species Distribution Across Islands',
             labels={'count': 'Number of Penguins', 'island': 'Island'},
             barmode='group')
fig.write_html('output/species_by_island_plotly.html')
print("✓ Saved: output/species_by_island_plotly.html")

# Step 6: Save analytics results to Parquet
print("\n=== Step 6: Saving Analytics Results to Parquet ===")

# Save aggregated results
species_avg.write.mode("overwrite").parquet("data/species_averages.parquet")
print("✓ Saved species averages to: data/species_averages.parquet")

species_island.write.mode("overwrite").parquet("data/species_island_distribution.parquet")
print("✓ Saved species-island distribution to: data/species_island_distribution.parquet")

# Summary
print("\n" + "="*60)
print("ANALYTICS COMPLETE!")
print("="*60)
print("\nGenerated Files:")
print("  Parquet Data:")
print("    - data/penguins.parquet (original data)")
print("    - data/species_averages.parquet (aggregated statistics)")
print("    - data/species_island_distribution.parquet (distribution data)")
print("\n  Visualizations:")
print("    - output/bill_dimensions_seaborn.png")
print("    - output/body_mass_distribution_seaborn.png")
print("    - output/3d_scatter_plotly.html (interactive)")
print("    - output/species_by_island_plotly.html (interactive)")
print("\nYou can open the HTML files in a browser for interactive visualizations!")
print("="*60)

# Stop Spark session
spark.stop()
print("\n✓ Spark session stopped successfully")
