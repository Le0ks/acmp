it = open('input.txt', 'r')
ot = open('output.txt', 'w')
n = int(it.readline())
k = n % 10
if n < 4**10 and k == 5:
	s = n ** 2
	ot.write(str(s))
it.close()
ot.close()