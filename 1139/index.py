n = list(map(int, input().split()))
i = 0
max = 0
count = 0
while n[i] != 0:
	if n[i] > max:
		max = n[i]
		count = 0
	if max == n[i]:
		count += 1
	i += 1
print(count)