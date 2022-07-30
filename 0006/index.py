s = input()
d = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,
	'G' : 7,
	'H' : 8
}
if len(s) == 5 and s[2] == '-' and s.count('-') == 1:
	x1y1, x2y2 = s.split('-')
	if ('A' == x1y1[0] or 'B' == x1y1[0] or 'C' == x1y1[0] or 'D' == x1y1[0] or 'E' == x1y1[0] or 'F' == x1y1[0] or 'G' == x1y1[0] or 'H' == x1y1[0]) and ('A' == x2y2[0] or 'B' == x2y2[0] or 'C' == x2y2[0] or 'D' == x2y2[0] or 'E' == x2y2[0] or 'F' == x2y2[0] or 'G' == x2y2[0] or 'H' == x2y2[0]) and ('1' == x1y1[1] or '2' == x1y1[1] or '3' == x1y1[1] or '4' == x1y1[1] or '5' == x1y1[1] or '6' == x1y1[1] or '7' == x1y1[1] or '8' == x1y1[1]) and ('1' == x2y2[1] or '2' == x2y2[1] or '3' == x2y2[1] or '4' == x2y2[1] or '5' == x2y2[1] or '6' == x2y2[1] or '7' == x2y2[1] or '8' == x2y2[1]):
		x1, y1 = d.get(x1y1[0]), int(x1y1[1])
		x2, y2 = d.get(x2y2[0]), int(x2y2[1])
		if (y1 >= 1 and y1 <= 8) and (y2 >= 1 and y2 <= 8) and (x1 >= 1 and x1 <= 8) and (x2 >= 1 and x2 <= 8):
			if (abs(y1 - y2) == 2 and abs(x1 - x2) == 1) or (abs(y1 - y2) == 1 and abs(x1 - x2) == 2):
				print('YES')
			else:
				print('NO')
		else:
			print('ERROR')
	else:
		print('ERROR')
else:
	print('ERROR')