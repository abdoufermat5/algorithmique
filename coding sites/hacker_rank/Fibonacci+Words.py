def fib_w(A, B, n):
	r = str(A) + str(B)
	print(r)
	while len(r) < n:
		A, B = str(B), r
		r = str(A) + str(B)
		print(r)
	return int(r[n-1])


print(fib_w(1415926535, 8979323846, 35))