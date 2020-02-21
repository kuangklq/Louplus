#!/usr/bin/env python3

filename = input('Enter the file name: ')

with open(filename) as f:
    count = 0
    for line in f:
        count += 1
        print(line)
    print('lines: ', count)

# 关联文件test.txt，其内容为'''……'之间的内容
'''
I love Python
lou+ at shiyanlou.com
'''
