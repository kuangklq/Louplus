#!/usr/bin/env python3

def change():
    global a
    print(a)
    a = 90
a = 9
print("before",a)
print("inside",end=' ')
change()
print("after",a)
