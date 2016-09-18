import pandas as pd

# ufo = pd.read_csv('http://bit.ly/uforeports')
# ufo.to_csv('uforeports.csv', index=None)

ufo = pd.read_csv('uforeports.csv')

# print(ufo.head(3))

'''
loc is for filtering rows and selecting columns by LABEL (label for rows is index, label for columns is column name
'''

# print(ufo.loc[0:3, 'City' : 'State'])

# print(ufo.loc[ufo.City == 'Oakland', 'State'])


'''
iloc is for filtering rows and selecting columns by INTEGER POSITION (odatle 'i' ispred loc)
'''

# print(ufo.iloc[:, [0, 3]])

print(ufo.loc[:, ['City', 'State']])

'''
ix is combination between loc and iloc - KORISTI SAMO AKO MORAS!!!

    ufo.ix[0:2, 0:2] -> ufo.ix[0(inclusive):2(inclusive), 0(inclusive):2(exclusive)]
-
'''


