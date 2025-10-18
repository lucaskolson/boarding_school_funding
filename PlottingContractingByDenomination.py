import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Replace these with your database credentials
host = '127.0.0.1'
user = 'lucas'
password = 'Domino123%'
database = 'Dissertation'

# Create a MySQL connection
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Define the tables you want to extract
table1_name = '`Dissertation`.`1876`'
table2_name = '`Dissertation`.`1877`'
table3_name = '`Dissertation`.`1878`'
table4_name = '`Dissertation`.`1879`'
table5_name = '`Dissertation`.`1880`'
table6_name = '`Dissertation`.`1881`'
table7_name = '`Dissertation`.`1882`'
table8_name = '`Dissertation`.`1883`'
table9_name = '`Dissertation`.`1884`'
table10_name = '`Dissertation`.`1885`'
table11_name = '`Dissertation`.`1886`'
table12_name = '`Dissertation`.`1887`'
table13_name = '`Dissertation`.`1888`'
table14_name = '`Dissertation`.`1889`'
table15_name = '`Dissertation`.`1890`'
table16_name = '`Dissertation`.`1891`'
table17_name = '`Dissertation`.`1892`'
table18_name = '`Dissertation`.`1893`'
table19_name = '`Dissertation`.`1894`'
table20_name = '`Dissertation`.`1895`'
table21_name = '`Dissertation`.`1896`'
table22_name = '`Dissertation`.`1897`'
table23_name = '`Dissertation`.`1898`'
table24_name = '`Dissertation`.`1899`'
table25_name = '`Dissertation`.`1900`'
table26_name = '`Dissertation`.`1901`'
table27_name = '`Dissertation`.`1902`'
table28_name = '`Dissertation`.`1903`'
table29_name = '`Dissertation`.`1904`'
table30_name = '`Dissertation`.`1905`'
table31_name = '`Dissertation`.`1906`'
table32_name = '`Dissertation`.`1907`'
table33_name = '`Dissertation`.`1908`'


# SQL queries to select data from the tables
query_table1 = f'SELECT * FROM {table1_name}'
query_table2 = f'SELECT * FROM {table2_name}'
query_table3 = f'SELECT * FROM {table3_name}'
query_table4 = f'SELECT * FROM {table4_name}'
query_table5 = f'SELECT * FROM {table5_name}'
query_table6 = f'SELECT * FROM {table6_name}'
query_table7 = f'SELECT * FROM {table7_name}'
query_table8 = f'SELECT * FROM {table8_name}'
query_table9 = f'SELECT * FROM {table9_name}'
query_table10 = f'SELECT * FROM {table10_name}'
query_table11 = f'SELECT * FROM {table11_name}'
query_table12 = f'SELECT * FROM {table12_name}'
query_table13 = f'SELECT * FROM {table13_name}'
query_table14 = f'SELECT * FROM {table14_name}'
query_table15 = f'SELECT * FROM {table15_name}'
query_table16 = f'SELECT * FROM {table16_name}'
query_table17 = f'SELECT * FROM {table17_name}'
query_table18 = f'SELECT * FROM {table18_name}'
query_table19 = f'SELECT * FROM {table19_name}'
query_table20 = f'SELECT * FROM {table20_name}'
query_table21 = f'SELECT * FROM {table21_name}'
query_table22 = f'SELECT * FROM {table22_name}'
query_table23 = f'SELECT * FROM {table23_name}'
query_table24 = f'SELECT * FROM {table24_name}'
query_table25 = f'SELECT * FROM {table25_name}'
query_table26 = f'SELECT * FROM {table26_name}'
query_table27 = f'SELECT * FROM {table27_name}'
query_table28 = f'SELECT * FROM {table28_name}'
query_table29 = f'SELECT * FROM {table29_name}'
query_table30 = f'SELECT * FROM {table30_name}'
query_table31 = f'SELECT * FROM {table31_name}'
query_table32 = f'SELECT * FROM {table32_name}'
query_table33 = f'SELECT * FROM {table33_name}'

# Extract data and create DataFrames
table1876_df = pd.read_sql(query_table1, conn)
table1877_df = pd.read_sql(query_table2, conn)
table1878_df = pd.read_sql(query_table3, conn)
table1879_df = pd.read_sql(query_table4, conn)
table1880_df = pd.read_sql(query_table5, conn)
table1881_df = pd.read_sql(query_table6, conn)
table1882_df = pd.read_sql(query_table7, conn)
table1883_df = pd.read_sql(query_table8, conn)
table1884_df = pd.read_sql(query_table9, conn)
table1885_df = pd.read_sql(query_table10, conn)
table1886_df = pd.read_sql(query_table11, conn)
table1887_df = pd.read_sql(query_table12, conn)
table1888_df = pd.read_sql(query_table13, conn)
table1889_df = pd.read_sql(query_table14, conn)
table1890_df = pd.read_sql(query_table15, conn)
table1891_df = pd.read_sql(query_table16, conn)
table1892_df = pd.read_sql(query_table17, conn)
table1893_df = pd.read_sql(query_table18, conn)
table1894_df = pd.read_sql(query_table19, conn)
table1895_df = pd.read_sql(query_table20, conn)
table1896_df = pd.read_sql(query_table21, conn)
table1897_df = pd.read_sql(query_table22, conn)
table1898_df = pd.read_sql(query_table23, conn)
table1899_df = pd.read_sql(query_table24, conn)
table1900_df = pd.read_sql(query_table25, conn)
table1901_df = pd.read_sql(query_table26, conn)
table1902_df = pd.read_sql(query_table27, conn)
table1903_df = pd.read_sql(query_table28, conn)
table1904_df = pd.read_sql(query_table29, conn)
table1905_df = pd.read_sql(query_table30, conn)
table1906_df = pd.read_sql(query_table31, conn)
table1907_df = pd.read_sql(query_table32, conn)
table1908_df = pd.read_sql(query_table33, conn)

