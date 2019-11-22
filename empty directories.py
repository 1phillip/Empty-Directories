import os, sys, shutil
sizeCutoff = None
while type(sizeCutoff) != int:
    try:
        sizeCutoff=int(input("Look for all files equal to or smaller than (bytes): "))
    except ValueError:
        print("Type an integer. \n")
def get_size(start_path = '.'):
    global total_size
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

listOfDirs = []
for root, dirs, files in os.walk(".", topdown=False):
   for name in dirs:
       if get_size(os.path.join(root, name)) <= sizeCutoff:
           print(os.path.join(root, name), total_size, 'bytes')
           listOfDirs.append(os.path.join(root, name))
if len(listOfDirs) > 0:
    delete=input('Delete? (y/n): ').lower()
    if delete=='y':
        for i in listOfDirs:
            shutil.rmtree(i)
            print('deleted %s' % i)
    elif delete == 'n':
        sys.exit()
else:
    print('No files found with that criteria.')
    sys.exit()
