# this code demonstrates how to outer join
# two pandas dataframes

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

outer_join = df1.merge(df2, on=['key'], how='outer')
print("Outer Join:")
print(outer_join)
