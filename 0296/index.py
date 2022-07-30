n = int(input())
if n%5==0:
	print(n//5, 0)
elif n%5==1:
	print((n-6)//5, 2)
elif n%5==2:
	print((n-12)//5, 4)
elif n%5==3:
	print((n-3)//5, 1)
elif n%5==4:
	print((n-9)//5, 3)