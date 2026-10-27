# COVID-19 Data Cleaning and Visualization

## 1. Project Overview
This project analyzes a country-level COVID-19 dataset using Python. The objective is to inspect the data, handle missing values, and create visualizations to explore reported cases and deaths.

## 2. Tools and Libraries
- Python 3
- Pandas
- Matplotlib
- Visual Studio Code

## 3. Dataset Description
The dataset contains 225 rows and 10 columns, including country names, population, continent, total COVID-19 cases, total deaths, cases per million, deaths per million, and death percentage.

## 4. Data Cleaning
- Inspected column names, data types, and dataset dimensions.
- Identified one missing value in the `Other names` column.
- Filled the missing value using the corresponding `Country` name.
- Checked for duplicate rows; none were found.
- Saved the cleaned dataset as `COVID-19_Cleaned.csv`.

## 5. Visualizations
1. **Top 10 Countries by Total COVID-19 Cases:** A bar chart comparing reported case totals across the ten countries with the highest values.
2. **Total COVID-19 Deaths by Continent:** A bar chart showing summed reported deaths grouped by continent.

## 6. Conclusion
The dataset was inspected and cleaned, and two charts were generated to make country-level COVID-19 statistics easier to compare. The results reflect the downloaded dataset and should not be interpreted as current statistics.

## 7. Project Files
- `data_cleaning.py` — Python analysis and visualization code.
- `data/COVID-19 Coronavirus.csv` — Original dataset.
- `data/COVID-19_Cleaned.csv` — Cleaned dataset.
- `visualizations/top_10_covid_cases.png` — Country comparison chart.
- `visualizations/deaths_by_continent.png` — Continent comparison chart.