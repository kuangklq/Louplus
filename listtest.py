#!/usr/bin/env python3

import sys

'''
str1 = ''
str2 = ''
for arg in sys.argv[1:]:
    if len(arg) <= 3:
        str1 = str1 + arg + ' '
    else:
        str2 = str2 + arg + ' '
print('{}\n{}'.format(str1, str2))
'''

list1 = []
list2 = []
for arg in sys.argv[1:]:
    if len(arg) <= 3:
        list1.append(arg)
    else:
        list2.append(arg)
print(' '.join(list1))
print(' '.join(list2))
