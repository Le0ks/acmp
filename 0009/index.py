it = open('input.txt', 'r')
ot = open('output.txt', 'w')
n = it.readlines()
t = list(map(int, str(n[1]).split(' ')))
a = t.index(max(t))
b = t.index(min(t))
if a>b:
	c = t[b+1:a]
elif a<b:
	c = t[a+1:b]
s = 0
k = 1
for i in t:
	if i >= 0:
		s = i + s
for i in c:
	k = i * k
ot.write(str(s)+' '+str(k))
it.close()
ot.close()