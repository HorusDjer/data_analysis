from datetime import datetime
import time
import os

# written in python 2.7

print "Starting lookup..."

# note: catalist updates file name to reflect date modified.
todays_date = datetime.now().strftime('%m%d%y')
file_path = '/data/vansync/ContactsContacts_VF_{}{}'.format(
    todays_date, '.txt')

try:
    with open(file_path, "r") as file_object:
        contents = file_object.readlines()
        all_canvassed_dates = []
        for line in contents[-200000:-1]:
            if line != contents[0]: # use in case we need to parse out whole file.
                record = line.split()
                canvassed_date = record[7] + " " + record[8]
                datetime_object = datetime.strptime(canvassed_date, '%Y-%m-%d %H:%M:%S')
                all_canvassed_dates.append(datetime_object)
except IOError:
    msg = "The file path used does not exist"
    print msg

try:
    date_modified = time.ctime(os.path.getmtime(file_path))
    last_record = contents[-1].split("\t") # assumes last row contains most recent date created.
    date_created = last_record[5]
    
    print contents[0]
    print "searching"
    time.sleep(1)
    print "..."
    time.sleep(1.5)
    # print contents[-1]
    print "..."
    time.sleep(2)
    print "The last date canvassed in contacts_contacts_vf is:", max(all_canvassed_dates)
    print "The last date created in contacts_contacts_vf is:  ", date_created
    print "\nThis file was last modified", date_modified
    # print "The length of the list: ", len(all_canvassed_dates)
    
    print "\nLookup complete"
except NameError:
    pass