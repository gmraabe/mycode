#!/usr/bin/env python3
# snippet01a.py
# Micah Raabe

# Lab 32 - Snippet.split.join

txtfile = open('ls_mycode.txt', 'r')
txtfile_list = txtfile.readlines()
txtfile.close()

for i in range(len(txtfile_list)):
    txtfile_list[i] = txtfile_list[i].strip()        # strip out the newline characters

txtfile_lista = " ".join(txtfile_list)               # join the list with a single whitespace
print('\n' + txtfile_lista)

txtfile_listb = "\t".join(txtfile_list)              # join the list with a tab
print('\n' + txtfile_listb)

