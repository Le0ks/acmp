t1r1, t2r1 = map(int, input().split())
t1r2, t2r2 = map(int, input().split())
t1r3, t2r3 = map(int, input().split())
t1r4, t2r4 = map(int, input().split())
a = t1r1 + t1r2 + t1r3 + t1r4
b = t2r1 + t2r2 + t2r3 + t2r4
if a>b:
	print(1)
elif a<b:
	print(2)
else:
	print('DRAW')