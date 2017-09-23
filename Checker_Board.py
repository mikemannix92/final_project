board=[]

for i in range(8):
	board.append(["-"]*8)

def grid(insert):
	for i in board:
		print " ".join(i)
print grid(board)

#CPU Pieces

for i in range(0,8,2):
	board[0][i]="x"

for i in range(1,8,2):
	board[1][i]="x"

for i in range(0,8,2):
	board[2][i]="x"

#Human Player Pieces

for i in range(1,8,2):
	board[5][i]="o"

for i in range(0,8,2):
	board[6][i]="o"

for i in range(1,8,2):
	board[7][i]="o"


print grid(board)

#Board is done....For Now......
