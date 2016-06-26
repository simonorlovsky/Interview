'''
Fibonacci.py
Implementation of recursive_fib
Author: Simon Orlovsky
Date: 6/10/16
'''
def recursive_fib(n):
	if (n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fib(n-1)+fib(n-2)

def main():
	n = input("Please enter n: ")
	print recursive_fib(n)

main()
