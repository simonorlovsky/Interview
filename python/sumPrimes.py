import functools
import operator

def sumPrimes(n):
    lst = range(n)
    for i in range(len(lst)):
        filter(lambda x: x % lst[0] == 0, lst)
sumPrimes(4)
