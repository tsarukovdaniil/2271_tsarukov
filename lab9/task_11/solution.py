def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper


if __name__ == '__main__':
    add = toint(lambda a, b: a + b)
    print(add('3', '4'))               # 7 (без toint было бы '34')
    print(toint(max)('5', '12', '7'))  # 12 (для строк max вернул бы '7')
    print(toint(range)('5'))           # range(0, 5)
    print(toint(pow)('2', '10'))       # 1024
