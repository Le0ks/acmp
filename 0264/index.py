n = int(input())
a = list(map(int, input().split()))
count = 0
m = 0
for i in a:
	if i > 0:
		count += 1
	else:
		count = 0
	if count > m:
		m = count
print(m)