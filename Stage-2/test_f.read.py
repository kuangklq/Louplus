#!/usr/bin/env python3

filename = input('Enter the file name: ')

with open(filename) as f:    # open函数决定了f是迭代器
    count = 0
    for line in f:
        count += 1
        print(line)    # 打印第1行内容，且第1行已经被for循环迭代出来了
        print(f.read())    # 打印剩余的内容，用完这一次f就没有了
    print('lines: ', count)    # for只循环1次，所以count＝1
