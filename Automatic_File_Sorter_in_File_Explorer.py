# operating system and ability to conduct high level operations on files
import os, shutil
# use the r before the string to create a 'raw string'
path = r"/Users/haleybengtson/Anatta Dropbox/Haley Bengtson/My Mac (anatta’s MacBook Pro)/Desktop/Anatta/Python Tutorial/"
# look to see what files are in our path and if there are folders in our path already
file_name = os.listdir(path)
# create folders for our different types of files we have
folder_names = ['csv files', 'image files', 'text files']

for folder in range(0,3):
    if not os.path.exists(path + folder_names[folder]):
        print(path + folder_names[folder])
        os.makedirs(path + folder_names[folder])
# for each file in the folder, we want to move them to their respective folders based on their file type
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif (".jpeg" in file or ".jpg" in file or ".png" in file) and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif (".txt" in file or ".pdf" in file) and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        continue
