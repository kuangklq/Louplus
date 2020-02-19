#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self._Name = Name

class NewUser(UserData):
    @property
    def name(self):    # 返回NewUser对象的名称
        return self._Name
    @name.setter
    def name(self, value):    # 设置NewUser对象的名称为value
        self._Name = value
    def __call__(self):
        print('{1}\'s id is {0}'.format(self.ID, self._Name))

if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()
