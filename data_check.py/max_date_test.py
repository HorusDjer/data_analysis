from datetime import datetime
import time
import os

# add automatic file change functionality
# note: file name reflects date modified
todays_date = datetime.now().strftime('%m%d%y')

""" file_path = '/data/vansync/ContactsContacts_VF_{}{}'.format(
    todays_date, '.txt') """

file_path = "/Users/ejikeobineme/Documents/data_analysis/data_check.py/contacts_contact.txt"
date_modified = time.ctime(os.path.getmtime(file_path))

""" try:
    with open(file_path, "r") as file_object:
        contents = file_object.readlines()
        all_canvassed_dates = []
        for line in contents:
            if line != contents[0]:
                record = line.split()
                canvassed_date = record[7] + " " + record[8]
                datetime_object = datetime.strptime(canvassed_date, '%Y-%m-%d %H:%M:%S')
                all_canvassed_dates.append(datetime_object) """

try:
    with open(file_path, "r") as file_object:
        contents = file_object.readlines()
        for line in contents:
            if line != contents[0]:
                
                all_canvassed_dates = list(map(datetime.strptime(canvassed_date, '%Y-%m-%d%H:%M:%S'), line.split()[7:9]))             

except IOError:
    msg = "The file path used does not exist"
    print(msg)

try:
    date_modified = time.ctime(os.path.getmtime(file_path))
    last_record = contents[-1].split("\t")
    date_canvassed = last_record[6]
    date_created = last_record[5]
    print(contents[0])

    print("searching for last record")
    # time.sleep(1)
    print("...")
    # time.sleep(1.5)
    # print contents[-1]
    print("...")
    # time.sleep(2)
    print("The last date canvassed in contacts_contacts_vf is:", max(all_canvassed_dates))
    print("The last date created in contacts_contacts_vf is:  ", date_created)
    print("\nThis file was last modified", date_modified)

    print("\nLookup complete")
except NameError:
    pass
