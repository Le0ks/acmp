n = int(input())
for i in range(1, n+1):
	n, m = map(int, input().split())
	print(int(19*m + (n + 239)*(n + 366) / 2))
