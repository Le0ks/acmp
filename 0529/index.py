x1, y1, x2, y2 = map(int, input().split())
ans = ((abs(x1 - x2))**2 + (abs(y1 - y2)**2))**0.5
if ans % 1 == 0:
	print(int(ans))
else:
	print(ans)