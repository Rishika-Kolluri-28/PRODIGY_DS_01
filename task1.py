
# ==========================================================
# PRODIGY INFOTECH - DATA SCIENCE INTERNSHIP
# TASK 01: DATA VISUALIZATION
# Population Distribution using Histogram and Bar Chart
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_theme(style="whitegrid")

# STEP 1: Load the dataset
print("Loading Dataset...")

df = pd.read_csv("population.csv", skiprows=4)

print("Dataset Loaded Successfully!")

# STEP 2: Display dataset information
print("\nFirst Five Rows:")
print(df.head())

# STEP 3: Select latest year
year_columns = [
    col for col in df.columns
    if str(col).isdigit() and len(str(col)) == 4
]

latest_year = max(year_columns, key=int)

print("\nSelected Year:", latest_year)

# STEP 4: Data Cleaning
df[latest_year] = pd.to_numeric(
    df[latest_year], errors="coerce"
)

df = df.dropna(subset=[latest_year])

# Remove aggregate regions and keep individual countries
# The World Bank country codes for aggregates are not ISO-3 codes.
df = df[
    df["Country Code"].astype(str).str.fullmatch(r"[A-Z]{3}")
]

# Remove zero or negative population values
df = df[df[latest_year] > 0]

print("\nCleaned Dataset:")
print(df[["Country Name", latest_year]].head())

print("\nTotal Countries:", len(df))

# STEP 5: Create Histogram
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x=latest_year,
    bins=25,
    kde=True,
    color="skyblue"
)

plt.title(
    "Population Distribution Across Countries",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.tight_layout()
plt.savefig("population_histogram.png", dpi=300)

plt.show()

# STEP 6: Create Bar Chart
top_countries = df.nlargest(10, latest_year)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_countries,
    x=latest_year,
    y="Country Name",
    color="cornflowerblue"
)

plt.title(
    "Top 10 Most Populated Countries in " + latest_year,
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Population")
plt.ylabel("Country Name")

plt.tight_layout()
plt.savefig("population_bar_chart.png", dpi=300)

plt.show()

# STEP 7: Statistical Analysis
print("\n========== STATISTICAL ANALYSIS ==========")

print(df[latest_year].describe())

print("\nTop 10 Most Populated Countries:")
print(top_countries[["Country Name", latest_year]])

# STEP 8: Completion message
print("\n================================")
print("PRODIGY TASK 01 COMPLETED!")
print("Histogram and Bar Chart Created!")
print("================================")
