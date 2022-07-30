x, p, y = map(int, input().split())
year = 0
while x < y:
	x *= 1 + p / 100
	x = int(100 * x) / 100
	year += 1
print(year)