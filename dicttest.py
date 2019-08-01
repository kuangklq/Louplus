#!/usr/bin/env python3

import sys
list_dict = {}
for arg in sys.argv[1:]:
    arg_list = arg.split(':')
    list_dict[arg_list[0]] = arg_list[1]
for key in list_dict:
    print("ID:{0} Name:{1}".format(key, list_dict[key]))
