l = [1, 2, 3, 4, 5]


def addone(x):
    print("add got called")
    return x + 1


def substract10(x):
    print("substract10 got called")
    return x - 10


def sqaure(x):
    print("sqaure got called")
    return x * x


def doAddone():
    for item in l:
        yield addone(item)


def doSubstract10():
    for item in doSquare():
        yield substract10(item)


def doSquare():
    for item in doAddone():
        yield sqaure(item)


def doWhere():
    cond = lambda x: x > 5
    for item in doSubstract10():
        if cond(item):
            yield item


def doTaketwo():
    n = 2
    i = 0
    flag = True
    generator_obj = doWhere()
    while flag:
        if n != i:
            item = yield next(generator_obj)
        else:
            flag = False
        n -= 1


print(list(doTaketwo()))
