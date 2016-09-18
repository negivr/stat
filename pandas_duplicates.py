import pandas as pd

pd.options.display.width = 5000
pd.options.display.max_rows = 999

# df = pd.read_csv('175 ture 1.csv')
#
# cols1 = ['Truck', 'Ship_Date', 'Delivery_Date', 'Trip_Num', 'Driver', 'Mileage', 'Origin', 'Destination']
#
# df = pd.read_csv('175 ture 1.csv', index_col = None, usecols=[14, 15, 16, 17, 18, 19, 20, 21], names=cols1)
#
# df.to_csv('175.csv', index=None)

# df = pd.read_csv('175.csv') #, sep = ',', header=None, names=cols1)

# print(df)

# df_dup = df.loc[df.duplicated(), :]

# duplo = df.loc[df.duplicated(), :]

# print(duplo)

# df1 = duplo.loc[:, ['Ship_Date', 'Origin']]
#
# df1['Ship_Date'] = pd.to_datetime(df1['Ship_Date'])
#
# df1.to_csv('dvekolone1.csv', index=None)


# df1 = duplo.loc[:, ['Delivery_Date', 'Destination']]
#
# df1['Delivery_Date'] = pd.to_datetime(df1['Delivery_Date'])
#
# df1.to_csv('dvekolone2.csv', index=None)


df1 = pd.read_csv('dvekolone1.csv', index_col=0, header=None, skiprows= 1)
df2 = pd.read_csv('dvekolone2.csv', index_col=0, header=None, skiprows= 1)
#
# # print(df1)
# # print(df2)
#
df = pd.concat([df1, df2])


# df.to_csv('dvekolone.csv', header=None)
# # df1.sort_values('Ship_Date')

# df = pd.read_csv('dvekolone.csv', index_col = None, names=['Datum', 'Grad'])
#
# df['Datum'] = pd.to_datetime(df.Datum)
# print(df['Datum'].dtypes)
#
# # df.sort_values('Datum')
# df5 = df.sort_values(by='Datum')

print(df)














