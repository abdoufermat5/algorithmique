import sys

# file = sys.argv[-1]
N = int(input())  # number of test

for i in range(N):
	lines = input()
	T, B = list(map(int, lines.split(' ')))
	lines = input()
	prices = list(map(int, lines.split(' ')))
	prices.sort()
	
	s = 0
	k = 0
	for p in prices:
		s += p
		if s <= B:
			k += 1
		else:
			break
	print('Case #{}: {}'.format(i + 1, k))
