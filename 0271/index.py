n = int(input())
a = 0
b = 1
c = 0
i = 0
while c < n:
	a = b
	b = c
	c = a + b
	i += 1
if c == n:
	print(1, i, sep='\n')
else:
	print(0)