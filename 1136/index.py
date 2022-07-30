n = list(map(int, input().split()))
i = 0
max = 0
while n[i] != 0:
	if n[i] > max:
		max = n[i]
	i += 1
print(max)