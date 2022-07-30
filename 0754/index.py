m1, m2, m3 = map(int, input().split())
if (m1>=94 and m1<=727) and (m2>=94 and m2<=727) and (m3>=94 and m3<=727):
	print(max(m1, m2, m3))
else:
	print('Error')