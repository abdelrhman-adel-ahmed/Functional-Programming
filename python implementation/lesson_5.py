from functools import partial, reduce

mydata = [3, 5, 7, 8]


def SubstractTen(item):
    return item - 10


def Square(item):
    return pow(item, 2)


def AddOne(item):
    return item + 1


def ComposeFunction(f1, f2, f3):
    return lambda item: f3(f2(f1(item)))


def compose(f, g):
    return lambda item: f(g(item))


def AddoneSquareSubstract(item):
    q1 = AddOne
    q2 = Square
    q3 = SubstractTen

    return compose(q3, compose(q2, q1))(item)


# we can also use reduce,but its not recommended :(https://realpython.com/python-functional-programming/#reducing-an-iterable-to-a-single-value-with-reduce)
def composite_fun(*fun):
    def compose(f, g):
        return lambda item: f(g(item))

    return reduce(compose, fun, lambda item: item)


# usual mapping iterable to func
out1 = list(map(SubstractTen, map(Square, map(AddOne, mydata))))
print(out1)

# neasting
out2 = [SubstractTen(Square(AddOne(item))) for item in mydata]
print(out2)

# composition
MyComposeFunction = ComposeFunction(AddOne, Square, SubstractTen)
out3 = list(map(MyComposeFunction, mydata))
print(out3)

# composition
out4 = list(map(AddoneSquareSubstract, mydata))
print(out4)

# using reduce
MyComposeFunction1 = composite_fun(SubstractTen, Square, AddOne)
out5 = list(map(MyComposeFunction1, mydata))
print(out5)
