import pandas as pd

df = pd.read_json('./state_of_js_2016_2020.json')

# print(df.head())

df.to_csv('state_of_js.csv')
