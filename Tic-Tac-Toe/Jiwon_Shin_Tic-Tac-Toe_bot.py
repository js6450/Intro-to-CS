#this is intro to computer science assignment for creating a tic-tac-toe

import random

#defining function to print the matrix in rows and columns
def print_matrix(matrix):
    for r in range(3):
        for c in range(3):
            print(matrix[r][c], end = "")
        print()

#function for a way to allow user to input at a location they desire
def user_play(matrix):
    while True:
        coordinates_r = int(input("please put in the row of your choice: "))
        coordinates_c = int(input("please put in the column of your choice: "))
        #checking if the location is already occupied
        if matrix[coordinates_r - 1][coordinates_c - 1] == " .":
            matrix[coordinates_r - 1][coordinates_c - 1] = " x"
            return matrix
        print("the cell is already occupied")
            
#function for the computer to randomly play the game    
def computer_play(matrix):
    x = 0
    y = 0
    #computer randomly chooses a box to play provided that it is not occupied
    while matrix[x][y] != " .":
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    matrix[x][y] = " o"

#function to check if there is a winner or a loser and if so, who is that winner
#/loser
def check(matrix):
    #Checking for horizontal winners
    for row in range(3):
        if matrix[row] == [" x", " x", " x"]:
            return 1
        elif matrix[row] == [" o", " o", " o"]:
            return 2
    #checking for vertical winners
    for column in range(3):
        if matrix[0][column]== matrix[1][column] == matrix[2][column] == " x":
            return 1
        elif matrix[0][column]== matrix[1][column] == matrix[2][column] == " o":
            return 2
    #checking for diagonal winners
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == " x":
        return 1
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == " x":
        return 1
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == " o":
        return 2
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == " o":
        return 2
    else:
        return

#main function to structure the program 
def main():
    #creating an empty matrix of 3x3
    matrix = [[" ." for row in range(3)] for column in range(3)]
    while True:
        print_matrix(matrix)
        user_play(matrix)    
        computer_play(matrix)
        #break out of the loop once the winner has been declared
        if check(matrix) == 1:
            print("the user has won")
            break
        elif check(matrix) == 2:
            print("the computer has won")
            break

main()
