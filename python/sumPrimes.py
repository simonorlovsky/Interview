import functools
import operator


def sumPrimes(n):
    lst = range(1, n)
    notPrime = []
    for i in range(len(lst)): 
        for j in range(len(lst)):
            if lst[i] % lst[j] == 0 and lst[i] != lst[j] and lst[j] != 1:
                notPrime.append(lst[i])
    for i in range(len(notPrime)):
        if notPrime[i] in lst:
            lst.remove(notPrime[i])
    return functools.reduce(operator.add, lst)

print(sumPrimes(10))
