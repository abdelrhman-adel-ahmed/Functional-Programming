from itertools import islice

mydata = [7, 4, 5, 6, 3, 8, 10]


def SubstractTen(item):
    return item - 10


def Square(item):
    return pow(item, 2)


def AddOne(item):
    return item + 1


# --------------------imperative--------------------------

for item in mydata:
    print(SubstractTen(Square(AddOne(item))))

# --------------------declerative-------------------------

out1 = list(map(SubstractTen, map(Square, map(AddOne, mydata))))

# add one then square then only select x <20 to pass them to the last step (SubstractTen)
ou2 = list(map(SubstractTen, filter(lambda x: x < 20, map(Square, map(AddOne, mydata)))))

# add one then square then only select x <70 and only take two then pass them to the last step (SubstractTen)
out3 = list(map(SubstractTen, islice(sorted(filter(lambda x: x < 70, map(Square, map(AddOne, mydata)))), 2)))

print(out3)
