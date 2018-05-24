#!/usr/bin/env python3
# keystone_counter.py
# Micah Raabe

loginfail = 0               # initialize fail counter and set initial value to 0
loginsucess = 0             # initialize sucess counter and set initial value to 0
ipfail = []
keystone_file = open('/home/student/bin/keystone.common.wsgi', 'r')    # open log file readonly
keystone_file_lines=keystone_file.readlines()              # create a list that contains the lines of the log file
keystone_file.close()                 # close log file

for i in range(len(keystone_file_lines)):           # loop for each line in the log file
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1        # increment fail counter
        keystone_file_line=keystone_file_lines[i]
        keystone_file_words=keystone_file_line.split()
        ipfail.append(keystone_file_words[keystone_file_words.__len__() - 1])
    elif "-] Authorization failed" in keystone_file_lines[i]:
        loginsucess += 1        # increment sucess counter
print('The number of failed log in attempts is ' + str(loginfail))
print('The IP addresses of the failed log in attempts are ' + str(ipfail))
print('The number of sucessful log in attempts is ' + str(loginsucess))

