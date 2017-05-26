class User(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __str__(self):
        return 'name is ' + self.name + ',age is ' + str(self.age)

    def __dir__(self):
        # return super(User, self).__dir__()
        return self.__dict__.keys()

    def __setattr__(self, key, value):
        print('setattr called key = %s value = %s' % (key, value))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        print('getattribute called item = %s' % item)
        # self.__dict__.get(item) 和 getattr()方法一样，会造成递归一场
        return super(User, self).__getattribute__(item)


if __name__ == '__main__':
    user1 = User('wamhcao', 12)
    user1.name = 'xaa'
    print(user1.name)
