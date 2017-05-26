class Animal(object):
    hobby = 'eat huo tui'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.weight

    def say_hello(self):
        print('animal say hello')


class Dog(Animal):
    def __init__(self, name, weight, color):
        super(Dog, self).__init__(name, weight)
        self.color = color

    def say_hello(self):
        print('dog say hello')


def say(anim):
    if isinstance(anim, Animal):
        anim.say_hello()


if __name__ == '__main__':
    dog = Dog('wangcai', 12, 'blue')
    dog.say_hello()
    say(dog)
