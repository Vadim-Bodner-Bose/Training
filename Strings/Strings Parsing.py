import re

list_to_parse = ['Index              Network  Security', '0            NETGEAR70           (null) disabled', \
                 '2            NETGEAR70G           (null) disabled']
#  find the line that starts with Index and Ends with security
# check the next line if it starts with a 0"
# check next line if starts with a 1
# check next line if starts with a 9"
# quit and report each lines that is found
# erase profile(s)
# parse the list for profiles
for index, item in enumerate(list_to_parse):
    if re.match('Index', item):
        count = 0
        # print(list_to_parse[index + 1])
        # send command profile 0
        # send command profile erase
    elif re.match('[0-9]', item):
        count +=1
        # if profiles above 1 and through 9 exist
        # remove them.
        print(item)

print("total profiles identified:", count)
