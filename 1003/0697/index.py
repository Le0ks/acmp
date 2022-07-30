import math
it=open('input.txt', 'r')
ot=open('output.txt', 'w')
a,b,c=map(int, it.read().split())
ans = math.ceil((2*(a*c)+2*(b*c))/16)
ot.write(str(ans))
it.close()
ot.close()