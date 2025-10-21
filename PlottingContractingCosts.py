import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# ------------------------
# Database connection
# ------------------------
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='lucas',
    password='Domino123%',
    database='Dissertation'
)

# ------------------------
# Load all tables dynamically
# ------------------------
years = list(range(1876, 1909))
tables = {}

for year in years:
    query = f'SELECT * FROM `Dissertation`.`{year}`'
    tables[year] = pd.read_sql(query, conn)

conn.close()

# ------------------------
# Load unique IDs for filtering
# ------------------------
unique_ids_df = pd.read_csv("Unique IDs.csv")
nw_ids = unique_ids_df.loc[unique_ids_df['Northwest_Coast'] == 1, 'Unique_ID'].tolist()

# ------------------------
# Preprocess tables
# ------------------------
for year, df in tables.items():
    df = df[df['Unique ID'].isin(nw_ids)].copy()
    df.rename(columns={df.columns[1]: 'Province', df.columns[9]: 'Contract'}, inplace=True)

    # Convert numeric columns
    for col in df.columns[4:10]:
        df[col] = pd.to_numeric(df[col].replace('*', np.nan), errors='coerce').astype('Int64')

    # Convert cost column
    df['Cost to govt'] = pd.to_numeric(df.iloc[:, 17], errors='coerce')

    tables[year] = df

# ------------------------
# Aggregate government costs by province
# ------------------------
provinces = ['WA', 'OR', 'CA', 'AK', 'BC']
sums_govt = {prov: [] for prov in provinces}

for year in years:
    df = tables[year]
    for prov in provinces:
        condition = (df['Contract'] == 1) & (df['Public'] == 0) & (df['Province'] == prov)
        sums_govt[prov].append(df.loc[condition, 'Cost to govt'].sum())

# Remove specific missing points
sums_govt['BC'][26] = None  # remove 1902 only

# ------------------------
# Plotting
# ------------------------
plt.figure(figsize=(12, 6))

# Define line styles and markers
line_styles = {
    'BC': ('-', 'black', 'o'),    # solid black, circle
    'AK': ('-', 'grey', 'o'),     # solid grey, circle
    'WA': ('--', 'grey', 's'),    # dashed grey, square
    'OR': ('--', 'grey', '^'),    # dashed grey, triangle
    'CA': ('--', 'grey', 'D')     # dashed grey, diamond
}

for prov in provinces:
    ls, color, marker = line_styles[prov]
    plt.plot(years, sums_govt[prov], label=f'{prov} Govt', linestyle=ls, color=color,
             marker=marker, markersize=4)

plt.xlabel('Years')
plt.ylabel('Cost ($)')
#plt.title('Boarding and Residential School Funding by Province (Government Only)')
plt.legend(fontsize=12, loc='best')

# Format y-axis with commas and dollar sign
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))

# Remove gridlines
plt.grid(False)
plt.tight_layout()
plt.show()
