
# this code creates a new column named "flg" that
# sets the value to high if x is greater than 3, 
# otherwise it sets the value to low

import pandas as pd
import numpy as np

# using a dictionary to create a pandas dataframe
# the keys are the column names and the values are the data
df = pd.DataFrame({
    'x': [1, 3, 5],
    'y': [2, 4, 6]})

print(df)

df['flg'] = np.where(df['x'] > 3, 'high', 'low')

print("-" * 50)
print(df)
