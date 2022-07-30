s = input()
ans = ''
for i in s:
	if ord(i) == 90:
		ans += chr(65)
		continue
	if ord(i) == 122:
		ans += chr(97)
		continue
	ans += chr(ord(i)+1)
print(ans)