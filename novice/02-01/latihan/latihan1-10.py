def call(x, f):
    return f(x)

square = lambda x : x*x

increment = lambda x : x+1

cube = lambda x : x*x*x

decrement = lambda x : x-1

funcs = [square, increment, cube, decrement]

from functools import reduce 
print(reduce(call, funcs, 2)) 