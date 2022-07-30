l1, w1, h1 = map(int, input().split())
l2, w2, h2 = map(int, input().split())
lc, wc, hc = map(int, input().split())
method1 = max(l1, w2)
method2 = max(w1, l2)
if (l2 + w1) * method1 <= lc * wc and h1 <= hc and h2 <= hc:
	print('YES')
elif (l1 + w2) * method2 <= lc * wc and h1 <= hc and h2 <= hc:
	print('YES')
elif ((l1 <= wc) or (l1 <= lc)) and ((w1 <= lc) or (w1 <= wc)) and h1 + h2 <= hc:
	print('YES')
else:
	print('NO')