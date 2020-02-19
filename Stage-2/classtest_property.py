#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self._Name = Name

class NewUser(UserData):
    @property
    def name(self):    #返回NewUser对象的名称
        return self._Name
    @name.setter
    def name(self, value):    #设置NewUser对象的名称为value
        if len(value) > 3:
            self._Name = value
        else:
            print('ERROR')

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
