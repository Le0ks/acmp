def area(x1, y1, x2, y2, x3, y3):
	a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
	b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
	c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
	p = (a + b + c) / 2
	area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	if area % 1 == 0:
		return int((p * (p - a) * (p - b) * (p - c)) ** 0.5)
	else:
		return (p * (p - a) * (p - b) * (p - c)) ** 0.5
x1, y1, x2, y2, x3, y3 = map(int, input().split())
print(area(x1, y1, x2, y2, x3, y3))