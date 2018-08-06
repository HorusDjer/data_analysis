from datetime import datetime

# add automatic file change functionality
# note: file name reflects date modified
todays_date = datetime.now().strftime('%m%d%y')
file_path = '/data/vansync/ContactsContacts_VF_{}{}'.format(
    todays_date, '.txt')
# file_path = '/data/vansync/ContactsContacts_VF_080518.txt'
file_path = "/Users/ejikeobineme/Documents/data_analysis/data_check.py/contacts_contact.txt"


with open(file_path, "r") as file_object:
    contents = file_object.readlines()

# put last string into a list to be evaluated.
last_record = contents[-1].split("\t")
date_canvassed = last_record[6]
print(last_record)
print(contents[-1])
print("The last canvassed date recorded in contacts_contact_vf is:", date_canvassed)
