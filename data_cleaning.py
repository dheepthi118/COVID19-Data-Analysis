
import pandas as pd
import os

# Define the dataset path
file_path = os.path.join("data", "COVID-19 Coronavirus.csv")

# Load the dataset
df = pd.read_csv(file_path)

# Display basic information
print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

# Check dataset information
print("\nDataset Information:")
df.info()

# Check for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Clean missing values
df["Other names"] = df["Other names"].fillna(df["Country"])

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal missing values remaining:")
print(df.isnull().sum().sum())

# Save the cleaned dataset
output_path = os.path.join("data", "COVID-19_Cleaned.csv")
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("Saved to:", output_path)

import matplotlib.pyplot as plt

# Select the 10 countries with the most COVID-19 cases
top_10 = df.nlargest(10, "Total Cases")

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_10["Country"], top_10["Total Cases"])

plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart
plt.savefig("visualizations/top_10_covid_cases.png")
plt.show()

print("\nBar chart created successfully!")

# Total COVID-19 deaths by continent
deaths_by_continent = df.groupby("Continent")["Total Deaths"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
deaths_by_continent.plot(kind="bar")

plt.title("Total COVID-19 Deaths by Continent")
plt.xlabel("Continent")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart
plt.savefig("visualizations/deaths_by_continent.png")
plt.show()

print("\nContinent chart created successfully!")
