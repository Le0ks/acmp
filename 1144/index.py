n = list(map(int, input().split()))
i = 1
big = 0
bigList = []
k = 0
while n[i] != 0:
	if n[i] > n[i-1] and n[i] > n[i+1] and n[i+1] != 0:
		big = n[i]
	if big > n[i]:
		k += 1
	if big == n[i]:
		bigList.append(big)
		max = 0
	i += 1
bigList.sort()
if bigList:
	print(bigList[-1])
else:
	print(0)