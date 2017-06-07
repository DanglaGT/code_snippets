# this code will sort the data in a pandas dataframe
# based on the columns specified

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [9, 9, 5],
    'y': [8, 6, 2]})

print(df)

df1 = df.sort_values(['x', 'y'])
df2 = df.sort_values(['x', 'y'], ascending=False)

print("-" * 50)
print(df1)
print("-" * 50)
print(df2)
