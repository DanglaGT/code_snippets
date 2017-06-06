
import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

df2 = df[df['y'] >= 4]

print(df)
print("-" * 50)
print(df2)
