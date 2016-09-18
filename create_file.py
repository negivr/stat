import os


def file_to_set(file_name):
    lista = set()
    with open(file_name, 'r') as f:
        for line in f:
            lista.add(line)
        return lista


def write_set_to_file(file_name, lista_set):
    for line in lista_set:
        with open(file_name, 'a') as f:
            f.write(line)


def append_set_to_file(file_name, lista_set):
    for line in lista_set:
        with open(file_name, 'a') as f:
            f.write(line)


def raw_file_to_clean_file(file_in, file_out):

    lista = []
    with open(file_in, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            for elem in l[:-1]:
                elem = elem.strip('"') + ','
                lista.append(elem)
            l[-1] = l[-1].strip('"') + '\n'
            lista.append(l[-1])
    with open(file_out, 'w') as f:
        for line in lista:
            f.write(line)

raw_file_to_clean_file('175 ture 1.csv', 'ture_temp_1.csv')
raw_file_to_clean_file('175 ture 2.csv', 'ture_temp_2.csv')
lista1 = file_to_set('ture_temp_1.csv')
lista2 = file_to_set('ture_temp_2.csv')

lista = lista1 | lista2

write_set_to_file('ture.csv', lista)

lista = []
with open('ture.csv', 'r') as f:
    for line in f:
        lista.append(line.strip().split(','))

lista.sort(key=lambda e: e[15])


with open('ture1.csv', 'w') as f:
    for sublist in lista:
        for item in sublist:
            f.write(item + ',')
        f.write('\n')











