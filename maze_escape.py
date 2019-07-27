#!/usr/bin/python

import fileinput

def get_move(board):
	# check right, top, left, bottom

	# check exit
	if board[1][2] == 'e':
		return 'RIGHT'

	if board[0][1] == 'e':
		return 'UP'

	if board[1][0] == 'e':
		return 'LEFT'

	if board[2][1] == 'e':
		return 'DOWN'

	# check paths
	if board[1][2] == '-':
		return 'RIGHT'

	if board[0][1] == '-':
		return 'UP'

	if board[1][0] == '-':
		return 'LEFT'

	if board[2][1] == '-':
		return 'DOWN'


board = []
for i, line in enumerate(fileinput.input()):
    if i > 0:
        board.append(line)

# check bottom
print(get_move(board))