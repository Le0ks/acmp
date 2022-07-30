letters = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,
	'G' : 7,
	'H' : 8
}
move1, move2 = map(list, input().split())
l1 = move1[0]
l2 = move2[0]
x1 = letters.get(l1)
y1 = int(move1[1])
x2 = letters.get(l2)
y2 = int(move2[1])
k = 0
if x1 == x2 or y1 == y2:
	print('Rook')
	k += 1
if abs(x1 - x2) == abs(y1 - y2):
	print('Bishop')
	k += 1
if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
	print('Knight')
	k += 1
if (x1 == x2 or y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
	print('Queen')
	k += 1
if (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2 ) == 1 and x1 == x2) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
	print('King')
	k += 1
if x1 == x2 and y1 != 1:
	if y1 == 2 and y1 + 2 == y2 or y1 + 1 == y2:
		print('Pawn')
		k += 1
if k == 0:
	print('Nobody')