x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if abs(x1 - x2) == 1 or abs(y1 -  y2) == 1:
	print('YES')
else:
	print('NO')