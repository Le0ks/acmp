n = input()
while '4' in n or '7' in n:
	n = n.replace('4', '')
	n = n.replace('7', '')
print(n)