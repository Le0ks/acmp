n = list(input())
b = n[0]
a = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,
	'G' : 7,
	'H' : 8
}
ans = int(a.get(b)) + int(n[1])
if ans % 2 == 0:
	print('BLACK')
else:
	print('WHITE')