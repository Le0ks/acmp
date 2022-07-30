n = int(input())
b = 1
a = c = i = 0
while i < n:
	a = b
	b = c
	c = a + b
	i += 1
print(c)