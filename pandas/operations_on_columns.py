
import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

print(df)

# adding column x and column y in newly created
# column z
df['z'] = df['x'] + df['y']

print(df)
