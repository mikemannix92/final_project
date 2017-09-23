board=[]

for i in range(8):
	board.append(["o"]*8)

def grid(insert):
	for i in board:
		print " ".join(i)
print grid(board)

#How to include the player pieces???