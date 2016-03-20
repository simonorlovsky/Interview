def palidrome(string):
    isPalindrome = True
    for i in range(len(string)/2):
        if (string[i]!=string[-i-1]):
            isPalindrome = False
    return isPalindrome



def main():
    print palidrome("racecar")
main()
