import pandas as pd

pd.options.display.width = 5000
pd.options.display.max_rows = 999

cols_n = ['Tran Date', 'Tran Time', 'City',  'State/ Prov']

df = pd.read_csv('175 fuel 2015.csv', usecols=cols_n)

# print(list(df.columns.values))



df['Time'] = df['Tran Date'] + ' ' + df['Tran Time']
df['Score'] = df['City'] + ', ' + df['State/ Prov']

df['Time'] = pd.to_datetime(df['Time'])

# cols_of_interest = ['Tran Date', 'Tran Time', 'City', 'State/ Prov']
cols_of_interest = ['Time', 'Score']
df = df[cols_of_interest]

df.to_csv('gorivo.csv', index=None)

print(df.head())



