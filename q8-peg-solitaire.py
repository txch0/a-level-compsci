def find(board,choice):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if choice == board[i][j]:
                return i, j

def show(board):
    output = ""
    for i in range(0, len(board)):
        row = ""
        for j in range(0, len(board[i])):
            row += board[i][j]
            row += " "

        output += "{0}\n".format(row)

    print(output)

def saveGame(board):
    save = open("game.txt", "wt")
    save.write("")
    save.close()
    
    save = open("game.txt", "at")
    
    save.write(str(len(board)))
    save.write("\n" + str(len(board[0])))
    for row in board:
        for value in row:
            save.write("\n" + value)

    save.close()

def loadSave():
    board = []
    save = open("game.txt", "rt")
    
    rows = int(save.readline()[0])
    columnSize = int(save.readline()[0])

    board = []
    for i in range(0, rows):
        rowList = []
        for j in range(0, columnSize):
            lineNumber = 2 + i + j
            blankSpace = " "
            rowList.append(save.readline()[0])

        board.append(rowList)

    return board

def generateGrid():
    size_x = int(input("Enter the grid width (2-6): "))
    size_y = int(input("Enter the grid height (2-4): "))
    while not (size_x * size_y >= 4 and size_x * size_y <= 24):
        print("Size out of range. Please try again.")
        size_x = int(input("Enter the grid width (2-6): "))
        size_y = int(input("Enter the grid height (2-4): "))

    board = []
    count = 1
    for i in range(0,size_y):
        row = []
        for j in range(0,size_x):
            character = chr(count + 96)
            if character == "b":
                row.append(blankSpace)
            else:
                row.append(character)
            count += 1

        board.append(row)

    return board

def checkWin(board):
    count = 0
    for row in board:
        for value in row:
            if value != blankSpace:
                count += 1

    return count <= 1
            
            
blankSpace = " "

loadExisting = input("Enter a start mode (load/new)").lower() == "load"

if loadExisting:
    grid = loadSave()
else:
    grid = generateGrid()

while True:
    show(grid)
    choice = input("Enter a letter or save, to save the file: ").lower()

    if choice == "save":
        saveGame(grid)
        break
    
    direction = input("Enter a direction (u,d,l,r): ").lower()
    while direction not in ["u", "d", "l", "r"]:
        print("Not a valid direction.")
        direction = input("Enter a direction (u,d,l,r): ").lower()

    row, column = find(grid, choice)
    
    if direction == "r" and column + 2 < len(grid[0]) and grid[row][column + 2] == blankSpace and grid[row][column + 1] != blankSpace:
        grid[row][column] = blankSpace
        grid[row][column + 1] = blankSpace
        grid[row][column + 2] = choice

        print("moved")

    if direction == "l" and column - 2 >= 0 and grid[row][column - 2] == blankSpace and grid[row][column - 1] != blankSpace:
        grid[row][column] = blankSpace
        grid[row][column - 1] = blankSpace
        grid[row][column - 2] = choice

    if direction == "u" and row - 2 >= 0 and grid[row - 2][column] == blankSpace and grid[row - 1][column] != blankSpace:
        grid[row][column] = blankSpace
        grid[row - 1][column] = blankSpace
        grid[row - 2][column] = choice

    if direction == "d" and row + 2 < len(grid) and grid[row + 2][column] == blankSpace and grid[row + 1][column] != blankSpace:
        grid[row][column] = blankSpace
        grid[row + 1][column] = blankSpace
        grid[row + 2][column] = choice

    if checkWin(grid):
        print("You have won the game, congrats.")
        break
                
input("Press enter to exit.")
