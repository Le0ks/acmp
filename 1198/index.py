n = int(input())
a, b, c = map(int, input().split())
a1 = 0
b1 = 0
c1 = 0
ans = ''
while a:
	if a1 <= 25:
		ans += chr(65 + a1)
	else:
		a1 = 0
		ans += chr(65 + a1)
	a -= 1
while b:
	if b1 <= 25:
		ans += chr(97 + b1)
	else:
		b1 = 0
		ans += chr(97 + b1)
	b -= 1
while c:
	if c1 <= 9:
		ans += chr(48 + c1)
	else:
		c1 = 0
		ans += chr(48 + c1)
	c -= 1
print(ans)