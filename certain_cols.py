

file_name = '175 ture.csv'

with open(file_name, 'r') as f:
    lista = []
    for line in f:
        l = line.split(',')
        # Carrier, Tractor, Driver, Ship_Date, Delivery_Date, Trip_Number, Origin, Destination, Mileage
        for i in (0, 14, 18, 15, 16, 17, 19, 20, 21, 22):
            l[15] = l[15][:11]
            l[16] = l[16][:11]
            lista.append(l[i].strip('"') + ',')
        lista.append(l[23].strip('"') + '\n')


with open('ture_clean.csv', 'w') as f:
    for line in lista:
        f.write(line)
