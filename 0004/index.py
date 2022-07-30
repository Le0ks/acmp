it = open('input.txt', 'r')
ot = open('output.txt', 'w')
n = int(it.readline())
s = 9 - n
a = str(n) + str(9) + str(s)
ot.write(a)
it.close()
ot.close()