import os
from datetime import datetime
import shutil


def rename_to_date(file):
    # find the date the file was created
    # file_data = os.stat(file)
    # modification_date = os.stat.st_mtime
    # file_stats = os.stat(file)
    # file_date = datetime.fromtimestamp(file_time).strftime("%Y-%m-%d")
    # filename, file_extension = os.path.splitext(file)
    # new_name = "{0}_{1}{2}".format(file_date, filename, file_extension)
    # os.rename(file, new_name)
    pass


# print(os.getcwd())
# print(os.listdir())

# get the name of directory that holds current script.
path = os.path.dirname(__file__)

# change current directory to directory that contains the file.
os.chdir(path)
files_in_dir = os.listdir()

# remove script file & hidden files from project list.
proj_dir = list(filter(lambda z: not z.startswith("."), files_in_dir))
script_file = os.path.basename(__file__)
proj_dir.remove(script_file)

# print(proj_dir)
# print(os.getcwd())

# rename txt files from proj_dir to reflect date created.
# print(os.listdir())

# print(os.path.getctime(path))
file_time = os.path.getmtime(path)
file_date = datetime.fromtimestamp(file_time).strftime("%Y-%m-%d")
print("file_date:", file_date)
print("path: ", path)

# get stats of particular file.
file_stats = os.stat("catalist_import_log.txt")

# get modification date of the file.
print("os.stat.st_mtime:", file_stats.st_ctime)

# convert epoch time in year month day format.
cat3 = os.path.getctime("catalist_import_log.txt")
file_date = datetime.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d")
print(file_date)

created_date = os.path.getctime("catalist_import_log.txt")
file_date = datetime.fromtimestamp(file_stats.st_birthtime).strftime("%Y-%m-%d")

print(file_date)

for file in files_in_dir:
    if file in proj_dir:  # and not file.startswith("2018"):
        rename_to_date(file)


# files = os.listdir(path)
# i = 1

# for file in proj_dir:
#     filename, file_extension = os.path.splitext(file)
#     os.rename(os.path.join(path, file), os.path.join(path, filename + str(i)
#                                                           + file_extension))
#     i = i+1
