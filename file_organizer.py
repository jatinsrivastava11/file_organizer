"""FILE ORANIZER BY EXTENSIONS"""

import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    name,extension = os.path.splitext(file)
    extension = extension[1:] #to remove the dot from extension name through slicing

    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
    
    