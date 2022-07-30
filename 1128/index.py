x, y = map(float, input().split())
day = 1
while x < y:
	x = x+x*0.15
	day += 1
print(day)