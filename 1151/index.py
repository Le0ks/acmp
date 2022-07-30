n = input()
ans = 0
if len(n) >= 12:
	for i in n:
		if i.isupper():
			ans += 1
			break
	for i in n:
		if i.islower():
			ans += 1
			break
	for i in n:
		if i.isdigit():
			ans += 1
			break
	if ans == 3:
		print('Yes')
	else:
		print('No')
else:
	print('No')