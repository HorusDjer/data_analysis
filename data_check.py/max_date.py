from datetime import datetime
import time
import os

# written by Ejike in python 2.7

# note: catalist updates file name to reflect date modified.
todays_date = datetime.now().strftime('%m%d%y')


file_path = '/data/vansync/ContactsContacts_VF_{}{}'.format(
    todays_date, '.txt')
try:
    with open(file_path, "r") as file_object:
        contents = file_object.readlines()
except IOError:
    msg = "The file path used does not exist"
    print msg

try:
    date_modified = time.ctime(os.path.getmtime(file_path))
    last_record = contents[-1].split("\t")
    date_canvassed = last_record[6]
    date_created = last_record[5]
    print contents[0]

    print "searching for last record"
    time.sleep(1)
    print "..."
    time.sleep(1.5)
    # print contents[-1]
    print "..."
    time.sleep(2)
    print "The last date canvassed in contacts_contacts_vf is:", date_canvassed
    print "The last date created in contacts_contacts_vf is:  ", date_created
    print "\nThis file was last modified", date_modified
    print "\nLookup complete"
except NameError:
    pass
