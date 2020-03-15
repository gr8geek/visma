from math import *
def SecantMethod(function, Value1 , Value2,iterations=1000):
    f = lambda x:eval(function)
    x0 = Value1
    x1 = Value2
    x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    itr=0
    while itr<iterations:
        try:
            x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
            x0 = x1
            x1 = x2
            itr=itr+1
        except:
            return x2

    return x2



