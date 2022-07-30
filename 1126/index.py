n = int(input())
if n % 2 == 0:
	print(2)
else:
	a = 3
	while n % a != 0 and a * a <= n:
		a += 2
	if a * a <= n:
		print(a)
	else:
		print(n)