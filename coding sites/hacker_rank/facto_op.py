def factorial(n):
	if n < 0:
		return 0
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)
	
	
def f(n):
	r = sum([factorial(int(i)) for i in str(n)])
	return r


def sf(n):
	a = f(n)
	r = sum([int(i) for i in str(a)])
	return r


def g(i):
	n = 0
	while sf(n) != i:
		n += 1
	return n


def sg(i):
	a = g(i)
	r = sum([int(i) for i in str(a)])
	return r


def sum_sg(n):
	r = sum([sg(i) for i in range(1, n+1)])
	return r+1
