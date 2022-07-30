import math

n, m = map(int, input().split())
if n > m:
	a, b = n, m
	while b > 0:
		a, b = b, a%b
	if a == 1:
		print(min(n, m))
	else:
		print(math.gcd(n, m))
elif n < m:
	a, b = n, m
	while b > 0:
		a, b = b, a%b
	if a == 1:
		print(min(n, m))
	elif :
		print(1)