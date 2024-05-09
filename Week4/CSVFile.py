
#Implement a Python script that reads data from a CSV file, performs some processing, and writes the results to a new CSV file.

import pandas as pd
data = pd.read_csv("/Users/likhithanarayana/Desktop/TESTCSV.csv")

print(data)
print(data.columns)

print("  DATA MANIPULATION  ")
columns = int(input("Enter number of columns you want to add: "))
rows = int(input("Enter number of rows you want to add: "))


data = {}
for i in range(columns):
    col_name = input(f"Enter name for column {i+1}: ")
    data[col_name] = []

for i in range(rows):
    print(f"Enter data for row {i+1}:")
    for col_name in data.keys():
        value = input(f"Enter value for {col_name}: ")
        data[col_name].append(value)

df = pd.DataFrame(data)
print(df)
df.to_csv('/Users/likhithanarayana/Desktop/DataAddCSV.csv')
