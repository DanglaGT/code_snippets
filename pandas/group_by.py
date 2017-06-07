# this code demonstrates how to run a "group by" on
# a pandas dataframe

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'gender': ['Male', 'Male', 'Female'],
    'age': [28, 21, 19]})

print(df)

df_summed = df.groupby(['gender'])['age'].sum()

print("-" * 50)
print(df_summed)
