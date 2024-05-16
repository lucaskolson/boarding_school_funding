import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Replace these with your database credentials
host = '127.0.0.1'
user = 'lucas'
password = 'Domino123@'
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
table_names = [f'table{year}_df' for year in years_range] # Create a list of table names using a list comprehension

#renaming column headers
for table_name in table_names:
    table_df = globals()[table_name]

    # Rename the 2nd column to "Province"
    table_df.rename(columns={table_df.columns[1]: 'Province'}, inplace=True)
    table_df.rename(columns={table_df.columns[9]: 'Contract'}, inplace=True)
    table_df.rename(columns={table_df.columns[15]: 'DayAtt'}, inplace=True)  

#converting text columns to binary variables for columns 5-9 (school type, public, and contract)
for table_name in table_names:
    table_df = globals()[table_name]
    #for column_index in range(5, 10):
    for column_index in range(5,10):
        table_df.iloc[:, column_index] = table_df.iloc[:, column_index].astype(str)
    #table_df.iloc[:, 9] = table_df.iloc[:, 9].replace('*', None).astype(float).astype('Int64')
        table_df.iloc[:, column_index] = table_df.iloc[:, column_index].replace('*', None).apply(lambda x: pd.to_numeric(x, errors='coerce')).astype('Int64')
    #table_df.iloc[:, 8]

# Iterate through tables to convert attendence, cost to govt and cost to churches into numeric variables
for table_name in table_names:
    table_df = globals()[table_name]
    
    #convert Unique ID to number
    table_df.iloc[:, 4] = pd.to_numeric(table_df.iloc[:, 4], errors='coerce')
    # Convert the 15th, 16th, 18th and 19th columns to numeric (double)
    table_df.iloc[:, 17] = pd.to_numeric(table_df.iloc[:, 17], errors='coerce')  # 18th column (zero-based index)
    table_df.iloc[:, 18] = pd.to_numeric(table_df.iloc[:, 18], errors='coerce')  # 19th column (zero-based index)
#    table_df.iloc[:,14] = pd.to_numeric(table_df.iloc[:, 14], errors='coerce')
#    table_df.iloc[:,15] = pd.to_numeric(table_df.iloc[:, 15], errors='coerce')

#pd.set_option('display.max_rows', None)
#print(table1895_df.loc[:,'DayAtt'])

#clean up names of denominations
for table_name in table_names:
    table_df = globals()[table_name]

    table_df['Denomination'].replace("Roman Catholic", "Catholic Church", inplace=True)
    table_df['Denomination'].replace("United Presbyterian", "Presbyterian", inplace=True)
    table_df['Denomination'].replace("*", None, inplace=True)
    table_df['Denomination'].replace("Nondenominational", "Non-denominational", inplace=True)
    table_df['Denomination'].replace("Undenominational", "Non-denominational", inplace=True)


#define function that will return all the average day attendance given a unique ID
def day_att(unique_id):
    # Initialize an empty DataFrame to store results
    result_df = pd.DataFrame(columns=['Table', 'DayAtt'])

    # Loop through each table in table_names
    for table_name in table_names:
        table_df = globals()[table_name]

        # Check if the Unique ID exists in the table
        if unique_id in table_df['Unique ID'].values:
            # Extract DayAtt for the specified Unique ID
            dayatt_value = table_df.loc[table_df['Unique ID'] == unique_id, 'DayAtt'].values[0]
        else:
            # If Unique ID not found, set DayAtt value to NaN
            dayatt_value = float('nan')

        # Append the result to the result_df
        result_df = pd.concat([result_df, pd.DataFrame({'Table': [table_name], 'DayAtt': [dayatt_value]})], ignore_index=True)

    # Print the result_df
    print(result_df)


# List to store DataFrames with "Unique ID" values from NaN rows
nan_dfs = pd.DataFrame()

for year in range(1893, 1899):
    table_name = f'table{year}_df'

    table_df = globals()[table_name]
        
        # Identify rows where "DayAtt" is NaN
    nan_rows = table_df[table_df['DayAtt'] == "*"]

        # Create a new DataFrame with the values of "Unique ID" from NaN rows
    nan_df = nan_rows[['Unique ID']].copy()

    nan_dfs = pd.concat([nan_dfs, nan_df], axis=0)

