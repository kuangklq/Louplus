#!/usr/bin/env python3

src = '/home/shiyanlou/shiyanlou.txt'
dst = '/home/shiyanlou/shiyanlou_copy.txt'
with open(src) as src_f:
    src_list = src_f.readlines()
    with open(dst, 'w') as dst_f:
        for i, x in enumerate(src_list):
            dst_f.write('{} {}'.format(i+1, x))  # 末尾不需加\n，因为列表每个x末尾已有
