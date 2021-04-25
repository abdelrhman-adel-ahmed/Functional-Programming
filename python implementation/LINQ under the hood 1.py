from itertools import islice

"""
note: all previous implementations i used map,filter,... all these function are generators,some of 
them are coroutines hence there are using lazy evaluation ,so they are optimal as linq, kindaa off :)
note: there is differnce between coroutines and generators 
*generators: provied values for iteration (using yield as statment)
*coroutines: consume values we send by using send() function .(using yiled as expression,and can be 
used as statement and expression !)
if any one want more materiales to understand generators ,coroutines,async programming in python
contact me .. 
"""
# l = [2, 1, 3, 6, 9, 10, 11, 13, 18]
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


# x = list(islice(filter(lambda x: x > 5, map(substract10, map(sqaure, map(addone, l)))), 2))
print(x)


def onebyone():
    for num in l:
        yield num


# genrator_obj = onebyone()
"""
note: for loop in python create a generator object and then call the next function on that genrator
each iteration unitll it get stopiteration error then it exit
"""
for num in onebyone():
    print(num)

# or
try:
    genrator_obj = onebyone()
    while True:
        print(next(genrator_obj))
except StopIteration:
    print("exhausted !!")
