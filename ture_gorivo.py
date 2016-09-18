import pandas as pd

pd.options.display.width = 5000
pd.options.display.max_rows = 999

df1 = pd.read_csv('df3.csv')
df1['Time'] = pd.to_datetime(df1.Time)

df2 = pd.read_csv('gorivo.csv')
df2['Time'] = pd.to_datetime(df2.Time)

df = pd.concat([df1, df2])

df = df.sort_values('Time')

df.to_csv('google.csv', index=None)

# print(df1.head())
# print(df2.head())

print(df.head())

