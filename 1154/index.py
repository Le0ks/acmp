n = input()
z = list(n.split('.'))
if n.count('.') == 3 and '' not in z:
	a, b, c, d = map(int, n.split('.'))
	if (a >= 0 and a <= 255) and (b >= 0 and b <= 255) and (c >= 0 and c <= 255) and (d >= 0 and d <= 255) and n.count('..') == 0:
		print('Good')
	else:
		print('Bad')
else:
	print('Bad')