it=open('input.txt', 'r')
ot=open('output.txt', 'w')
a = list(map(int, it.read().split()))
a = a[1:]
ot.write('{0} {1}'.format(min(a), max(a)))
it.close()
ot.close()