# Close the database connection
conn.close()

#import unique ID file for filtering
unique_ids_df = pd.read_csv("Unique IDs.csv")

# create list of all table names
years_range = range(1876, 1909) # Define the range of years (1876 to 1908)
table_names2 = [f'table{year}_df' for year in years_range] # Create a list of table names using a list comprehension
Protestant = ['Christian Union', 'Church of England', 'Congregational', 'Methodist', 'Presbyterian', 'Morovian', 'Free Mission Society of Sweden', 'Quakers', 'Russian Church', 'Swedish Evangelical', 'Swedish-Evangelical', 'Russo-Greek Church', 'Methodist Episcopal', 'Morovian', 'Protestant Episcopal', 'Moravian', 'Protestant Episcopal', 'Russian Orthodox', 'Episcopal', 'Swedish-Evangelcial', 'WNIA', 'Salvation Army']

#convert all df column dtypes to object
for table_name in table_names2:
    table_df = globals()[table_name]
    for col in table_df.columns[4:10]:
        table_df[col] = pd.to_numeric(table_df[col], errors='coerce').fillna(0).astype(np.int64)

#filter for only schools in the northwest coast
table_names = []

for table in table_names2:
    table_df = globals()[table]
    filtered_rows = table_df[table_df['Unique ID'].isin(unique_ids_df.loc[unique_ids_df['Northwest_Coast'] == 1, 'Unique_ID'])]
    table_names.append(filtered_rows)


#renaming column headers
for table_df in table_names:
    #table_df = globals()[table_name]

    # Rename the 2nd column to "Province"
    table_df.rename(columns={table_df.columns[1]: 'Province'}, inplace=True)
    table_df.rename(columns={table_df.columns[9]: 'Contract'}, inplace=True)  

#converting text columns to binary variables for columns 5-9 (school type, public, and contract)
for table_df in table_names:
    #table_df = globals()[table_name]
    #for column_index in range(5, 10):
    for column_index in range(5,10):
        table_df.iloc[:, column_index] = table_df.iloc[:, column_index].astype(str)
    #table_df.iloc[:, 9] = table_df.iloc[:, 9].replace('*', None).astype(float).astype('Int64')
        table_df.iloc[:, column_index] = table_df.iloc[:, column_index].replace('*', None).apply(lambda x: pd.to_numeric(x, errors='coerce')).astype('Int64')
    #table_df.iloc[:, 8]

# Iterate through tables to convert cost to govt and cost to churches into numeric variables
for table_df in table_names:
    #table_df = globals()[table_name]
    
    # Convert the 18th and 19th columns to numeric (double)
    table_df.iloc[:, 17] = pd.to_numeric(table_df.iloc[:, 17], errors='coerce')  # 18th column (zero-based index)
    table_df.iloc[:, 18] = pd.to_numeric(table_df.iloc[:, 18], errors='coerce')  # 19th column (zero-based index)

#clean up names of denominations
for table_df in table_names:
    #table_df = globals()[table_name]

    table_df['Denomination'].replace("Roman Catholic", "Catholic Church", inplace=True)
    table_df['Denomination'].replace("United Presbyterian", "Presbyterian", inplace=True)
    table_df['Denomination'].replace("*", None, inplace=True)
    table_df['Denomination'].replace("Nondenominational", "Non-denominational", inplace=True)
    table_df['Denomination'].replace("Undenominational", "Non-denominational", inplace=True)
    table_df['Denomination'].replace(to_replace=Protestant, value='Protestant', inplace=True)


#create tables of per year cost to govt and churches
Combined_denomination_rev = []
exclude_values = ["Alaska Company", "North American Commercial Company", "Independent", "Non-denominational", "N/A", ""]

for table_df in table_names:
    #table_df = globals()[table_name]

    if 'Denomination' in table_df.columns:
        # Filter out rows where 'Denomination' is in exclude_values
        filtered_series = table_df[~table_df['Denomination'].isin(exclude_values)]['Cost to govt'].groupby([table_df['Country'], table_df['Denomination']]).sum()

        # Append the filtered Series to Combined_denomination_rev
        Combined_denomination_rev.append(filtered_series)

print(Combined_denomination_rev)

#drop blanks from df (overhead costs for state school expenditures, eg govt supervisor)
for i, s in enumerate(Combined_denomination_rev):
    if "" in s.index:
        Combined_denomination_rev[i] = s.drop(index=[""])


# Years from 1876 to 1908
years = list(range(1876, 1909))

#print(Combined_denomination_rev[-1].index)

#Plotting Combined Denominational Revenue
df = pd.DataFrame(Combined_denomination_rev)
df['year'] = years
#df = df.drop('N/A', axis=1)
df = df[df['year'] != 1902]
#df = df.drop(df[df['year'] == 1902].index, inplace=True)

df.plot(x='year', marker='o', linestyle='-', markersize=8)
plt.xlabel('Year')
plt.ylabel('$')
plt.title('Government Funding Received by denomination for school operations')
plt.legend()
plt.show()












    
