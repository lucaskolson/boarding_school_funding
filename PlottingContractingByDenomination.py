import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ------------------------
# Database connection
# ------------------------
host = '127.0.0.1'
user = 'lucas'
password = 'Domino123%'
database = 'Dissertation'

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

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
# Protestant denominations
# ------------------------
Protestant = ['Christian Union', 'Church of England', 'Congregational', 'Methodist', 'Presbyterian',
              'Morovian', 'Free Mission Society of Sweden', 'Quakers', 'Russian Church',
              'Swedish Evangelical', 'Swedish-Evangelical', 'Russo-Greek Church', 'Methodist Episcopal',
              'Morovian', 'Protestant Episcopal', 'Moravian', 'Protestant Episcopal', 'Russian Orthodox',
              'Episcopal', 'Swedish-Evangelcial', 'WNIA', 'Salvation Army']

# ------------------------
# Preprocess tables
# ------------------------
for year, df in tables.items():
    df = df[df['Unique ID'].isin(nw_ids)].copy()
    df.rename(columns={df.columns[1]: 'Province', df.columns[9]: 'Contract'}, inplace=True)

    # Convert numeric columns
    for col in df.columns[4:10]:
        df[col] = pd.to_numeric(df[col].replace('*', np.nan), errors='coerce').astype('Int64')
    df['Cost to govt'] = pd.to_numeric(df.iloc[:, 17], errors='coerce')

    # Standardize denominations
    df['Denomination'].replace({
        "Roman Catholic": "Catholic Church",
        "United Presbyterian": "Presbyterian",
        "*": None,
        "Nondenominational": "Non-denominational",
        "Undenominational": "Non-denominational"
    }, inplace=True)
    df['Denomination'].replace(to_replace=Protestant, value='Protestant', inplace=True)

    tables[year] = df

# ------------------------
# Aggregate per-year costs
# ------------------------
exclude_values = ["Alaska Company", "North American Commercial Company", "Independent", 
                  "Non-denominational", "N/A", ""]

combined_data = {}

for year in years:
    df = tables[year]
    if 'Denomination' in df.columns:
        filtered = df[~df['Denomination'].isin(exclude_values)]
        grouped = filtered.groupby(['Country', 'Denomination'])['Cost to govt'].sum()
        for idx, value in grouped.items():
            combined_data.setdefault(idx, []).append((year, value))

# ------------------------
# Convert to DataFrame for plotting
# ------------------------
plot_data = pd.DataFrame()
for idx, values in combined_data.items():
    years_list, costs_list = zip(*values)
    plot_data[idx] = pd.Series(data=costs_list, index=years_list)

# ------------------------
# Remove 1902 from all series
# ------------------------
plot_data.loc[1902, :] = np.nan

# Remove Canada Protestant points for 1882–1884, 1896–1898, 1900 onward
can_prot_idx = ('Canada', 'Protestant')
if can_prot_idx in plot_data.columns:
    plot_data.loc[1882:1884, can_prot_idx] = np.nan
    plot_data.loc[1896:1898, can_prot_idx] = np.nan
    plot_data.loc[1900:, can_prot_idx] = np.nan

# ------------------------
# Drop empty columns (all NaN) to avoid extra legend lines
# ------------------------
plot_data = plot_data.dropna(axis=1, how='all')

# ------------------------
# Plot
# ------------------------
plt.figure(figsize=(12,6))

line_styles = {
    ('US', 'Catholic Church'): ('-', 'black'),
    ('US', 'Protestant'): ('--', 'black'),
    ('Canada', 'Catholic Church'): ('-', 'grey'),
    ('Canada', 'Protestant'): ('--', 'grey')
}

for col in plot_data.columns:
    linestyle, color = line_styles.get(col, ('-', 'blue'))
    plt.plot(plot_data.index, plot_data[col], marker='o', markersize=4,
             linestyle=linestyle, color=color, label=f'{col[0]} {col[1]}')

plt.xlabel('Year')
plt.ylabel('Cost ($)')
#plt.title('Government Funding Received by Denomination for School Operations')

# Format Y-axis with commas
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.legend()
plt.show()
