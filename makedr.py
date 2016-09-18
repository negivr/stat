import os

crtdir = os.getcwd()

print(crtdir)

fpath = os.path.join(crtdir, 'PHIL-MCNE/ture.csv')
print(fpath)

# os.system("<text editor> <file name with extension>") #http://askubuntu.com/questions/675270/when-i-open-gedit-from-terminal-i-am-unable-to-use-terminal-for-anything-else-u
os.system('gedit {} &'.format(fpath))

print(os.path.isfile(fpath))
print(os.path.isdir(fpath))



