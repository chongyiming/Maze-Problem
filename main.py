class Cell:
    #Cell class
    def __init__(self,):
        #initialize possible path, cell on the right and cell above the current cell
        self.possible_path = 0
        self.up = None
        self.right = None
    def __repr__(self):
        return f"{self.possible_path}"

def create_memo(maze_length):
    #create nested array
    memo = []
    for _ in range(maze_length):
        row = [Cell() for _ in range(maze_length)]
        memo.append(row)
    return memo

def printStatement(nested_array):
    for row in nested_array:
        print(row)
    print("")

def top_row_and_right_column_checking(Maze,memo):
    # Top row and most right column checking
    for i in range(len(Maze) - 1):
        if Maze[0][len(Maze) - (i + 1)] != 0 and Maze[0][len(Maze) - (i + 1) - 1] == 1 and memo[0][len(Maze) - (i + 1)].possible_path != 0:
            # check if the right cell and current cell in original maze is road or wall
            # check if possible path of right cell is 0 or 1, only add current cell possible path if right cell's possible path is not 0
            # assign right cell to self.right to allow easier tracking
            memo[0][len(Maze) - (i + 1) - 1].possible_path = 1
            memo[0][len(Maze) - (i + 1) - 1].right = memo[0][len(Maze) - (i + 1)]
        if Maze[i][len(Maze) - 1] != 0 and Maze[i + 1][len(Maze) - 1] == 1 and memo[i][len(Maze) - 1].possible_path != 0:
            # check if the cell above and current cell in original maze is road or wall
            # check if possible path of cell above is 0 or 1, only add current cell possible path if cell above's possible path is not 0
            # assign cell above to self.up to allow easier tracking
            memo[i + 1][len(Maze) - 1].possible_path = 1
            memo[i + 1][len(Maze) - 1].up = memo[i][len(Maze) - 1]

def all_cells_possible_paths_checking(Maze,memo):
    for i in range(len(Maze) - 1):
        for j in range(len(Maze) - 1):
            if Maze[i + 1][len(Maze) - (j + 2)] == 1:
                # check if the right cell and current cell in original maze is road or wall
                # add possible path of right cell to current cell's possible path
                # assign right cell to self.right to allow easier tracking
                if Maze[i + 1][len(Maze) - (j + 2) + 1] != 0:
                    memo[i + 1][len(Maze) - (j + 2)].possible_path += memo[i + 1][len(Maze) - (j + 2) + 1].possible_path
                    memo[i + 1][len(Maze) - (j + 2)].right = memo[i + 1][len(Maze) - (j + 2) + 1]
                # check if the cell above and current cell in original maze is road or wall
                # add possible path of cell above to current cell's possible path
                # assign cell above to self.up to allow easier tracking
                if Maze[i + 1 - 1][len(Maze) - (j + 2)] != 0:
                    memo[i + 1][len(Maze) - (j + 2)].possible_path += memo[i + 1 - 1][len(Maze) - (j + 2)].possible_path
                    memo[i + 1][len(Maze) - (j + 2)].up=memo[i + 1 - 1][len(Maze) - (j + 2)]

def create_path(Maze,memo):
    #make a start point, and assign the bottom left corner cell to current cell
    path = "(Start) -> "
    current_cell = memo[len(Maze) - 1][0]
    while current_cell.possible_path is not None:
        #we will prioritize to go right
        if current_cell.right is not None and current_cell.right.possible_path > 0:
            path += "right -> "
            current_cell = current_cell.right
        #go left if it is None in currentcell.right
        elif current_cell.up is not None and current_cell.up.possible_path > 0:
            path += "up -> "
            current_cell = current_cell.up
        #reach exit or there is no path at all
        else:
            path += "(Exit)"
            break

    #check if there is valid path
    if path == "(Start) -> (Exit)":
        print("No Path")
    else:
        print(path)

    #Since the bottom left corner cell is the starting point and it actually store the number of possible path from starting point to exit
    print("Number of possible path =", memo[len(Maze) - 1][0].possible_path)


if __name__ == "__main__":
    """
    Assume the top right corner is exit and bottom left corner is starting point
    Assume we can only move up or right
    Assume that Maze's width and height has same length
    """

    Maze= [[1,0,1,1,1],
           [1,1,0,0,1],
           [1,0,0,1,0],
           [1,0,0,1,1],
           [1,1,1,1,1]]

    print("Original Maze, 0 represents wall : 1 represents walkable road")
    printStatement(Maze)

    #Create another Maze that allow us to plot out the possible path for the maze
    memo = create_memo(len(Maze))

    #Since the top right corner cell is exit, we will add a possible path for that cell
    if Maze[0][len(Maze) - 1]!=0:
        memo[0][len(Maze) - 1].possible_path = 1

    top_row_and_right_column_checking(Maze,memo)

    print("Find possible path for the top row and most right column")
    printStatement(memo)

    all_cells_possible_paths_checking(Maze,memo)

    print("Each cell stores the possible path if they can go up or right")
    printStatement(memo)

    create_path(Maze,memo)
