s, p = map(int, input().split())
x = 0
y = 0
exitFlag = False
for i in range(1, s+1):
	x += 1
	for q in range(1, s+1):
		if x + y == s and x * y == p:
			print(x, y)
			exitFlag = True
			break
		y += 1
	if exitFlag:
		break	
	y = 0