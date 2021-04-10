def add_two_number(a, b):
	return a + b


try:
	s = input()
	a, b = s.split(" ")
	print(add_two_number(int(a), int(b)))
except:
	print("Error")
