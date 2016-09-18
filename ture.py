import pandas as pd

pd.options.display.width = 5000
pd.options.display.max_rows = 999


# df = pd.read_csv('175.csv')
#
# # duplo_ne = df.loc[df.drop_duplicates()]
# d = df.drop_duplicates()
#
#
# df1 = d.loc[:, ['Ship_Date', 'Origin']]
# df2 = d.loc[:, ['Delivery_Date', 'Destination']]
#
# df1.columns = ['Time', 'Score']
# df2.columns = ['Time', 'Score']
#
# df3 = pd.concat([df1, df2])
#
#
# df3.to_csv('df3.csv', index=None)


df = pd.read_csv('df3.csv')

df['Time'] = pd.to_datetime(df.Time)

df1 = df.sort_values('Time')

print(df1.head())

print(df.head())

