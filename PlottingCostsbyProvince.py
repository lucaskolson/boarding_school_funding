import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# --- Database Connection ---
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='lucas',
    password='Domino123%',
    database='Dissertation'
)

# --- Load all tables dynamically ---
years = range(1876, 1909)
tables = {
    year: pd.read_sql(f"SELECT * FROM `Dissertation`.`{year}`", conn)
    for year in years
}
conn.close()

# --- Clean and prepare data ---
for df in tables.values():
    # Convert "Cost to govt" and "Cost to denomination" columns to numeric
    df['Cost to govt'] = pd.to_numeric(df['Cost to govt'], errors='coerce')
    df['Cost to denomination'] = pd.to_numeric(df['Cost to denomination'], errors='coerce')

# --- Regions to analyze ---
regions = ["WA", "OR", "CA", "AK", "BC"]

# --- Initialize results dictionary ---
sums = {region: {"govt": [], "church": []} for region in regions}

# --- Compute yearly sums for each region ---
for year in years:
    df = tables[year]
    for region in regions:
        region_mask = df.iloc[:, 1] == region  # assuming 2nd column = Province/State
        govt_sum = df.loc[region_mask, 'Cost to govt'].sum()
        church_sum = df.loc[region_mask, 'Cost to denomination'].sum()
        sums[region]["govt"].append(govt_sum)
        sums[region]["church"].append(church_sum)

# --- Fix known missing BC entry (if applicable) ---
sums["BC"]["govt"][-7] = None
sums["BC"]["church"][-7] = None

# --- Plot results ---
plt.figure(figsize=(10, 6))
for region in regions:
    plt.plot(years, sums[region]["govt"], label=f'Cost to {region} Government', marker='o')
    plt.plot(years, sums[region]["church"], linestyle='dotted', label=f'Cost to {region} Churches', marker='o')

plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Boarding and Residential School Funding Over Years')
plt.legend()
plt.tight_layout()
plt.show()
