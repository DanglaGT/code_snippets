
import pandas as pd

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'

tips = pd.read_csv(url)

print(tips.head())

# export to new csv file
tips.to_csv('tips2.csv')
