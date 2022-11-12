# честно говоря, меня не было, поэтому в 1 не понял как что, и в 7 =)


def second():
    arr = [int(input("введите 1 число")), int(input("введите 2 число")), int(input("введите 3 число")),
           int(input("введите 4 число"))]
    print("они равны" if sum(arr) == arr[0] * 4 else "не равны")


def third():
    size = int(input("введите кол-во эл"))
    list = []
    for i in range(size):
        list.append(int(input("введите " + str(i) + " число")))
    k = int(input("введите число элементов"))
    print(sorted(list)[len(list) - k:])


def fourth():
    size = int(input("введите кол-во эл"))
    list = []
    for i in range(size):
        list.append(int(input("введите " + str(i) + " число")))
    k = int(input("введите число элементов"))
    print(sorted(list, reverse=True)[len(list) - k:])


def fifth():
    size = int(input("введите кол-во эл"))
    li = []
    for i in range(size):
        li.append(int(input("введите " + str(i) + " число")))
    avg = sum(li) / len(li)
    print(list(filter(lambda val: val > avg, li)))


def sixth():
    x = int(input("введите число 1"))
    y = int(input("введите число 2"))
    mult = 0

    for i in range(abs(y)):
        mult += x

    print("ответ: " + str(mult if y > 0 else -mult))


def eighth():
    print("ответ: " + str((int(input("введите градус")) - 32) / 1.8))


def ninth():
    print("ответ: " + str(float(input("введите массу тела")) / pow(float(input("введите рост")), 2)))


def tenth():
    a = int(input("введите число"))
    print("квадрат: " + str(pow(a, 2)) + "\nкуб: " + str(pow(a, 3)) + "\nчетвертая степень: " + str(pow(a, 4)))


def eleven():
    a = int(input("введите 1 сторону"))
    b = int(input("введите 2 сторону"))
    c = int(input("введите 3 сторону"))
    print("могут" if (a + b > c) and (a + c > b) and (b + c > a) else "не могут")
