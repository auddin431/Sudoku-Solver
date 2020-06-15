from math import sqrt

# Finds an Empty location on the grid.
def empty(grid, cell):
    x = len(grid)
    for i in range(x):
        for j in range(x):
            if grid[i][j] == 0:
                cell[0], cell[1] = i, j 
                return True
    return False

# Iterates through row, column, and the square the cell is located in to check if the position is valid.
def validCell(grid, row, col, num):
    valid_row = True
    valid_col = True
    valid_square = True
    x = len(grid)
    for j in range(x):
        if grid[row][j] == num:
            valid_row = False
    for i in range(x):
        if grid[i][col] == num:
            valid_col = False
    x = int(sqrt(x))
    for i in range(x):
        for j in range(x):
            if grid[row-row%x+i][col-col%x+j] == num:
                valid_square = False
    if valid_row and valid_col and valid_square:
        return True
    return False


def solver(grid):
    cell = [0,0]
    if not empty(grid, cell):
        return True
    row, col = cell[0], cell[1]
    x = len(grid)
    for num in range(1,x+1):
        if validCell(grid,row,col,num):
            grid[row][col] = num
            if solver(grid):
                return True
            grid[row][col] = 0
    return False

if __name__ == "__main__":

    # Grids to try:
    # grid = [[0,3,4,0],
    #         [4,0,0,2],
    #         [1,0,0,3],
    #         [0,2,1,0]]

    grid = [[3,6,0,0,4,0,2,0,0],
            [0,0,7,0,0,9,3,8,0],
            [0,0,9,0,0,0,6,0,0],
            [1,2,0,0,6,0,7,5,3],
            [9,0,0,1,0,8,4,2,0],
            [0,0,6,5,0,3,0,9,0],
            [7,5,0,0,9,1,0,6,0],
            [0,9,0,0,0,2,0,3,0],
            [8,1,2,0,5,6,9,4,0]]

    if solver(grid):
        for i in grid:
            for j in i:
                print(j, end=" ")
            print("\n")
    else:
        print("No valid solution")