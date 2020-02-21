#!/usr/bin/env python3

filename = input('Enter the file name: ')

with open(filename) as f:
    f_list = list(f)    # 将迭代器f列表化，f_list就不是一次性的了
    '''
    count = 0
    for line in f_list:
        count += 1
    '''
#    print(f_list)
    print(''.join(f_list))    # 列表每个元素就是每行的内容（包括换行符）
    print('lines:', len(f_list))    # 列表获取数量的方法，注意不是.count()
