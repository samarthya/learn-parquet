# learn-parquet

Tutorial sample for apache parquet using PySpark and Quarto.

## Overview

This project demonstrates how to work with Apache Parquet files using PySpark. It includes a Quarto-based website that showcases:

- Creating a Spark session with appName "ParquetPenguinsDemo"
- Loading the Palmer Penguins dataset
- Dropping NA values from the dataset
- Displaying the top 10 rows
- Showing the DataFrame schema

## Features

- **Quarto Website**: Static website with interactive PySpark examples
- **Automated Deployment**: GitHub Actions workflow for automatic compilation and deployment to GitHub Pages
- **PySpark Integration**: Demonstrates data processing with Apache Spark

## Local Development

### Prerequisites

- Python 3.12+
- Quarto 1.4+

### Setup

1. Install dependencies:
```bash
pip install pyspark palmerpenguins jupyter nbformat
```

2. Render the website:
```bash
quarto render
```

3. Preview the website:
```bash
quarto preview
```

## Deployment

The website is automatically deployed to GitHub Pages when changes are pushed to the `main` branch. The GitHub Actions workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs required dependencies (PySpark, palmerpenguins, Jupyter)
4. Sets up Quarto
5. Renders and publishes the website to GitHub Pages

## Technologies Used

- **Apache Spark**: Distributed data processing framework
- **PySpark**: Python API for Apache Spark
- **Quarto**: Scientific and technical publishing system
- **Palmer Penguins**: Sample dataset for data science
- **GitHub Actions**: CI/CD for automated deployment

Tutorial sample for Apache Parquet with PySpark and Data Analytics

## Overview

This project demonstrates how to use Apache Parquet format with PySpark for efficient data storage and analytics. We use the Palmer Penguins dataset as an example to showcase:

- Loading data and converting to Parquet format
- Using PySpark for data processing and analytics
- Creating visualizations with Seaborn and Plotly
- Saving analytical results back to Parquet

## Features

- **Data Format Conversion**: Convert CSV/DataFrame data to Parquet format
- **PySpark Integration**: Use PySpark for distributed data processing
- **Data Analytics**: Perform aggregations, grouping, and statistical analysis
- **Visualizations**: Generate static (Seaborn) and interactive (Plotly) charts
- **Efficient Storage**: Leverage Parquet's columnar storage for better performance

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/samarthya/learn-parquet.git
cd learn-parquet
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the penguins analytics example:

```bash
python penguins_analytics.py
```

This script will:
1. Load the Palmer Penguins dataset from Seaborn
2. Convert it to a Spark DataFrame
3. Save the data to Parquet format
4. Load the Parquet data back into Spark
5. Perform various analytics operations:
   - Calculate average measurements by species
   - Analyze distribution by species and island
   - Examine sex distribution
6. Generate visualizations:
   - Bill dimensions scatter plot (Seaborn)
   - Body mass distribution box plot (Seaborn)
   - 3D interactive scatter plot (Plotly)
   - Species distribution bar chart (Plotly)
7. Save analytical results to Parquet files

## Output

The script generates the following files:

### Parquet Data Files
- `data/penguins.parquet` - Original dataset in Parquet format
- `data/species_averages.parquet` - Aggregated statistics by species
- `data/species_island_distribution.parquet` - Distribution data by species and island

### Visualizations
- `output/bill_dimensions_seaborn.png` - Bill length vs depth scatter plot
- `output/body_mass_distribution_seaborn.png` - Body mass distribution by species and sex
- `output/3d_scatter_plotly.html` - Interactive 3D scatter plot (open in browser)
- `output/species_by_island_plotly.html` - Interactive bar chart (open in browser)

## About Parquet Format

Apache Parquet is a columnar storage file format optimized for use with big data processing frameworks. Benefits include:

- **Efficient Compression**: Columnar storage allows for better compression
- **Fast Query Performance**: Only read the columns you need
- **Schema Evolution**: Support for adding new columns over time
- **Cross-Platform**: Works with multiple big data tools (Spark, Hadoop, Pandas, etc.)

## Dataset

The Palmer Penguins dataset contains measurements for three penguin species observed on islands in the Palmer Archipelago, Antarctica. The dataset includes:

- Species: Adelie, Chinstrap, or Gentoo
- Island: Biscoe, Dream, or Torgersen
- Bill length and depth (mm)
- Flipper length (mm)
- Body mass (g)
- Sex

## Technologies Used

- **PySpark**: Distributed data processing
- **Pandas**: Data manipulation
- **PyArrow**: Parquet file support
- **Seaborn**: Statistical data visualization
- **Matplotlib**: Plotting library
- **Plotly**: Interactive visualizations

## License

MIT License - feel free to use this code for learning purposes.
