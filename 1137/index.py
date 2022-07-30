n = list(map(int, input().split()))
i = 1
count = 0
while n[i] != 0:
	if n[i] > n[i-1]:
		count += 1
	i += 1
print(count)