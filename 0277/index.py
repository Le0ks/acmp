a, b, c = map(int, input().split())
if a == b == c == 0:
	print(0)
if a != 0:
	print('{0}'.format(a), end='')
if b != 0:
	if b > 0:
		if a != 0:
			print('+', end='')
		if b == 1:
			print('x', end='')
		else:
			print('{0}x'.format(b), end='')
	elif b < 0:
		if b == -1:
			print('-x', end='')
		else:
			print('{0}x'.format(b), end='')
if c != 0:
	if c > 0:
		if a != 0 or b != 0:
			print('+', end='')
		if c == 1:
			print('y', end='')
		else:
			print('{0}y'.format(c), end='')
	elif c < 0:
		if c == -1:
			print('-y', end='')
		else:
			print('{0}y'.format(c), end='')