it=open('input.txt', 'r')
ot=open('output.txt', 'w')
n=int(it.read())
s=1
for i in range(1, n+1):
	s=s*i
ot.write(str(s))
it.close()
ot.close()