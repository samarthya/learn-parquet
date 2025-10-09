# Penguins Analytics Example - Summary

## Overview
This project demonstrates a complete data analytics workflow using Apache Parquet format with PySpark, showcasing data loading, processing, analytics, and visualization.

## What Was Implemented

### 1. Core Analytics Script (`penguins_analytics.py`)
A comprehensive Python script that:
- Loads the Palmer Penguins dataset from Seaborn
- Converts data to PySpark DataFrame
- Saves data in Parquet format (columnar storage)
- Loads and processes Parquet data using PySpark
- Performs multiple analytics operations:
  - Average measurements by species
  - Distribution by species and island
  - Sex distribution analysis
- Generates visualizations (static and interactive)
- Saves analytics results back to Parquet

### 2. Parquet Reader Example (`read_parquet_example.py`)
A helper script that demonstrates:
- Reading Parquet files with PySpark
- Displaying data and schema
- Running queries on Parquet data
- Best practices for working with Parquet files

### 3. Dependencies (`requirements.txt`)
All necessary Python packages:
- PySpark 3.5.0 - Distributed data processing
- Pandas 2.1.4 - Data manipulation
- PyArrow 14.0.2 - Parquet file support
- Seaborn 0.13.1 - Statistical visualizations
- Matplotlib 3.8.2 - Plotting library
- Plotly 5.18.0 - Interactive visualizations

### 4. Documentation (`README.md`)
Comprehensive documentation including:
- Project overview and features
- Installation instructions
- Usage examples
- Output file descriptions
- Information about Parquet format
- Dataset description
- Technologies used

### 5. Configuration (`.gitignore`)
Properly configured to exclude:
- Python artifacts (`__pycache__`, `.pyc`)
- Data files (`*.parquet`, `*.csv`)
- Output directories
- IDE and OS files
- Spark metadata

## Generated Outputs

### Parquet Data Files (not in repo)
1. `data/penguins.parquet` - Original dataset in Parquet format
2. `data/species_averages.parquet` - Aggregated statistics by species
3. `data/species_island_distribution.parquet` - Distribution data

### Visualizations (not in repo)
1. `output/bill_dimensions_seaborn.png` - Scatter plot of bill dimensions by species
2. `output/body_mass_distribution_seaborn.png` - Box plot of body mass by species and sex
3. `output/3d_scatter_plotly.html` - Interactive 3D scatter plot
4. `output/species_by_island_plotly.html` - Interactive bar chart of species distribution

## Key Features Demonstrated

### Parquet Format Benefits
- **Columnar Storage**: Efficient compression and query performance
- **Schema Evolution**: Self-describing format with embedded schema
- **Cross-Platform**: Compatible with Spark, Pandas, and other tools
- **Compression**: Snappy compression reduces file size

### PySpark Operations
- DataFrame creation from Pandas
- Parquet read/write operations
- Data aggregations and grouping
- Statistical calculations
- Filtering and transformations

### Data Analytics
- Species-level statistics (average measurements)
- Geographic distribution analysis (species by island)
- Demographic analysis (sex distribution)
- Custom queries and filtering

### Visualizations
- Static plots with Seaborn (publication-ready)
- Interactive plots with Plotly (exploratory analysis)
- Multiple chart types (scatter, box, 3D scatter, bar)

## How to Use

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main analytics script:
   ```bash
   python penguins_analytics.py
   ```

3. (Optional) Read and query Parquet files:
   ```bash
   python read_parquet_example.py
   ```

4. View visualizations:
   - Open `.png` files with any image viewer
   - Open `.html` files in a web browser for interactive charts

## Technical Highlights

- **Minimal Dependencies**: Only essential packages included
- **Clean Code**: Well-documented with clear structure
- **Error Handling**: Properly handles null values
- **Performance**: Uses Spark's distributed processing capabilities
- **Best Practices**: Follows PySpark and data engineering conventions
- **Reproducible**: Complete workflow from raw data to insights

## Dataset Information

**Palmer Penguins Dataset**
- 344 observations of 3 penguin species
- 7 variables (species, island, measurements, sex)
- Species: Adelie, Chinstrap, Gentoo
- Islands: Biscoe, Dream, Torgersen
- Measurements: Bill length/depth, flipper length, body mass

## Success Metrics

✅ Successfully loads data from multiple sources
✅ Converts between formats (CSV → Parquet)
✅ Performs distributed processing with PySpark
✅ Generates meaningful analytics and insights
✅ Creates professional visualizations
✅ Demonstrates Parquet format advantages
✅ Provides reusable, well-documented code
✅ Includes comprehensive documentation
