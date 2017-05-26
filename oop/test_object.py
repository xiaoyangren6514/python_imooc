class User(object):
    """
    成员变量，可以通过类名饮用，所有对象共有
    如果对象修改了成员变量的值，不会影响其他对象的值
    如果通过类名调用直接修改了成员变量的值，那么所有对象对应的值都发生变化，除非对象之前修改过此值
    """
    address = 'bj'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    user = User('wangcai', 12, 98)
    print(user)
    print(dir(user))
    print(user.__dict__)
    print(user.name)
    print(user._age)
    print(user.get_weight())
    print(user.address)
    user.address = 'tj'
    print(user.address)
    user2 = User('daqiang', 19, 22)
    print(user2.address)
    print(User.address)
    User.address = 'sd'
    print(user.address)
    print(user2.address)
