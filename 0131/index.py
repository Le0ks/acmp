n = int(input())
k = -1
m = 0
for i in range(1, n+1):
	v, s = map(int, input().split())
	if s == 1 and v > m:
		m = v
		k = i
print(k)