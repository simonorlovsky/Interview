def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

def main():
	print factorial(10)

main()
