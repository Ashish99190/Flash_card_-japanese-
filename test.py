# Read the CSV file into a DataFrame
import pandas
df = pandas.read_csv('data.csv')

# Convert DataFrame to dictionary, excluding index column
data_dict = df.to_dict('records', index=False)
print(data_dict)
