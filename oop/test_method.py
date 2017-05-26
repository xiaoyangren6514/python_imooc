class User(object):

    hobby = 'ball'

    def __init__(self,name,age):
        self.__name = name
        self.__age  = age

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @classmethod
    def eat(cls):
        print( 'eat')

    def run(self):
        print('run')

    @property
    def get_name(self):
        return self.__name


u = User('旺财',12)
u.run()
u.run = '123'
print(u.run)
u.eat()
User.eat()
print(u.get_name)
print(u.get_hobby())
print(User.get_hobby())