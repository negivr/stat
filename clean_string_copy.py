

# lines = []
# with open('175 ture 1.csv', 'r') as f:
#         for line in f:
#             # list_existing.add(line)
#             lines.append(line)
# lines_set = set(lines)
# print(sorted(lines_set))
#
# with open('ture_no_duplikat.csv', 'w')as f:
#     for line in sorted(lines_set):
#         f.write(line)

def raw_file_to_main_file(main_file_name, raw_file_name):
    list_existing = []
    with open(main_file_name, 'r') as f:
        for line in f:
            list_existing.append(line)
    list_existing_set = set(list_existing)

    list_raw = []
    with open(raw_file_name, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            for elem in l[:-1]:
                elem = elem.strip('"').strip() + ', '
                list_raw.append(elem)
            l[-1] = l[-1].strip('"').strip() + '\n'
            list_raw.append(l[-1])
    list_raw_set = set(list_raw)

    list_to_file = list_existing_set | list_raw_set

    with open(main_file_name, 'w') as f:
        for line in sorted(list_to_file):
            f.write(line)

raw_file_to_main_file('ture.csv', '175 ture 2.csv')


