#!/usr/bin/env python3

import sys
for arg in sys.argv[1:]:
    arg_list = arg.split(':')
    a, b = arg_list
    print('ID:{0} Name:{1}'.format(a, b))
