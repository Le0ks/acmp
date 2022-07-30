it=open('input.txt', 'r')
ot=open('output.txt', 'w')
x,y,z=map(int, it.read().split())
pencil=3
pen=5
fl=12
ans = x*pencil+y*pen+z*fl
ot.write(str(ans))
it.close()
ot.close()