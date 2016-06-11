#big o of n^2
def bubble(l):
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i] < l[j]:
				l[i], l[j] = l[j], l[i]
	return l


def main():
	l = ['cat', 'dog', 'apple', 'monkey', 'aardvark']
	print bubble(l)

main()
