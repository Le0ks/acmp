n = input()
s = 0
m = 0
for i in n:
	if i == '0':
		s += 1
		if s > m:
			m = s
	else:
		s = 0
print(m)