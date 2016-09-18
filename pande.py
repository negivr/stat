import pandas as pd

pd.options.display.width = 5000

cols1 = ['Truck#', 'Ship_Date', 'Delivery_Date', 'Driver', 'Mileage', 'Origin', 'Destination']

df = pd.read_csv('175 ture.csv', index_col = None, usecols=[14, 15, 16, 18, 19, 20, 21], names=cols1)

# df.to_csv('ture_panda_names.csv', index=False)


df['Ship_Date'] = pd.to_datetime(df.Ship_Date)#.dt.date
# df['Ship_Date'] = df['Ship_Date'].dt.date
df['Delivery_Date'] = pd.to_datetime(df.Delivery_Date)#.dt.date
# df['Delivery_Date'] = df['Delivery_Date'].dt.date

# print(df.head())

# print(df.loc[(df.Ship_Date >= pd.to_datetime('10/1/2015')) & (df.Ship_Date <= pd.to_datetime('10/31/2015'))])
# df1 = df.loc[(df.Ship_Date >= pd.to_datetime('9/1/2015')) & (df.Ship_Date <= pd.to_datetime('9/30/2015'))]

# df.to_csv('ture_panda_names_dates.csv', index=False)

# print(df['Ship_Date'] < df['Delivery_Date'])
#
# print(df['Ship_Date'])
# print(df['Delivery_Date'])

# print(df1['Mileage'].sum())

print(df.loc[df.duplicated(), :])




