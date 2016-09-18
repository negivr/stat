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
# with open('test.csv', 'r') as f:
#     for line in f:
#         # l = line.split()
#         a+= int(line.split()[4])
#
# print(a)


a = 0

with open('175 ture.csv', 'r') as f:
    for line in f:
        # l = float(line.strip().split(',')[19].strip('"'))
        l = line.strip().split(',')[19] # ture_change.csv
        # a+= l      #float(a)
        print(type(l), l)

# print(a)







