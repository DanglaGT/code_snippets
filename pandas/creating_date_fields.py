
import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

print(df)
print("-" * 50)

# create new date field in df dataframe
df['date1'] = pd.Timestamp('2013-01-15')

# create another new datefield in df dataframe
df['date2'] = pd.Timestamp('2015-02-15')

# create a new field with only the year from date1
df['date1_year'] = df['date1'].dt.year

# create a new field with only the month from date2
df['date2_month'] = df['date2'].dt.month

# create a new field that calculates the number of months between 2 dates
df['months_between'] = (df['date2'].dt.to_period('M') -
                        df['date1'].dt.to_period('M'))

print(df)
