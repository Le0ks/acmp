it = open('input.txt', 'r')
ot = open('output.txt', 'w')
a,b,c = it.readline().split()
if int(a) >= int(b) and int(a) >= int(c):
	ot.write(str(a))
elif int(b) >= int(a) and int(b) >= int(c):
	ot.write(str(b))
else:
	ot.write(str(c))
it.close()
ot.close()