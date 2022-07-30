from math import gcd

i, j = map(int, input().split())
i, j = max(i, j), min(i, j)
f0 = 0
f1 = 1
for z in range(1, i + 1):
	if z == j:
		fj = f1
	if z == i:
		fi = f1
	f0, f1 = f1, f0 + f1
print(gcd(fi, fj) % 10 ** 9)