import os


# Get raw file and strip off " from elements
def remove_quotes_from_file_elements(path_in, path_out):
    lista = []
    with open(path_in, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            for elem in l[:-1]:
                elem = elem.strip('"') + ','
                lista.append(elem)
            l[-1] = l[-1].strip('"') + '\n'
            lista.append(l[-1])
    with open(path_out, 'w') as f:
        for element in lista:
            f.write(element)


def create_driver_directory(drivers_set):
    if not os.path.exists(drivers_set):
        os.mkdir(drivers_set)


def create_driver_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, 'w'):
            pass


def add_trips_to_drivers_directory(path, data):
    with open(path, 'a') as f:
            f.write(data)


def get_drivers(path):
    drivers = set()
    with open(path, 'r') as f:
        for line in f:
            drivers.add(line.split(',')[18])
    return drivers


def get_trips(path, driver):
    trips = set()
    with open(path, 'r') as f:
        for line in f:
            if driver == line.split(',')[18]:
                trips.add(line)
    return trips


vozaci = get_drivers('ture_change.csv')

base_path = os.getcwd()

for vozac in vozaci:
    create_driver_directory(vozac)
    path_name = (os.getcwd() + '/' + vozac + '/' + 'ture.csv')
    create_driver_file(path_name)
    ture = get_trips('ture_change.csv', vozac)
    for linija in ture:
        add_trips_to_drivers_directory(path_name, linija)