#drop duplicate Unique IDs      
nan_dfs.drop_duplicates(subset='Unique ID', inplace=True)

#reset index
nan_dfs.reset_index(drop=True, inplace=True)

def update_dayatt(year, unique_id, att):
    # Assuming your DataFrames are named table{year}_df
    table_name = f'table{year}_df'

    if table_name in globals() and isinstance(globals()[table_name], pd.DataFrame):
        table_df = globals()[table_name]

        # Check if the "Unique ID" exists in the DataFrame
        if unique_id in table_df['Unique ID'].values:
            # Update the "DayAtt" value for the specified "Unique ID"
            table_df.loc[table_df['Unique ID'] == unique_id, 'DayAtt'] = att
            print(f"Updated DayAtt for Unique ID {unique_id} in {table_name} to {att}")
        else:
            print(f"Unique ID {unique_id} not found in {table_name}")
    else:
        print(f"Table {table_name} not found")


#day_att(125)

#IMPUTING FOR AK DAY SCHOOLS, 1893-98
#school id 125, 6 year gap between 23.8 and 14 = 9.8 / 7 = 1.4
update_dayatt(1893, 125, 22.4)
update_dayatt(1894, 125, 21)
update_dayatt(1895, 125, 19.6)
update_dayatt(1896, 125, 18.2)
update_dayatt(1897, 125, 16.8)
update_dayatt(1898, 125, 15.4)

#school id 126, 3 year gap after 15.4
update_dayatt(1893, 126, 15.4)
update_dayatt(1894, 126, 15.4)
update_dayatt(1895, 126, 15.4)

#school id 127, 6 year gap before 23
update_dayatt(1893, 127, 23)
update_dayatt(1894, 127, 23)
update_dayatt(1895, 127, 23)
update_dayatt(1896, 127, 23)
update_dayatt(1897, 127, 23)
update_dayatt(1898, 127, 23)

#school id 128, two year gap after 17.2
update_dayatt(1893, 128, 17.2)
update_dayatt(1894, 128, 17.2)

#school id 129, 6 year gap between 32.1 and 23 = 9.1 / 7 = 1.3
update_dayatt(1893, 129, 30.8)
update_dayatt(1894, 129, 29.5)
update_dayatt(1895, 129, 28.2)
update_dayatt(1896, 129, 26.9)
update_dayatt(1897, 129, 25.6)
update_dayatt(1898, 129, 24.3)

#school id 130, 6 year gap after 15.7
update_dayatt(1893, 130, 15.7)
update_dayatt(1894, 130, 15.7)
update_dayatt(1895, 130, 15.7)
update_dayatt(1896, 130, 15.7)
update_dayatt(1897, 130, 15.7)
update_dayatt(1898, 130, 15.7)

#school id 132, 3 year gap after 147
update_dayatt(1893, 132, 147)
update_dayatt(1894, 132, 147)
update_dayatt(1895, 132, 147)

#school id 134, 2 year gap after 13
update_dayatt(1893, 134, 13)
update_dayatt(1894, 134, 13)

#school id 141, 2 year gap after 21.3
update_dayatt(1893, 141, 21.3)
update_dayatt(1894, 141, 21.3)

#school id 147, 6 year gap between 26.1 and 32 = 5.9 / 7 = .84
update_dayatt(1893, 147, 26.94)
update_dayatt(1894, 147, 27.78)
update_dayatt(1895, 147, 28.62)
update_dayatt(1896, 147, 29.46)
update_dayatt(1897, 147, 30.3)
update_dayatt(1898, 147, 31.14)

#school id 148, 5 year gap
update_dayatt(1893, 148, 17.9)
update_dayatt(1894, 148, 17.9)
update_dayatt(1895, 148, 17.9)
update_dayatt(1896, 148, 17.9)
update_dayatt(1898, 148, 17)

#school id 151, 6 year gap between 21.1 and 26 = 4.9 / 7 = 0.7
update_dayatt(1893, 151, 21.8)
update_dayatt(1894, 151, 22.5)
update_dayatt(1895, 151, 23.2)
update_dayatt(1896, 151, 23.9)
update_dayatt(1897, 151, 24.6)
update_dayatt(1898, 151, 25.3)

