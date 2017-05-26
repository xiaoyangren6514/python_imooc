filename = 'test01.txt'


def find_str01(filename):
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('imooc'):
                print(line)


def find_str02(filename):
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('imooc') and line.endswith('imooc'):
                print(line)


if __name__ == '__main__':
    pass
    # find_str01(filename)
    # find_str02(filename)
