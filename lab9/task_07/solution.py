def every_other(seq):
    it = iter(seq)
    for x in it:
        yield x
        next(it, None)   # пропускаем следующий элемент


if __name__ == '__main__':
    print(*every_other([10, 20, 30, 40, 50]))
    print(*every_other(range(10)))
    print(*every_other(iter(range(10))))
    print(sum(every_other(map(int, input().split()))))  # ввод: 2 5 11 3 8 -> 21
