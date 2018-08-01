import os
import datetime
import shutil

print(os.getcwd())
print(os.listdir())
files_in_dir = os.listdir()

# remove hidden files to create project list.
proj_dir = list(filter(lambda z: not z.startswith("."), files_in_dir))
print(proj_dir)


