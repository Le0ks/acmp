k, w = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
if b1 >= k and a1 <= w:
	print('YES')
elif b2 >= k and a2 <= w:
	print('YES')
elif b3 >= k and a3 <= w:
	print('YES')
elif b1 + b2 >= k and a1 + a2 <= w:
	print('YES')
elif b2 + b3 >= k and a2 + a3 <= w:
	print('YES')
elif b1 + b3 >= k and a1 + a3 <= w:
	print('YES')
elif b1 + b2 + b3 >= k and a1 + a2 + a3 <= w:
	print('YES')
else:
	print('NO')