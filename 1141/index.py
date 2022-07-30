n = list(map(int, input().split()))
i = 0
count = 0
a = n[i]
while n[i]:
	if n[i] == n[i+1] == a:
		a = n[i]
		count += 1
	i += 1
print(sum)