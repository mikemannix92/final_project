board=[]

for i in range(8):
	board.append(["o"]*8)

#for i in board:
#	print i

def grid(insert):
	for i in board:
		print " ".join(i)
print grid(board)