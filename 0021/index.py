it=open('input.txt', 'r')
ot=open('output.txt', 'w')
a,b,c=map(int, it.read().split())
mx=max(a,b,c)
mn=min(a,b,c)
r=mx-mn
ot.write(str(r))
it.close()
ot.close()