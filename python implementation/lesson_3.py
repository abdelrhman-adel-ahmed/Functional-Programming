import enum

"""
a programming language is said to have first-class functions if it treats functions as first-class
citizens. This means the language supports passing functions as arguments to other functions, 
returning them as the values from other functions, and assigning them to variables or storing them 
in data structures.[1] Some programming language theorists require support for anonymous functions 

references :
 https://en.wikipedia.org/wiki/First-class_function
 https://realpython.com/python-functional-programming/#reducing-an-iterable-to-a-single-value-with-reduce

"""


def Test1(x):
    return x / 2


def Test2(x):
    return (x / 4) + 1


def Test3(funptr, x):
    return funptr(x) + x


test1ptr = Test1
test2ptr = Test2
ptrlist = [test1ptr, test2ptr]

# regular invocation
print(Test2(Test1(5)))
print(Test1(Test2(5)))

# using the delegate (pointer to the entry point of the function) to invoke the func
print(ptrlist[0](5))
print(ptrlist[1](5))

# send function(ptr) to function parameter
print(Test3(Test1, 5))
print(Test3(Test2, 5))

# ------------------------------------------------------------------------------------------


class Order:
    def __init__(self, orderid, productindex, quantity, unitprice):
        self.orderid = orderid
        self.productindex = productindex
        self.quantity = quantity
        self.unitprice = unitprice


class ProductType(enum.Enum):
    Food = 1
    Beverage = 2
    RawMaterial = 3


def ProductParameterFood(productindex):
    return (productindex / (productindex + 100), productindex / (productindex + 300))


def ProductParameterBeverage(productindex):
    return (productindex / (productindex + 300), productindex / (productindex + 400))


def ProductParameterRawMaterial(productindex):
    return (productindex / (productindex + 400), productindex / (productindex + 400))


def calculatediscount(ProductParameterCalc, order):
    parameters = ProductParameterCalc(order.productindex)
    return parameters[0] * order.quantity + parameters[1] * order.unitprice


r = Order(10, 100, 20, 4)
A = ProductParameterFood
B = ProductParameterBeverage
c = ProductParameterRawMaterial

product = ProductType.Food

if product == ProductType.Food:
    P = A
elif product == ProductType.Beverage:
    P = B
else:
    P = C
print(calculatediscount(P, r))
