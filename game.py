def printBoard(board):
	print("   A  B  C")
	count = 1
	for b in board:
		print("{0} {1}".format(count, b))
		count += 1

def checkWin(board):
	for b in board:
		if b[0] == b[1] && b[1] == b[2]:
			return b[0]

	for i in range(2):
		if board[0][i] == board[1][i] && board[1][i] == board[2][i]:
			return board[0][i]

	if board[0][2] == board[1][1] && board[1][1] == board[2][0]:
		return board[0][2]
	elif board[0][0] == board[1][1] && board[1][1] == board[2][2]:
		return board[0][0]
	else:
		return 0.5

def updatePosition(board, pos, value):
	x, y = pos.split()

	x = x.replace("A", "0")
	x = x.replace("B", "1")
	x = x.replace("C", "2")

	board[int(y)-1][int(x)] = value

	return board


players = [1, 2]

board = [
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
		]



printBoard(board)
board = updatePosition(board, "B 2", 4)
printBoard(board)