#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.ID, self.Name)  #不是私有属性，不用get_name方法

class NewUser(UserData):
    def get_name(self):    #返回NewUser对象的名称
        return self.Name
    def set_name(self, value):    #设置NewUser对象的名称为value
        self.Name = value

if __name__ == '__main__':
    user1 = NewUser(101, 'jack')
    user1.set_name('Jackie')    #使用set_name方法设置对象的名称
    user2 = NewUser(102, 'Louplus')
    print(user1)
    print(user2)
