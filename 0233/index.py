n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(0, n):
	k += 1
	if a[i] <= 437:
		print('Crash {0}'.format(k))
		break
else:
	print('No crash')