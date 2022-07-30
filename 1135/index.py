n = list(map(int, input().split()))
i = 0
even = 0
while n[i] != 0:
	if n[i] % 2 == 0:
		even += 1
	i+=1
print(even)