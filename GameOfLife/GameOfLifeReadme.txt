This program simulates the game of life.
In the game of life, there will be either an organism living or not living in a square within the grid.
If an organism has 2 or 3 neighbours, it survives; other cases, the organism will die either of  loneliness or overcrowdedness.
A vacant cell can generate life if it has exactly 3 neighbours surrounding the square.
The user can input a original state of life consistent of 25 rows and 75 columns of text.
After printing the original state of life, the user will be given a choice whether to see the next generation of life or to abort the program.
Pressing enter will allow the user to see the next stage of life and pressing another key then enter will stop the process.
As the further stages of life are displayed, it will tell the user the number of the generation the program is displaying.
If there are no signs of life on the grid, the program will tell the user that "All life has been terminated."
If the state of life is repeated infinitely, it will tell the user that "This status of life will repeat."


define function print_grid using input grid
	initialize string to an empty string ""
	for r in range 27 as the matrix will consist of 27 rows
		for c in range 77 as the matrix will consist of 77 columns
			continuously add grid[r][c] to value string
		add \n at the end of every column to the value string
	print string

define function upload_grid using input file:
	initialize matrix to file.readlines() to convert the given text into a list consisting of the lines of the text
	close the file
	initialize value grid to a line of list of "." for item in range 77
	for line in matrix
		initialize line to a list of '.' + line without \n every end + '.'
		append the line to the grid
	append the line '.' for item in range 77 to the grid
	return grid

define function neighbour using input grid
	initialize grid_neighbour to an empty list
	for r in range between 1 to 26
		initialize list_neighbour to an empty list
		for c in range 1 to 76
			initialize value to 0
			for row in range between r - 1 and r + 2
				for column in range between c - 1 and c + 2
					if grid[row][column] is equal to "X"
						continuously add on to value
			if grid[r][c] is equal to "X"
				minus on from the value
			append value to list_neighbour
		append list_neighbour to grid_neighbour
	return grid_neighbour

define function new_generation using input neighbour_grid and grid
	initialize new_grid to a line of list of  "." for item in range 77
	for r in range 1 to 26
		initialize list_new_grid to an empty list
		for c in range 1 to 76
			initialize life to 0
			if grid[r][c] is equal to "X"
				if neighbour_grid[r - 1][c - 1] is equal to 3 or is equal to 2
					life is equal to "X"
				else
					life is equal to "."
			else
				if neighbour_grid[r - 1][c - 1] is equal to 3
					life is equal to "X"
				else
					life is equal to "."
			append life to list_new_grid
		append "." + list_new_grid + "." to new_grid
	append "." for item in range 77 to new_grid
	return new_grid

define function check_empty_grid using input grid
	initialize empty to 0
	for r in range 1 to 26
		for c in range 1 to 76
			if grid[r][c] is equal to "X"
				empty is equal to 1
				break
	return empty

define function main
	initialize user_file to input from question to the user "Please enter the file path: "
	initialize file to open user_file as "r"
	initialize grid1 to upload_file of file
	execute print_grid function using input grid1
	initialize generation_number to 0
	while True
		initialize neighbour_grid to function neighbour using input grid1
		initalize grid2 to function new_generation using inputs neighbour_grid and grid1
		continously add 1 on generation_number 
		initialize user to input of the statement "Press enter to see the next generation, or press another key then enter to exit \n"
		if user does not press ""
			break
		if output of function check_empty_grid using input grid2 is equal to 0
			print statement "All life has been terminated."
			break
		if grid1 is equal to grid2
			print statement "This status of life will repeat."
			break
		print statement "Generation:" then generation_number
		execute print_grid function using input grid2
		equal grid1 to grid2

execute function main