#!/usr/bin/env python3
'''
import sys
list_dict = {}
for arg in sys.argv[1:]:
    arg_list = arg.split(':')
    list_dict[arg_list[0]] = arg_list[1]
for key in list_dict:
    print("ID:{0} Name:{1}".format(key, list_dict[key]))
'''

import sys
output_dict = {}

def handle_data(arg):
    list_ = arg.split(':')
    output_dict[list_[0]] = list_[1]

def print_data(key,value):
    print("ID:{0} Name:{1}".format(key,value))

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        handle_data(arg)
    for key in output_dict:
        print_data(key,output_dict[key])
