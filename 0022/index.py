it=open('input.txt', 'r')
ot=open('output.txt', 'w')
n=int(it.read())
s=0
while n>0:
	if (n%2)==1:
		s=s+1
	n=int(n/2)
ot.write(str(s))
it.close()
ot.close()