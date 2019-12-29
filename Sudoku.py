import time
from Unsorted import *






    #W
def main(sudoku):
    while True:
        command = input("What to do: ").lower()
        command = command.split(" ")

        if command[0] == "solve":

            print()

        elif command[0] == "print" and command[1] == "all":
            print()

        elif command[0] == "add":
            addToDatabase()

        elif command[0] == "help":
            print()
        elif command[0] == "c":
            break
        else:
            print("Sorry, didn't get that, try again")

    printSudoku(sudoku)
    sudoku = solve(sudoku)
    if not sudokuLegal(sudoku):
        print("Sudoku is not legal!")


def addToDatabase():
    title = input("Title: ")
    description = input("Description: ")
    print("Enter each row as a series of 9 digits where '0' is an empty cell:")
    writtenSudoku = []
    for row in range(9):
        line = input(f"row{row+1}: ")
        writtenSudoku += [line]
    f = open("database.txt", "a")
    f.write(f"Title: {title}\nDescription: {description}\n")
    for line in writtenSudoku:
        f.write(line + "\n")
    f.write("\n")
    f.close()

def listSudokusInDatabase():
    f = open("database.txt", "r")
    file = f.read()
    f.close()
    database = file.split("Title: ")
    for number in range(database):
        database[number] = database[number].split("Description: ")

            database[number][1]


def fetchSudokuFromDatabase(sudokuName):
    print(":)")

def databaseToList():
    print(":)")


# Prints the sudoku in a pretty way
def printSudoku(sudoku):
    fulline = "-------------------------\n"
    output = fulline
    for c in range(3):
        for l in range(3):
            for ch in range(3):
                output += "| "
                for lh in range(3):
                    if sudoku[(c)*3+l][(ch)*3+lh] == None:
                        output += "  "
                    else:
                        output += str(sudoku[(c)*3+l][(ch)*3+lh]) + " "
            output += "|\n"
        output += fulline
    print(output[:-1])
    return

def solve(sudoku):
    print(f"Unsolved:")
    printSudoku(sudoku)
    startTime = time.perf_counter()

        # Try to solve sudoku logically
    sudoku = solveLogically(sudoku)
    print(f"Time taken: {(time.perf_counter()-startTime)/1000000000} s. Sudoku after solving logically:")
    printSudoku(sudoku)
    startTime = time.perf_counter()

        # Give up, use brute force
    if not sudokuFilled(sudoku):
        sudoku = guessSolve(sudoku)
        print(f"Time taken : {time.perf_counter()-startTime} s. Sudoku after guessing:")
        printSudoku(sudoku)
    return sudoku

    # Solves the sudoku logiacally as far as it gets and returns it
def solveLogically(sudoku):
    newNumberFound = True
    while newNumberFound:
        #printSudoku(sudoku)
        newNumberFound = False
        for y in range(9):
            yBox = y // 3
            for x in range(9):
                xBox = x // 3
                for v in range(1, 10):
                    if mustBeInThisCell(sudoku, y, x, v, yBox, xBox):
                        sudoku[y][x] = v
                        print(f"{v} in ({x + 1}, {y + 1})")
                        newNumberFound = True
    return sudoku

    # Returns whether the the value v must be in this cell
def mustBeInThisCell(sudoku, y, x, v, yBox, xBox):
    if not sudoku[y][x] and numberCannotBeInOtherCellsInBox(sudoku, y, x, v, yBox, xBox):
        return True
    return False

    # Returns whether v can be in this cell
def legalInThisCell(sudoku, y, x, v, yBox, xBox):
    if not sudoku[y][x] and not numberInBox(sudoku, v, yBox, xBox) and not numberOnRowOrColumn(sudoku, y, x, v):
        return True
    return False


    # Can this number cannot be in another cell in this box?
def numberCannotBeInOtherCellsInBox(sudoku, y, x, v, yBox, xBox):
    if not numberInBox(sudoku, v, yBox, xBox) and not numberOnRowOrColumn(sudoku, y, x, v):
        for yLocal in range(3):
            for xLocal in range(3):
                if (not sudoku[yBox*3 + yLocal][xBox*3 + xLocal]) and (not(yBox*3 + yLocal == y and xBox*3 + xLocal == x)) and (not numberOnRowOrColumn(sudoku, yBox*3 + yLocal, xBox*3 + xLocal, v)):
                    return False
    else:
        return False
    return True


    # Checks if the number v already is in this box
