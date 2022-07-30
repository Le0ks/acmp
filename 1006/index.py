a = input()
b = input()
c = input()
if a == 'black' and b == 'black' and c == 'green':
	print(a, b, c.upper(), sep='\n')
elif a == 'black' and b == 'black' and c == 'GREEN':
	print(a, 'yellow', a, sep='\n')
elif a =='black' and b == 'yellow' and c == 'black':
	print('red', a, a, sep='\n')
elif a == 'red' and b == 'black' and c == 'black':
	print(a, 'yellow', c, sep='\n')
elif a == 'red' and b == 'yellow' and c =='black':
	print(c, c, 'green', sep='\n')
elif a == 'black' and b == 'YELLOW' and c == 'black':
	print(a, b, c, sep='\n')
else:
	print('error')