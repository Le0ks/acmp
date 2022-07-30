n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
x = int(input())
t = {}
for i in a:
	b = i
	if i == x:
		t.update({0 : x})
		break
	else:
		t.update({abs(b - x) : i})
print(t.get(min(t)))