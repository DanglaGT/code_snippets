# this code will create a pandas dataframe out of a Python
# dictionary. this is a convenient way to do it when your
# data set is small

import pandas as pd

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data 
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

print(df)
