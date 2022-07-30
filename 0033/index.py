it=open('input.txt', 'r')
ot=open('output.txt', 'w')
a,b=map(int, it.read().split())
c=a+b
n=c-a-1
k=c-b-1
ot.write(str(n) + ' ' + str(k))
it.close()
ot.close()