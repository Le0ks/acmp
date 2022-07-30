it = open('input.txt', 'r')
ot = open('output.txt', 'w')
n = int(it.readline())
s = 0
if n>0:
	s = int(((n+1)*n)/2)
elif n<=0:
	s = int(((((abs(n)+1)*n)/2)+1))
ot.write(str(s))
it.close()
ot.close()