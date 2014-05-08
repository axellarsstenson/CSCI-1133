
from math import sqrt

def fibonacci(n):
    fibList = []
    for i in range(1, n+1):
        fibList +=  [int((1/(sqrt(5))) * ((((1+(sqrt(5)))/2) ** i) - (((1-(sqrt(5)))/2) ** i)))]
    return fibList

print(fibonacci(50))