#school id 152, 6 year gap between 17 and 25 = 8 / 7 = 1.14
update_dayatt(1893, 152, 18.14)
update_dayatt(1894, 152, 19.28)
update_dayatt(1895, 152, 20.42)
update_dayatt(1896, 152, 21.56)
update_dayatt(1897, 152, 22.7)
update_dayatt(1898, 152, 23.84)

#school id 154, 2 year gap after 10
update_dayatt(1893, 154, 10)
update_dayatt(1894, 154, 10)

#school id 167, 2 year gap after 11
update_dayatt(1893, 167, 11)
update_dayatt(1894, 167, 11)

#school id 168, 6 year gap between 34.3 and 23 = 11.3 / 7 = 1.61
update_dayatt(1893, 168, 32.66)
update_dayatt(1894, 168, 31.05)
update_dayatt(1895, 168, 29.44)
update_dayatt(1896, 168, 27.83)
update_dayatt(1897, 168, 26.22)
update_dayatt(1898, 168, 24.61)

#school id 170, 6 year gap, nearest value is 17.3
update_dayatt(1893, 170, 17.3)
update_dayatt(1894, 170, 17.3)
update_dayatt(1895, 170, 17.3)
update_dayatt(1896, 170, 17.3)
update_dayatt(1897, 170, 17.3)
update_dayatt(1898, 170, 17.3)

#school id 172, 4 year gap, nearest value is 106
update_dayatt(1893, 172, 106)
update_dayatt(1894, 172, 106)
update_dayatt(1896, 172, 106)
update_dayatt(1897, 172, 106)
update_dayatt(1898, 172, 106)

#school id 173, 5 year gap, nearest values
update_dayatt(1893, 173, 33)
update_dayatt(1894, 173, 33)
update_dayatt(1897, 173, 30)
update_dayatt(1898, 173, 30)
update_dayatt(1899, 173, 30)

#school id 179, 2 year gap, above 25
update_dayatt(1893, 179, 25)
update_dayatt(1894, 179, 25)

#school id 187, 2 year gap, above 20
update_dayatt(1893, 187, 20)
update_dayatt(1894, 187, 20)

#school id 198, 2 year gap, above 28
update_dayatt(1893, 198, 28)
update_dayatt(1894, 198, 28)

#school id 202, 1 year gap, between 24.3 and 8
update_dayatt(1893, 202, 16.15)

#school id 212, 2 year gap, above 20
update_dayatt(1893, 212, 20)
update_dayatt(1894, 212, 20)

#school id 215, 2 year gap, above 171
update_dayatt(1893, 215, 171)
update_dayatt(1894, 215, 171)

#school id 135, 1 year gap, nearest value 8
update_dayatt(1895, 135, 8)

#school id 145, 1 year gap, looks like error
update_dayatt(1895, 145, None)

#school id 171, 3 year gap, nearest value is 20
update_dayatt(1895, 171, 20)
update_dayatt(1896, 171, 20)
update_dayatt(1897, 171, 20)

#school id 131, 3 year gap, nearest value is 17
update_dayatt(1896, 131, 17)
update_dayatt(1897, 131, 17)
update_dayatt(1898, 131, 17)

#school id 133, 3 year gap, nearest value is 14
update_dayatt(1896, 133, 14)
update_dayatt(1897, 133, 14)
update_dayatt(1898, 133, 14)

#school id 153, 2 year gap, looks like error
update_dayatt(1896, 133, None)
update_dayatt(1897, 133, None)

#school id 174, 1 year gap, looks like error
update_dayatt(1897, 174, None)

#school id 149, 1 year gap, looks like error
update_dayatt(1898, 149, None)


# Iterate through tables to convert attendence, cost to govt and cost to churches into numeric variables
for table_name in table_names:
    table_df = globals()[table_name]
    
    # Convert the 15th, 16th, 18th and 19th columns to numeric (double)
    table_df.iloc[:,14] = pd.to_numeric(table_df.iloc[:, 14], errors='coerce')
    table_df.iloc[:,15] = pd.to_numeric(table_df.iloc[:, 15], errors='coerce')


