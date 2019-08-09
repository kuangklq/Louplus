class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.ID, self.Name)

class NewUser(UserData):
    def get_name(self):
        return self.Name
    def set_name(self, value):
        self.Name = value

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.set_name('Jackie')
    user2 = NewUser(102, 'Louplus')
    print(user1)
    print(user2)
