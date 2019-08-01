#!/usr/bin/env python3

num = input("Enter a number:")
try:
    new_num = int(num)
    print('INT:{}'.format(new_num))
except ValueError:
    print('ERROR: abc')
