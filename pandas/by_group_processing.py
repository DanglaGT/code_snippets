# this code demonstrates how to use by-group processing
# to select the first row of each gender

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'gender': ['Male', 'Male', 'Female', 'Male', 'Female'],
    'age': [28, 21, 19, 18, 30]})

print(df)

df2 = df.groupby(['gender']).first()

print("-" * 50)
print(df2)
