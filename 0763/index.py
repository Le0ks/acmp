x, y = map(int, input().split())
if x == 1 and y == 1:
	print(0)
elif x != y:
	print(1)
elif x == 1 or y == 1:
	print(1)
elif x == y and x != 1:
	print(2)