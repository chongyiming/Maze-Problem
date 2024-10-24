class Cell:
    #Cell class
    def __init__(self,):
        #initialize possible path, cell on the right and cell below the current cell
        self.possible_path = 0
        self.down = None
        self.right = None
        self.finalpath=None
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

def bottom_row_and_right_column_checking(Maze,memo):
    # Bottom row and most right column checking
    for i in range(len(Maze) - 1):
        if Maze[len(Maze) - 1][len(Maze) - (i + 1)] != 0 and Maze[len(Maze) - 1][len(Maze) - (i + 1) - 1] == 1 and memo[len(Maze) -  1][len(Maze) - (i + 1)].possible_path != 0:
            # check if the right cell and current cell in original maze is road or wall
            # check if possible path of right cell is 0 or 1, only add current cell possible path if right cell's possible path is not 0
            # assign right cell to self.right to allow easier tracking
            memo[len(Maze) - 1][len(Maze) - (i + 1) - 1].possible_path = 1
            memo[len(Maze) - 1][len(Maze) - (i + 1) - 1].right = memo[len(Maze) - 1][len(Maze) - (i + 1)]
        if Maze[len(Maze) - (i+1)][len(Maze) - 1] != 0 and Maze[len(Maze) - (i+1)-1][len(Maze) - 1] == 1 and memo[len(Maze) - (i+1)][len(Maze) - 1].possible_path != 0:
            # check if the cell below and current cell in original maze is road or wall
            # check if possible path of cell below is 0 or 1, only add current cell possible path if cell below's possible path is not 0
            # assign cell below to self.down to allow easier tracking
            memo[len(Maze) - (i+2)][len(Maze) - 1].possible_path = 1
            memo[len(Maze) - (i+2)][len(Maze) - 1].down = memo[len(Maze) - (i+1)][len(Maze) - 1]

def all_cells_possible_paths_checking(Maze,memo):
    for i in range(len(Maze) - 1):
        for j in range(len(Maze) - 1):
            if Maze[len(Maze)-(i+2)][len(Maze) - (j + 2)] == 1:
                # check if the right cell and current cell in original maze is road or wall
                # add possible path of right cell to current cell's possible path
                # assign right cell to self.right to allow easier tracking
                if Maze[len(Maze)-(i+2)][len(Maze) - (j + 2) + 1] != 0:
                    memo[len(Maze)-(i+2)][len(Maze) - (j + 2)].possible_path += memo[len(Maze)-(i+2)][len(Maze) - (j + 2) + 1].possible_path
                    memo[len(Maze)-(i+2)][len(Maze) - (j + 2)].right = memo[len(Maze)-(i+2)][len(Maze) - (j + 2) + 1]
                # check if the cell below and current cell in original maze is road or wall
                # add possible path of cell below to current cell's possible path
                # assign cell below to self.down to allow easier tracking
                if Maze[len(Maze) - (i + 1)][len(Maze) - (j + 2)] != 0:
                    memo[len(Maze) - (i + 2)][len(Maze) - (j + 2)].possible_path += memo[len(Maze) - (i + 1)][len(Maze) - (j + 2)].possible_path
                    memo[len(Maze) - (i + 2)][len(Maze) - (j + 2)].down = memo[len(Maze) - (i + 1)][len(Maze) - (j + 2)]

def create_path(Maze,memo):
    #make a start point, and assign the upper left corner cell to current cell
    path = "(Start) -> "
    current_cell = memo[0][0]
    while current_cell.possible_path is not None:
        #we will prioritize to go right
        if current_cell.right is not None and current_cell.right.possible_path > 0:
            path += "right -> "
            current_cell.finalpath=1
            current_cell = current_cell.right
        #go down if it is None in currentcell.right
        elif current_cell.down is not None and current_cell.down.possible_path > 0:
            path += "down -> "
            current_cell.finalpath = 1
            current_cell = current_cell.down
        #reach exit or there is no path at all
        else:
            path += "(Exit)"
            current_cell.finalpath = 1
            break




if __name__ == "__main__":
    """
    Assume the bottom right corner is exit and upper left corner is starting point
    Assume we can only move down or right
    Assume that Maze's width and height has same length
    Assume the input is in nested list
    """

    Maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    #Create another Maze that allow us to plot out the possible path for the maze
    memo = create_memo(len(Maze))

    #Since the bottom right corner cell is exit, we will add a possible path for that cell
    if Maze[len(Maze) - 1][len(Maze) - 1]!=0:
        memo[len(Maze) - 1][len(Maze) - 1].possible_path = 1

    bottom_row_and_right_column_checking(Maze,memo)

    # print("Find possible path for the bottom row and most right column")
    # printStatement(memo)

    all_cells_possible_paths_checking(Maze,memo)

    print("Each cell stores the possible path if they can go down or right")
    printStatement(memo)

    create_path(Maze,memo)

    for row in memo:
        for i in range(len(row)):
            if row[i].finalpath!=1:
                row[i]=0
            else:
                row[i]=1

    print("Final Path")
    printStatement(memo)
