'''
Sort.py
Author: Simon A Orlovsky
Date: 6/10/16

Implementation of bubble sort
'''

#big o of n^2
def bubble(l):
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i] < l[j]:
				l[i], l[j] = l[j], l[i]
	return l

def 


def main():
	l = ['cat', 'dog', 'apple', 'monkey', 'aardvark']
	print bubble(l)

main()
