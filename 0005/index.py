it = open('input.txt', 'r')
ot = open('output.txt', 'w')
odd = []
even = []
n = list(it.readlines())
t = list(str(n[1]).split(' '))
for i in t:
	if int(i)%2==0:
		odd.append(i)
	else:
		even.append(i)
odd1 = ' '.join(odd)
even1 = ' '.join(even)
if len(odd) >= len(even):
	ot.write(str(even1) + '\n' + str(odd1) + '\n' + 'YES')
elif len(odd) < len(even):
	ot.write(str(even1) + '\n' + str(odd1) + '\n' + 'NO')
