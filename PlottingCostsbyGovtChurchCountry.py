import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# === Database connection ===
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='lucas',
    password='Domino123%',
    database='Dissertation'
)

# === Load tables dynamically into a dictionary ===
years = range(1876, 1909)
tables = {year: pd.read_sql(f"SELECT * FROM `Dissertation`.`{year}`", conn) for year in years}

conn.close()

# === Load unique IDs for filtering ===
unique_ids_df = pd.read_csv("Unique IDs.csv")
northwest_ids = unique_ids_df.loc[unique_ids_df['Northwest_Coast'] == 1, 'Unique_ID']

# === Clean, filter, and convert numeric columns ===
filtered_tables = []
for df in tables.values():
    # Convert numeric columns (4–9) to integers
    for col in df.columns[4:10]:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(np.int64)
    
    # Convert cost columns (18th and 19th) to numeric
    df.iloc[:, 17] = pd.to_numeric(df.iloc[:, 17], errors='coerce')
    df.iloc[:, 18] = pd.to_numeric(df.iloc[:, 18], errors='coerce')
    
    # Filter only Northwest Coast schools
    df_filtered = df[df['Unique ID'].isin(northwest_ids)]
    filtered_tables.append(df_filtered)

# === Calculate yearly sums for US and BC, govt and church ===
sums = {"US_govt": [], "US_church": [], "BC_govt": [], "BC_church": []}

for df in filtered_tables:
    us_mask = df['Country'] == "US"
    bc_mask = df.iloc[:, 1] == "BC"  # Province column
    denom_mask = df['Denomination'].notna() & (df['Denomination'] != "") & (df['Denomination'] != "N/A")

    sums["US_govt"].append(df.loc[us_mask, 'Cost to govt'].sum())
    sums["US_church"].append(df.loc[us_mask & denom_mask, 'Cost to govt'].sum())
    sums["BC_govt"].append(df.loc[bc_mask, 'Cost to govt'].sum())
    sums["BC_church"].append(df.loc[bc_mask & denom_mask, 'Cost to govt'].sum())

# Fix missing BC data for plotting
sums["BC_govt"][-7] = None
sums["BC_church"][-7] = None

# === Plotting ===
plt.figure(figsize=(12, 6))

# US lines (black)
plt.plot(years, sums["US_govt"], label='Cost to US Government', color='black', linestyle='-', marker='o', markersize=3)
plt.plot(years, sums["US_church"], label='Cost to US Churches', color='black', linestyle='--', marker='o', markersize=3)

# Canada lines (grey)
plt.plot(years, sums["BC_govt"], label='Cost to BC Government', color='grey', linestyle='-', marker='o', markersize=3)
plt.plot(years, sums["BC_church"], label='Cost to BC Churches', color='grey', linestyle='--', marker='o', markersize=3)

# Labels, title, legend
plt.xlabel('Years')
plt.ylabel('Values ($)')
#plt.title('Boarding and Residential School Funding Over Years')
plt.legend(fontsize=12, loc='best')

# Y-axis formatting with commas
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

# Remove gridlines
plt.grid(False)
plt.tight_layout()
plt.show()
