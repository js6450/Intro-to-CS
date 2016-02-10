from matrix import *
from player import *

def main():
#assigning class objects
    matrix1 = Matrix()
    player1 = Player(" x")
    player2 = Player(" o")
#repeating the loop of print matrix, user play and check if the user play has
#resulted in any wins or draws
    while True:
        matrix1.print_matrix()
        matrix1.matrix = player1.user_play(matrix1.matrix)
        if matrix1.check_matrix() == 1: break 
        matrix1.print_matrix()
        matrix1.matrix = player2.user_play(matrix1.matrix)
        if matrix1.check_matrix() == 1: break
        
main()
