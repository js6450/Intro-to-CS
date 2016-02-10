"""This class is for players."""

class Player():
#whether the player plays "x" or "o" is decided in the main
    def __init__(self, turn):
        self.turn = turn
        self.row = 0
        self.column = 0

#user puts in the row and column of the coordinate that they wish to play
#function puts either "x" or "o" in the desired location if not occupied already
    def user_play(self, matrix):
        while True:
            self.row = int(input("please put in the row of your choice: "))
            self.column = int(input("please put in the column of your choice: "))
            if matrix[self.row - 1][self.column - 1] == " .":
                matrix[self.row - 1][self.column - 1] = self.turn
                return matrix
            print("the cell is already occupied")
