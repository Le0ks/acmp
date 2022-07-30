x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
	print('YES')
else:
	print('NO')