def numberInBox(sudoku, v, yBox, xBox):
    for yLocal in range(3):
        for xLocal in range(3):
            if v == sudoku[yBox*3 + yLocal][xBox*3 + xLocal]:
                return True
    return False


    # Is the number v on this row or column?
def numberOnRowOrColumn(sudoku, y, x, v):
    for axis in range(9):
        if sudoku[y][axis] == v or sudoku[axis][x] == v:
            return True
    return False


    # Checks if the sudoku is filled
def sudokuFilled(sudoku):
    for y in range(9):
        for x in range(9):
            if not sudoku[y][x]:
                print("Sudoku is not finished")
                return False
    print("Sudoku is finished")
    return True


    # Checks if the sudoku is legal
def sudokuLegal(sudoku):
    for y in range(9):
        yBox = y // 3
        for x in range(9):
            xBox = x // 3
            v = sudoku[y][x]
            sudoku[y][x] = None
            if v and numberInBox(sudoku, v, yBox, xBox):
                print(f"Sudoku is illegal because of {v} in box ({yBox}, {xBox})")
                return False
            if v and numberOnRowOrColumn(sudoku, y, x, v):
                print(f"Sudoku is illegal because ({y}, {x})")
                return False
            sudoku[y][x] = v
    print("Sudoku is legal")
    return True


    # Lie in title, just spits out the first sudoku it finds, which is the same evey time. Might fix later
def createRandomSudoku():
    sudoku = [[None for x in range(9)] for y in range(9)]
    changeLog = []
    for y in range(9):
        for x in range(9):
            if not sudoku[y][x]:
                changeLog += [[y, x, 0, [0]]]
    print(sudoku)
    print(changeLog)

    cellNumber = 0
    oneStepBack = False
    while cellNumber < 81:
        y = cellNumber // 9
        yBox = y // 3
        x = cellNumber % 9
        xBox = x // 3

        if oneStepBack:
            sudoku[y][x] = None
            changeLog[cellNumber][3] += [changeLog[cellNumber][2]]
            changeLog[cellNumber][2] = 0
            oneStepBack = False
        noNewNumber = True
        for v in range(1, 10):
            if v not in changeLog[cellNumber][3] and legalInThisCell(sudoku, y, x, v, yBox, xBox):
                sudoku[y][x] = v
                changeLog[cellNumber][2] = v
                cellNumber += 1
                noNewNumber = False
                break
        if noNewNumber:
            sudoku[y][x] = None
            changeLog[cellNumber][2] = 0
            changeLog[cellNumber][3] = [0]
            cellNumber -= 1
            oneStepBack = True
    return sudoku

    # Solves sudoku by brute force
def guessSolve(sudoku):

        # Makes a 82 long list for the changelog, which will keep track of what has been put into the sudoku-list, and which values that already has been tried
    changeLog = []
    for y in range(9):
        for x in range(9):
            if sudoku[y][x]:
                changeLog += [[0, 0, 0, 0, True]]
            else:
                changeLog += [[y, x, 0, [0], False]]
    changeLog += [[0,0,0,0,False]]

    cellNumber = 0
    while changeLog[cellNumber][4]:
        cellNumber += 1
    oneStepBack = False
    while cellNumber < 81:
        #printSudoku(sudoku)
        y = cellNumber // 9
        yBox = y // 3
        x = cellNumber % 9
        xBox = x // 3

        if oneStepBack:
            sudoku[y][x] = None
            changeLog[cellNumber][3] += [changeLog[cellNumber][2]]
            changeLog[cellNumber][2] = 0
            oneStepBack = False
        noNewNumber = True
        for v in range(1, 10):
            if v not in changeLog[cellNumber][3] and legalInThisCell(sudoku, y, x, v, yBox, xBox):
                sudoku[y][x] = v
                changeLog[cellNumber][2] = v
                cellNumber += 1
                while changeLog[cellNumber][4]:
                    cellNumber += 1
                noNewNumber = False
                break
        if noNewNumber:
            sudoku[y][x] = None
            changeLog[cellNumber][2] = 0
            changeLog[cellNumber][3] = [0]
            cellNumber -= 1
            while changeLog[cellNumber][4]:
                cellNumber -= 1
            oneStepBack = True
    return sudoku




main(sudokuUnsolvable28)

#sudoku = guessSolve(sudoku5)
#printSudoku(sudoku)
#sudokuLegal(sudoku)