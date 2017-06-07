# this code will rename a specific column in a 
# pandas dataframe

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

print(df)

df = df.rename(columns={'x':'zz'})

print("-" * 50)
print(df)
