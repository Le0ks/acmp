n = int(input())
a = list(map(int, input().split()))
mx = max(a)
mn = min(a)
for i == range(len(a)):
	if a[i] == mx:
		a[i] = mn
print(*a)