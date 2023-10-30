from functools import reduce
def function1(k, n):
	progeny = 2**k
	n -= 1
	return 1 - prob(n, 0.25, progeny)

def fact(n): 
	if n < 2: return 1
	return reduce(lambda x, y: x*y, range(2, int(n)+1))

def prob(y, p, n):
	x = 1.0 - p

	a = n - y
	b = y + 1

	c = a + b - 1

	prob = 0

	for j in range(a, c + 1):
		prob += fact(c) / (fact(j)*fact(c-j)) \
				* x**j * (1 - x)**(c-j)

	return prob

# Test
print(function1(5,8))

