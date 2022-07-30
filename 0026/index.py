x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
interval = (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5
if r1 + r2 >= interval and interval + r2 >= r1 and interval + r1 >= r2:
	print('YES')
else:
	print('NO')