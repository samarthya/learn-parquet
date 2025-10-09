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

