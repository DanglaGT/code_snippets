# this code demonstrates how to check the data types
# of the columns in a pandas dataframe

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'gender': ['Male', 'Male', 'Female', 'Male', 'Female'],
    'age': [28, 21, 19, 18, 30],
    'bday': [pd.Timestamp('1989-05-05'), pd.Timestamp('2013-01-15'),
             pd.Timestamp('2019-01-15'), pd.Timestamp('2010-01-15'),
             pd.Timestamp('2013-09-08')]
    })

print(df.dtypes)
