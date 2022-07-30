k = int(input())
while k:
	a = list(input().split())
	print(' '.join(a[::-1]))
	k -= 1