import pandas as pd

# Read the CSV file into a DataFrame
input_file_path = 'InputFileCSV.csv'
df = pd.read_csv(input_file_path)

# Display the DataFrame to verify the structure
print("Original DataFrame:")
print(df)

# Check the data types of the columns
print("Data Types before conversion:")
print(df.dtypes)

# Find the 'revenue' row by its label
revenue_row_index = df[df.iloc[:, 0].str.contains('revenue', case=False, na=False)].index[0]

# Display the values in the 'revenue' row before conversion
print("Revenue row values before conversion:")
print(df.iloc[revenue_row_index, 1:])

# Remove commas, extra spaces, and convert the relevant columns to numeric to ensure correct multiplication
df.iloc[revenue_row_index, 1:] = df.iloc[revenue_row_index, 1:].replace({',': ''}, regex=True).str.strip().astype(float)

# Display the values in the 'revenue' row after conversion
print("Revenue row values after conversion:")
print(df.iloc[revenue_row_index, 1:])

# Multiply the revenue row for each quarter by the specified factor
df.iloc[revenue_row_index, 1] *= 2  # 2024 Q1
df.iloc[revenue_row_index, 2] *= 4  # 2024 Q2
df.iloc[revenue_row_index, 3] *= 6  # 2024 Q3
df.iloc[revenue_row_index, 4] *= 8  # 2024 Q4

# Display the DataFrame to verify the changes
print("Modified DataFrame:")
print(df)

# Output the modified DataFrame to a new CSV file
output_file_path = 'OutputFileCSV.csv'
df.to_csv(output_file_path, index=False)

print("Data has been processed and saved to OutputFileCSV.csv")
