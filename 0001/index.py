i = open('input.txt', 'r')
o = open('output.txt', 'w')

a, b = map(int, i.readline().split(' '))
o.write(str(a + b))

i.close()
o.close()