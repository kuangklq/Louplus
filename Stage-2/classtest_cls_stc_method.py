#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.ID, self.Name)  #不是私有属性，不用get_name方法

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(ID, Name):
        return '{1}\'s id is {0}'.format(ID, Name)
    
    def get_name(self):    #返回NewUser对象的名称
        return self.Name
    def set_name(self, value):    #设置NewUser对象的名称为value
        self.Name = value

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109, 'Lucy'))
