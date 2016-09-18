from general import *

# ture_set_1 = file_to_set("175 ture 1.csv")
# ture_set_2 = file_to_set("175 ture 2.csv")

# ture_set = ture_set_1 | ture_set_2

# set_to_file(ture_set, 'ture.csv')

# test_set_1 = file_to_set("test1.csv")
# test_set_2 = file_to_set("test2.csv")
#
#
# test = test_set_1 | test_set_2


# set_to_file(test, 'test.csv')


# lista = []



# a = 0
#
# with open('175 ture.csv', 'r') as f:
#     for line in f:
#         l = float(line.strip().split(',')[19].strip('"'))
#         # l = line.strip().split(',')[19] # ture_change.csv
#         a+= l      #float(a)

# print(a)


def raw_file_to_clean_file(file_in, file_out):

    lista = []
    with open(file_in, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            for elem in l[:-1]:
                elem = elem.strip('"').strip() + ', '
                lista.append(elem)
            l[-1] = l[-1].strip('"').strip() + '\n'
            lista.append(l[-1])
    with open(file_out, 'w') as f:
        for line in lista:
            f.write(line)


def raw_file_to_main_file(main_file_name, raw_file_name):
    list_existing = set()
    with open(main_file_name, 'r') as f:
        for line in f:
            list_existing.add(line)

    list_raw = set()
    with open(raw_file_name, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            for elem in l[:-1]:
                elem = elem.strip('"').strip() + ', '
                list_raw.add(elem)
            l[-1] = l[-1].strip('"').strip() + '\n'
            list_raw.add(l[-1])

    list_to_file = list_existing | list_raw

    with open(main_file_name, 'w') as f:
        for line in list_to_file:
            f.write(line)

    # print(list_existing)
    # print(list_raw)



raw_file_to_clean_file('175 ture 1.csv', 'ture.csv')
# raw_file_to_main_file('ture.csv', '175 ture 2.csv')




