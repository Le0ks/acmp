it = open('input.txt', 'r')
ot = open('output.txt', 'w')
a,b,c = it.readline().split()
if int(a) * int(b) == int(c):
	ot.write('YES')
else:
	ot.write('NO')
it.close()
ot.close()