# this code demonstrates how to inner join
# 2 pandas dataframes together

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': np.random.randn(4)})

df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
                    'value': np.random.randn(4)})

print(df1)
print("-" * 50)
print(df2)
print("-" * 50)

inner_join = df1.merge(df2, on=['key'], how='inner')
print("Inner Join:")
print(inner_join)
