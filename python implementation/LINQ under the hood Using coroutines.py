"""
note : 1-we can add scheduler to make it more prettier  ,if i have time may be i will do so  ,
       2-we can also use async wait ,instead of doing all this by hand ,but i figure out that doing it like this will make things clear about how coroutine works
"""
l = [1, 2, 3, 4, 5]


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def source(l, target):
    for item in l:
        try:
            target.send(item)
        except StopIteration:
            target.close()


@coroutine
def addone(target):
    try:
        while True:
            print("add get called")
            val = yield
            result = val + 1
            target.send(result)
    except StopIteration:
        target.close()


@coroutine
def substract(target):
    try:
        while True:
            print("substract get called")
            val = yield
            result = val - 10
            target.send(result)
    except StopIteration:
        target.close()


@coroutine
def square(target):
    try:
        while True:
            print("square get called")
            val = yield
            result = val * val
            target.send(result)
    except StopIteration:
        target.close()


@coroutine
def greater(target):
    cond = lambda x: x > 5
    try:
        while True:
            print("greater get called")
            val = yield
            if cond(val):
                target.send(val)
    except StopIteration:
        target.close()


li = []


@coroutine
def take(it):
    flage = True
    while flage:
        print("take get called")
        if it != 0:
            val = yield
            li.append(val)
        else:
            flage = False
        it -= 1


source(l, addone(square(substract(greater(take(2))))))
for item in li:
    print(item)
