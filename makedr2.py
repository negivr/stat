import os


def create_dirs(path, d_name):
    d_path = os.path.join(path, d_name)
    if not os.path.exists(d_path):
        os.makedirs(d_path)
        print('dir {} kreiran'.format(d_name))
    else:
        print('dir {} postoji'.format(d_name))


def create_file(path, f_name):
    f_path = os.path.join(path, f_name)
    if not os.path.exists(f_path):
        with open(f_path, 'w'):
            pass
        print('file {} kreiran'.format(f_name))
    else:
        print('file {} postoji'.format(f_name))


cd = os.getcwd()
print('cwd: ', cd)

create_dirs(cd, 'proba1/proba2/proba3/proba4')
create_file(cd, 'proba/test.txt')











