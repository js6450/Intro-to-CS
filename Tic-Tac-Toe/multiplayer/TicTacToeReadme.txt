This program allows 2 players to play a game of tic-tac-toe.
Users will be asked to put in first the number of row then the number of column to place their turn (either "x" or "o") in the grid.
Everytime a turn is placed, the program will check whether there is a winner or a draw is created.

from matrix import *
from player import *

define function main
	matrix1 is object of class Matrix
	player1 is object of class Player
	player2 is object of class Player
	while True
		print_matrix of matrix1
		matrix1 is equal to user_play of player1
		if check_matrix of matrix1 is equal to 1, break
		print_matrix of matrix1
		matrix1 is equal to user_play of player2
		if check_matrix if matrix1 is equal to 1, break
execute main function