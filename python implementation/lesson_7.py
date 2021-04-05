"""
i recommend to read those articles in order to gain more deep understanding of closures
1-https://en.wikipedia.org/wiki/Closure_(computer_programming)
2-https://en.wikipedia.org/wiki/Funarg_problem
3-https://medium.com/@5066aman/lexical-environment-the-hidden-part-to-understand-closures-71d60efac0e0
4-https://www.youtube.com/watch?v=HcW5-P2SNec
5-You Don't Know JS: Scope & Closures Book by Kyle Simpson
"""

# note:The example of the lecture has already been written by MuhammadMotawe
# link : https://github.com/MuhammadMotawe/FunctionalProgramming/blob/main/Closures/Python/Closures.py
# note: its not recomended to use OrderedDict with large data due to overhead complexity of using doubly linked list


def outer(x):
    x1 = x + 10

    def inner(a):
        return a + x1

    return inner


out1 = outer(10)
print(out1(4))
# --------------------------------------------------------------------------

# use the clouser to decorate another function
def decorator_fun(original_fn):
    def wrapper_fun():
        print(f"decorated the function {original_fn}")
        return original_fn()

    return wrapper_fun


def display():
    print("decorated fucntion is hereee ")


out2 = decorator_fun(display)()
# --------------------------------------------------------------------------

# using @ to directly calling the decorated function
def decorator_fun1(original_fn):
    def wrapper_fun(*args, **kwargs):
        print(f"decorated the function value get passed to wrapper is {args[0]}")
        return original_fn(*args, **kwargs)

    return wrapper_fun


@decorator_fun1
def display1(x):
    print("decorated fucntion is hereee ")


out3 = display1
out3(12)

# --------------------------------------------------------------------------
