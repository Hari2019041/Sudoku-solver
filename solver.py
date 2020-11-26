def check_sudoku(row, column, number, grid):
	for i in range(9):
		if grid[row][i] == number:
			return False
		if grid[i][column] == number:
			return False

	row = row - row%3 
	column = column - column%3

	for i in range(row, row+3):
		for j in range(column, column+3):
			if grid[i][j] == number:
				return False
	return True

def find_next_empty_square(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				return (i, j)
	
	return (-1, -1) 

def solve_sudoku(grid):
	row, column = find_next_empty_square(grid)

	if (row, column) == (-1, -1):
		printSolution(grid)
		return

	for i in range(1, 10):
		if check_sudoku(row, column, i, grid):
			grid[row][column] = i
			if solve_sudoku(grid):
				return True
			grid[row][column] = 0

	return False

def printSolution(grid):
	for row in grid:
		print(*row)

grid = [[0, 0, 4, 7, 0, 6, 3, 0, 0],
		[0, 9, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 5, 0, 0, 1, 2, 8, 0],
		[0, 0, 0, 8, 0, 7, 0, 6, 3],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[5, 6, 0, 3, 0, 2, 0, 0, 0],
		[0, 3, 7, 1, 0, 0, 5, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 0],
		[0, 0, 9, 6, 0, 8, 7, 0, 0],
		]

solve_sudoku(grid)

