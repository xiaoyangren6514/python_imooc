class User(object):
    def __new__(cls, *args, **kwargs):
        print('new called')
        print(args)
        return super(User, cls).__new__(cls)

    def __init__(self, name, age):
        print('init called')
        self.name = name
        self.age = age


user = User('wangcai', 12)
print(user.age)
