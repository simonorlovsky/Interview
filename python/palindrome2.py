def isPalindrome(word):
	isPalindrome = True
	for i in range(len(word)):
		if word[i-1]!=word[-i]:
			isPalindrome = False
	return isPalindrome

def main():
	word = "racecar"
	print isPalindrome(word)
	word2 = "cat"
	print isPalindrome(word2)

main()

