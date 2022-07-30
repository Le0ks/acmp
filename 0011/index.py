k, n = map(int, input().split())
a = [1]
for i in range(1, n + 1):
	sum_ = 0
	for j in range(1, min(i, k) + 1):
		sum_ += a[i - j]
	a.append(sum_)
print(a[-1])