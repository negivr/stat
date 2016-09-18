
l_list = []

with open('ture.csv', 'r') as f:
    for i in range(5):
        l = f.readline().strip().split(',')
        l1 = []
        for elem in l[:-1]:
            l1.append(elem.strip() + ',')
        l1.append(l[-1].strip() + '\n')
        l_list.append(l1)


with open('ture_strip.csv', 'w') as f:
    for line in l_list:
        for elem in line:
            f.write(elem)