#convert all df column dtypes to numeric
for table_name in table_names:
    table_df = globals()[table_name]
    for col in table_df.columns[4:10]:
        table_df[col] = pd.to_numeric(table_df[col], errors='coerce').fillna(0).astype(np.int64)

#test = globals()[table_names[22]]
#print(test.info())

#filter for only schools in the northwest coast
table_names2 = []

for table in table_names:
    table_df = globals()[table]
    filtered_rows = table_df[table_df['Unique ID'].isin(unique_ids_df.loc[unique_ids_df['Northwest_Coast'] == 1, 'Unique_ID'])]
    table_names2.append(filtered_rows)


#create tables of per year cost to govt and churches
US_Day_Att = [] # Initialize list to store sums
US_Day_Att_Church = []
US_Boarding_Att = []
US_Boarding_Att_Church = []
Canada_Day_Att = []
Canada_Day_Att_Church = []
Canada_Boarding_Att = []
Canada_Boarding_Att_Church = []

for table_df in table_names2:
    # Access the DataFrame using the global() function
    #table_df = globals()[table_name]

    # Calculate the sum of 'DayAtt' where 'Country' is equal to 'US'
    sum_day_att_US = table_df.loc[table_df['Country'] == 'US', 'DayAtt'].sum()
    sum_day_att_US_church = table_df.loc[(table_df['Country'] == 'US') & (table_df['Denomination'] != 'N/A'), 'DayAtt'].sum()
    sum_boarding_att = table_df.loc[table_df['Country'] == 'US', 'Boarding'].sum()
    sum_boarding_att_US_church = table_df.loc[(table_df['Country'] == 'US') & (table_df['Denomination'] != 'N/A'), 'Boarding'].sum()
    sum_day_att_CA = table_df.loc[table_df['Country'] == 'Canada', 'DayAtt'].sum()
    sum_day_att_CA_church = table_df.loc[(table_df['Country'] == 'Canada') & (table_df['Denomination'] != 'N/A'), 'DayAtt'].sum()
    sum_boarding_att_CA = table_df.loc[table_df['Country'] == 'Canada', 'Boarding'].sum()
    sum_boarding_att_CA_church = table_df.loc[(table_df['Country'] == 'Canada') & (table_df['Denomination'] != 'N/A'), 'Boarding'].sum()

    # Append the sum to the list
    US_Day_Att.append(sum_day_att_US)
    US_Day_Att_Church.append(sum_day_att_US_church)
    US_Boarding_Att.append(sum_boarding_att)
    US_Boarding_Att_Church.append(sum_boarding_att_US_church)
    Canada_Day_Att.append(sum_day_att_CA)
    Canada_Day_Att_Church.append(sum_day_att_CA_church)
    Canada_Boarding_Att.append(sum_boarding_att_CA)
    Canada_Boarding_Att_Church.append(sum_boarding_att_CA_church)


Canada_Boarding_Att[-7] = None
Canada_Day_Att[-7] = None
Canada_Boarding_Att_Church[-7] = None
Canada_Day_Att_Church[-7] = None


years = range(1876, 1909)

# Plot the results
plt.plot(years, US_Day_Att, marker='o', label='US Day Attendance')
plt.plot(years, US_Day_Att_Church, marker='o', linestyle='dotted', label='US Day Attendance Church')
plt.plot(years, Canada_Day_Att, marker='o', label="Canada Day Attendance")
plt.plot(years, Canada_Day_Att_Church, marker='o', linestyle='dotted', label="Canada Day Attendance Church")

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.title('Day Attendance by country')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(years, Canada_Boarding_Att, marker='o', label="Canada Boarding Attendance")
plt.plot(years, Canada_Boarding_Att_Church, marker='o', linestyle='dotted', label="Canada Boarding Attendance")
plt.plot(years, US_Boarding_Att, marker='o', label='US Boarding Attendance')
plt.plot(years, US_Boarding_Att_Church, marker='o', linestyle='dotted', label='US Boarding Attendance Church')

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.title('Boarding Attendance by Country')
plt.legend()
plt.grid(True)
plt.show()