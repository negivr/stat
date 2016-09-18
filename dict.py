import os
from datetime import datetime

f_name = os.path.abspath('ture_panda_names_dates.csv')

print(f_name)

with open(f_name,'r') as f:
    header = f.readline()#.strip().split(',')
    print(header)

    lista =[]

    for line in f:
        items = line.strip().split(',')
        items[5] = items[5][1:]
        items[6] = items[6][:-1]
        # print(items[5])
        # print(items[6])
        items[5] = items[5] + ',' + items[6]
        items[7] = items[7][1:]
        items[8] = items[8][:-1]
        items[6] = items[7] + ',' + items[8] + '\n'
        items = items[:-2]
        lista.append(items)


with open('ture_cisto.csv', 'w') as f:
    f.write(header)
    for line in lista:
        f.write(', '.join(line))





