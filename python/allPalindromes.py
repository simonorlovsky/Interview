#ihaveakayak => kayak
#ihaveakayaktoo
#ihaveakaya
#ihaveakay
#ihaveaka
#ihaveak
#...
#i
#ihaveakayak
#haveakayak

#str = abc
#abc
#ab
#a

#bc
#c

#b

#def longestPalindrome(string):
#     #pop
#     copy = string
#     currentLongest = ""
#     longestCount = 0
#     for i in range(len(string)):
#         if (isPalindrome(copy) and len(copy)>longestCount):
#             currentLongest = copy
#             longestCount = len(copy)
#         lenCopy = len(copy)
#         copy = copy[:lenCopy]

# Runtime ->  O(n^3)

def isPalindrome(string):
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True




def subSet(string):
    subSets = []
    for i in range(len(string)):
        copy = string
        for j in range(len(copy)):
            copy = copy[:(len(copy)-1)]
            subSets.append(copy)
        string = string[1:]
    return subSets

sub = subSet("ihaveakayaktoo")
#max(mylist, key=len)
palindromes = list(filter(isPalindrome, sub))
print(max(palindromes, key=len))
