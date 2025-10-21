import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Database connection
# -------------------------
host = '127.0.0.1'
user = 'lucas'
password = 'Domino123%'
database = 'Dissertation'

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# -------------------------
# Load all tables into a dictionary
# -------------------------
years = range(1876, 1909)
tables_df = {}

for year in years:
    table_name = f'`Dissertation`.`{year}`'
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, conn)
    tables_df[year] = df  # Store DataFrame keyed by year

# Close the connection
conn.close()

# -------------------------
# Clean and transform data
# -------------------------
for year, df in tables_df.items():
    # Rename specific columns
    df.rename(columns={df.columns[1]: 'Province',
                       df.columns[9]: 'Contract',
                       df.columns[15]: 'DayAtt'}, inplace=True)

    # Convert columns 5-9 (school type, public, contract) to numeric safely
    for col_idx in range(5, 10):
        df.iloc[:, col_idx] = pd.to_numeric(df.iloc[:, col_idx].replace('*', np.nan), errors='coerce')

    # Convert columns 15,16,18,19 (zero-based 14,15,17,18) to numeric safely
    for col_idx in [14, 15, 17, 18]:
        df.iloc[:, col_idx] = pd.to_numeric(df.iloc[:, col_idx], errors='coerce')

    # Clean up denomination names
    df['Denomination'] = df['Denomination'].replace({
        "Roman Catholic": "Catholic Church",
        "United Presbyterian": "Presbyterian",
        "*": None,
        "Nondenominational": "Non-denominational",
        "Undenominational": "Non-denominational"
    })

# -------------------------
# Aggregate attendance
# -------------------------
US_Day_Att = []
US_Boarding_Att = []
Canada_Day_Att = []
Canada_Boarding_Att = []

for year, df in tables_df.items():
    US_Day_Att.append(df.loc[df['Country'] == 'US', 'DayAtt'].sum())
    US_Boarding_Att.append(df.loc[df['Country'] == 'US', 'Boarding'].sum())
    Canada_Day_Att.append(df.loc[df['Country'] == 'Canada', 'DayAtt'].sum())
    Canada_Boarding_Att.append(df.loc[df['Country'] == 'Canada', 'Boarding'].sum())

# Optional: manually set missing values (as in your original script)
Canada_Boarding_Att[-7] = None
Canada_Day_Att[-7] = None

# -------------------------
# Plot attendance
# -------------------------
plt.plot(years, US_Day_Att, marker='o', label='US Day Attendance')
plt.plot(years, US_Boarding_Att, marker='o', label='US Boarding Attendance')
plt.plot(years, Canada_Day_Att, marker='o', label='Canada Day Attendance')
plt.plot(years, Canada_Boarding_Att, marker='o', label='Canada Boarding Attendance')

plt.xlabel('Year')
plt.ylabel('Attendance')
#plt.title('Attendance by School Type in US and Canada')
plt.legend()
plt.grid(True)
plt.show()