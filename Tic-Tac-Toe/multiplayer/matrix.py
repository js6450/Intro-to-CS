"""This class is for creating a matrix"""

class Matrix():
#initializing the original grid
    def __init__(self):
        self.matrix = [[" ." for row in range(3)] for column in range(3)]

    def print_matrix(self):
        for r in range(3):
            for c in range(3):
                print(self.matrix[r][c], end = "")
            print()

#checking the matrix for wins of either players and draws and thus when the game
#ends breaks out of the loop and prints thus statement
    def check_matrix(self):
        for row in range(3):
            if self.matrix[row] == [" x", " x", " x"]:
                print("the player1 has won")
                return 1
            elif self.matrix[row] == [" o", " o", " o"]:
                print("the player2 has won")
                return 1
        for c in range(3):
            if self.matrix[0][c]== self.matrix[1][c] == self.matrix[2][c] == " x":
                print("the player1 has won")
                return 1
            elif self.matrix[0][c]== self.matrix[1][c] == self.matrix[2][c] == " o":
                print("the player2 has won")
                return 1
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == " x":
            print("the player1 has won")
            return 1
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == " x":
            print("the player1 has won")
            return 1
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == " o":
            print("the player2 has won")
            return 1
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == " o":
            print("the player2 has won")
            return 1
        for r in range(3):
            for c in range(3):
                if self.matrix[r][c] == " .":
                    return 0
        print("you have a draw")
        return 1
