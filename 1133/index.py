n = list(map(int, input().split()))
i = 0
sum = 0
while n[i] != 0:
	sum += n[i]
	i+=1
print(sum)