# s = 'test'
# print(s == s)
# print(dir(s))
import math


class User(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, User):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be User')

    def __add__(self, other):
        if isinstance(other, User):
            return self.age + other.age
        else:
            raise Exception('the type of object must be User')

    def __len__(self):
        return len(self.name)


if __name__ == '__main__':
    user1 = User('wamhcao', 12)
    user2 = User('liqiang', 14)
    print(user1 == user2)
    print(user1 + user2)
    print(len(user1))
