import mysql.connector
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

# create list of all table names
years_range = range(1876, 1909) # Define the range of years (1876 to 1908)
table_names = [f'table{year}_df' for year in years_range] # Create a list of table names using a list comprehension

# Iterate through tables to convert cost to govt and cost to churches into numeric variables
for table_name in table_names:
    table_df = globals()[table_name]
    
    # Convert the 18th and 19th columns to numeric (double)
    table_df.iloc[:, 17] = pd.to_numeric(table_df.iloc[:, 17], errors='coerce')  # 18th column (zero-based index)
    table_df.iloc[:, 18] = pd.to_numeric(table_df.iloc[:, 18], errors='coerce')  # 19th column (zero-based index)

#create tables of per year cost to govt and churches
sums_WA_govt_costs = [] # Initialize list to store sums
sums_WA_church_costs = []
sums_OR_govt_costs = [] # Initialize list to store sums
sums_OR_church_costs = []
sums_CA_govt_costs = [] # Initialize list to store sums
sums_CA_church_costs = []
sums_AK_govt_costs = [] # Initialize list to store sums
sums_AK_church_costs = []
sums_BC_govt_costs = [] # Initialize list to store sums
sums_BC_church_costs = []

# Iterate through tables
for table_name in table_names:
    table_df = globals()[table_name]
   
    # Calculate sum of the 18th column and append to the list
    sum_WA_18th_column = table_df.loc[table_df.iloc[:, 1] == "WA", 'Cost to govt'].sum()  # 18th column (zero-based index)
    sums_WA_govt_costs.append(sum_WA_18th_column)

    # Calculate sum of the 19th column and append to the list
    sum_WA_19th_column = table_df.loc[table_df.iloc[:, 1] == "WA", 'Cost to denomination'].sum()  # 19th column (zero-based index)
    sums_WA_church_costs.append(sum_WA_19th_column)

    # Calculate sum of the 18th column and append to the list
    sum_OR_18th_column = table_df.loc[table_df.iloc[:, 1] == "OR", 'Cost to govt'].sum()  # 18th column (zero-based index)
    sums_OR_govt_costs.append(sum_OR_18th_column)

    # Calculate sum of the 19th column and append to the list
    sum_OR_19th_column = table_df.loc[table_df.iloc[:, 1] == "OR", 'Cost to denomination'].sum()  # 19th column (zero-based index)
    sums_OR_church_costs.append(sum_OR_19th_column)

    # Calculate sum of the 18th column and append to the list
    sum_CA_18th_column = table_df.loc[table_df.iloc[:, 1] == "CA", 'Cost to govt'].sum()  # 18th column (zero-based index)
    sums_CA_govt_costs.append(sum_CA_18th_column)

    # Calculate sum of the 19th column and append to the list
    sum_CA_19th_column = table_df.loc[table_df.iloc[:, 1] == "CA", 'Cost to denomination'].sum()  # 19th column (zero-based index)
    sums_CA_church_costs.append(sum_CA_19th_column)

    # Calculate sum of the 18th column and append to the list
    sum_AK_18th_column = table_df.loc[table_df.iloc[:, 1] == "AK", 'Cost to govt'].sum()  # 18th column (zero-based index)
    sums_AK_govt_costs.append(sum_AK_18th_column)

    # Calculate sum of the 19th column and append to the list
    sum_AK_19th_column = table_df.loc[table_df.iloc[:, 1] == "AK", 'Cost to denomination'].sum()  # 19th column (zero-based index)
    sums_AK_church_costs.append(sum_AK_19th_column)

    # Calculate sum of the 18th column and append to the list
    sum_BC_18th_column = table_df.loc[table_df.iloc[:, 1] == "BC", 'Cost to govt'].sum()  # 18th column (zero-based index)
    sums_BC_govt_costs.append(sum_BC_18th_column)

    # Calculate sum of the 19th column and append to the list
    sum_BC_19th_column = table_df.loc[table_df.iloc[:, 1] == "BC", 'Cost to denomination'].sum()  # 19th column (zero-based index)
    sums_BC_church_costs.append(sum_BC_19th_column)
    
#Remove 0s for missing data in plotting
sums_BC_govt_costs[-7] = None
sums_BC_church_costs[-7] = None

# Years from 1876 to 1908
years = list(range(1876, 1909))

# Plotting the line chart
plt.plot(years, sums_WA_govt_costs, label='Cost to WA Government', marker='o')
plt.plot(years, sums_WA_church_costs, linestyle='dotted', label='Cost to WA Churches', marker='o')
plt.plot(years, sums_OR_govt_costs, label='Cost to OR Government', marker='o')
plt.plot(years, sums_OR_church_costs, linestyle='dotted', label='Cost to OR Churches', marker='o')
plt.plot(years, sums_CA_govt_costs, label='Cost to CA Government', marker='o')
plt.plot(years, sums_CA_church_costs, linestyle='dotted', label='Cost to CA Churches', marker='o')
plt.plot(years, sums_AK_govt_costs, label='Cost to AK Government', marker='o')
plt.plot(years, sums_AK_church_costs, linestyle='dotted', label='Cost to AK Churches', marker='o')
plt.plot(years, sums_BC_govt_costs, label='Cost to BC Government', marker='o')
plt.plot(years, sums_BC_church_costs, linestyle='dotted', label='Cost to BC Churches', marker='o')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Boarding and Residential School Funding Over Years')

# Adding legend
plt.legend()

# Display the plot
plt.show()

