import random

# def generateUniqueString(string, length, currentSet):
#     notUnique = True
#     while notUnique:
#         unusedLetters = list(string)
#         subset = ""
#         while len(subset) < length:
#             randomLetter = string[random.randint(0, len(string))-1]
#             if randomLetter in unusedLetters:
#                 subset += randomLetter
#                 unusedLetters.remove(randomLetter)
#         if subset not in currentSet:
#             return subset
#
# def subset(string):
#     subsets = []
#     for i in range(len(string)):
#         currentSet = []
#         while (len(currentSet) < 2**i):
#             if randomLetter in unusedLetters:
#                 subset += randomLetter
#                 unusedLetters.append(randomLetter)
#             subsets.append(subset)
#     return subsets

# def subsets(string):
#     for i in range(len(string)):
#         for j in range(len(string)):
#             if i<j:
#                 print(string[i:j+1])

from itertools import permutations


def main():
    # string = "aba"
    # print(subsets(string))
    #print(subset(string))
    perms = [''.join(p) for p in permutations('stack')]
    print(perms)

main()
