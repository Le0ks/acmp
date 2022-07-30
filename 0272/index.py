n = list(map(int, input().split()))
even = []
odd = []
for i in range(len(n)):
	if (i+1) % 2 == 0:
		even.append(n[i])
	else:
		odd.append(n[i])
print(max(even) + min(odd))