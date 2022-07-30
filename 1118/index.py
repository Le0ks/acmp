a,b,c=input().split()
n=0
r=0
while n<int(a)-int(b):
    n=n+int(b)-int(c)
    r=r+1
print(r+1)