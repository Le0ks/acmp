x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x1 == x2 and y1 != 1:
	if y1 == 2 and y1 + 2 == y2 or y1 + 1 == y2:
		print('YES')
	else:
		print('NO')
else:
	print('NO')