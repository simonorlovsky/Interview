'''
Algorithm
1. Generate all combinations of list put together
2. See if str is in that list of combinations
'''

def catdog(str, lst):
    combinations = []
    currentStr = ""
    for i in range(len(lst)):
        currentStr += lst[i]
        combinations.append(currentStr)
    return combinations

lst = ["cat", "dog", "man"]
print(catdog("simon", lst))
