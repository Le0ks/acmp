a, b, c = map(int, input().split())
if a == 0:
	if b == 0:
		if c == 0:
			print(-1)
		else:
			print(0)
	else:
		x = -c / b
		print(1, x, sep='\n')
else:
	d = b**2 - 4 * a * c
	if d < 0:
		print(0)
	elif d == 0:
		x = -b / (a * 2)
		print(1, x, sep='\n')
	else:
		x = (-b - d**0.5) / (a * 2)
		y = (-b + d**0.5) / (a * 2)
		print(2, x, y, sep='\n')