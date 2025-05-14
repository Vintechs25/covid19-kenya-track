# COVID-19 Data Tracker - Kenya Focus

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
try:
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Filter for Kenya
kenya_data = df[df['location'] == 'Kenya']

# Check basic info
print("\nKenya COVID-19 Data Summary:")
print(kenya_data[['date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths']].describe())

# Clean: Drop rows with missing total_cases
kenya_data_clean = kenya_data.dropna(subset=['total_cases'])

# Plot total cases over time
plt.figure(figsize=(12, 6))
plt.plot(kenya_data_clean['date'], kenya_data_clean['total_cases'], color='blue')
plt.title('Total COVID-19 Cases in Kenya Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot new daily cases
plt.figure(figsize=(12, 6))
plt.plot(kenya_data_clean['date'], kenya_data_clean['new_cases'], color='orange')
plt.title('Daily New COVID-19 Cases in Kenya')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot new daily deaths
plt.figure(figsize=(12, 6))
plt.plot(kenya_data_clean['date'], kenya_data_clean['new_deaths'], color='red')
plt.title('Daily New COVID-19 Deaths in Kenya')
plt.xlabel('Date')
plt.ylabel('New Deaths')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Histogram of new cases
plt.figure(figsize=(8, 6))
sns.histplot(kenya_data_clean['new_cases'], bins=30, kde=True, color='green')
plt.title('Distribution of New COVID-19 Cases in Kenya')
plt.xlabel('New Cases')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot: Total cases vs. Total deaths
plt.figure(figsize=(8, 6))
plt.scatter(kenya_data_clean['total_cases'], kenya_data_clean['total_deaths'], color='purple')
plt.title('Total Cases vs. Total Deaths in Kenya')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.grid(True)
plt.tight_layout()
plt.show()
