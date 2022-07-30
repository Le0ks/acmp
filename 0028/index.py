x1, y1, x2, y2 = map(int, input().split())
x_a, y_a = map(int, input().split())
if x1 == x2:
	print(x1 + (x1 - x_a), y_a)
elif y1 == y2:
	print(x_a, y1 + (y1 - y_a))
