import math

it = open('input.txt','r')
ot = open('output.txt','w')
a,b=map(int, it.read().split())
n=math.gcd(a,b)
k=int(a*b/n)
ot.write(str(k))
it.close()
ot.close()