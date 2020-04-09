import sys

"""
uses backtracking algorithm to place queens in 
the correct positions on the n x n board
returns the input board after updating 
"""
def placeQueens(n, board, v):
	queenIndexes = []
	index = []
	numQI = 0 #both iterator for index column and loop
	while numQI < n :
		#print if verbose
		if v:
			printBoard(board)

		#try to find a spot to put queen in
		found = False
		for i in range(n):
			if board[i][numQI] == '-':
				board[i][numQI] = 'Q'
				index = [i,numQI]
				queenIndexes.append(index)
				found = True
				break

		#if found, increment numQI and forward check
		if found:
			board = forwardCheck(board, index, numQI, n)
			numQI = numQI + 1
			continue

		#if not found:
		#backtrack to most recent assignment in column
		if ~found:
			highest = 0
			for i in range(n):
				if board[i][numQI] != '-' and board[i][numQI] != 'x':
					if int(board[i][numQI]) > highest:
						highest = int(board[i][numQI])
			for i in range(numQI-highest):
				queenIndexes.pop()
			numQI = highest
			backTrack(board, highest, n)

	return board

"""
takes in a board and an index value
returns the board with the indices that the new
index excludes
"""
def forwardCheck(board, index, numQI, n):
	#assigning forward
	tempx = index[0]
	tempy = index[1] + 1
	while onBoard([tempx, tempy], n):
		if board[tempx][tempy] == '-' or board[tempx][tempy] == 'x':
			board[tempx][tempy] = numQI
		tempy = tempy + 1

	#assigning up
	tempx = index[0] - 1
	tempy = index[1] + 1
	while onBoard([tempx, tempy], n):
		if board[tempx][tempy] == '-' or board[tempx][tempy] == 'x':
			board[tempx][tempy] = numQI
		tempy = tempy + 1
		tempx = tempx - 1
	#assigning down
	tempx = index[0] + 1
	tempy = index[1] + 1
	while onBoard([tempx, tempy], n):
		if board[tempx][tempy] == '-' or board[tempx][tempy] == 'x':
			board[tempx][tempy] = numQI
		tempy = tempy + 1
		tempx = tempx + 1
	return board

"""
backtracks the board to the xth
step of the program, then returns it
"""
def backTrack(board, x, n):
	for i in range(n):
		if board[i][x] == 'Q':
			board[i][x] = 'x'
	for i in range(n):
		for j in range(x+1,n):
			if board[i][j] != '-':
				if board[i][j] == 'Q' or board[i][j] == 'x':
					board[i][j] = '-'
				elif int(board[i][j]) >= x:
					board[i][j] = '-'
	return board

"""
takes in an index and n
outputs if the index is on the board
"""
def onBoard(index, n):
	if index[0] >= n or index[0] < 0:
		return False
	if index[1] >= n or index[1] < 0:
		return False
	return True

"""
takes in a board and outputs
"""
def printBoard(board):
	print(len(board), " by ", len(board), ": ")
	for i in range(len(board)):
		for j in range(len(board[0])):
			print(board[i][j], end=' ')
		print()
	print()

def printFinalBoard(board):
	print(len(board), " by ", len(board), ": ")
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != 'Q':
				print('-', end=' ')
			else:
				print('Q', end=' ')
		print()
	print()

def main():
	#grab number of queens
	n = int(sys.argv[1])

	#deciding whether output is ~verbose~ or not
	v = False
	if len(sys.argv) > 2:
		v = True

	#generate board 
	board = [['-' for _ in range(n)] for _ in range(n)]

	#run the algorithm
	board = placeQueens(n, board, v)

	#print the correct answer :)
	print("Final:")
	printFinalBoard(board)

if __name__ == '__main__':
	main()
