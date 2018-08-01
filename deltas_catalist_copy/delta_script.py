import os
import datetime
import shutil

def rename_to_date(file):
    pass

print(os.getcwd())
print(os.listdir())

# get the name of directory that holds current script.
path = os.path.dirname(__file__)

# change current directory to directory that contains the file.
os.chdir(path)
files_in_dir = os.listdir()

# remove hidden files & script file from project list.
proj_dir = list(filter(lambda z: not z.startswith("."), files_in_dir))
script_file = os.path.basename(__file__)
proj_dir.remove(script_file)

print(proj_dir)
print(os.getcwd())

# rename txt files from proj_dir to reflect date created.
print(os.listdir())

for file in files_in_dir:
    if file in proj_dir:
        rename_to_date(file)


# files = os.listdir(path)
# i = 1

# for file in proj_dir:
#     if
#     filename, file_extension = os.path.splitext(file)
#     os.rename(os.path.join(path, file), os.path.join(path, filename + str(i) 
#                                                           + file_extension))
#     i = i+1


