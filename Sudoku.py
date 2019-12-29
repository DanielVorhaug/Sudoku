import time


# A couple of functions and some code i might use again later IDK
def findLastPlaceInBox(sudoku, yBox, xBox):
    unFilledCells = []
    valuesLeft = [1,2,3,4,5,6,7,8,9]
    for yLocal in range(3):
        for xLocal in range(3):
            if not sudoku[yBox*3 + yLocal][xBox*3 + xLocal]:
                unFilledCells.append([yBox*3 + yLocal, xBox*3 + xLocal])
            else:
                valuesLeft.remove(sudoku[yBox*3 + yLocal][xBox*3 + xLocal])
            if len(unFilledCells) > 1:
                return [False]
    if len(valuesLeft) == 1:
        return [True, unFilledCells[0][0], unFilledCells[0][1], valuesLeft[0]]
    else:
        return [False]
def legalIsLastPlaceInBox(sudoku, y, x, v, yBox, xBox):
    valuesLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for yLocal in range(3):
        for xLocal in range(3):
            if not sudoku[yBox * 3 + yLocal][xBox * 3 + xLocal]:
                if not(y == yBox * 3 + yLocal and x == xBox * 3 + xLocal):
                    return False
            else:
                valuesLeft.remove(sudoku[yBox * 3 + yLocal][xBox * 3 + xLocal])
    if len(valuesLeft) == 1 and valuesLeft[0] == v:
        return True
    else:
        return False
            # Checks for boxs with only one clear cell, puts in correct number
        #for yBox in range(3):
         #   for xBox in range(3):
          #      lastInBoxInfo = findLastPlaceInBox(sudoku, yBox, xBox)
           #     if lastInBoxInfo[0]:
            #        sudoku[lastInBoxInfo[1]][lastInBoxInfo[2]] = lastInBoxInfo[3]
             #       newNumberFound = True
              #      print(f"Last box: {lastInBoxInfo[3]} in ({lastInBoxInfo[2]+1}, {lastInBoxInfo[1]+1}")
               #     #printSudoku(sudoku)


    # Sudokus are on the format of a 9x9 list, where None is an unfilled cell

# empty
sudoku0 = [[None for x in range(9)] for y in range(9)]

# easy
sudokuEasy1 = [
    [3,8,None,None,4,None,2,9,None],
    [None,4,None,9,1,7,3,8,None],
    [None,None,9,None,None,None,None,4,None],
    [2,None,None,None,None,9,None,7,None],
    [None,None,None,8,3,4,None,None,None],
    [None,1,None,7,None,None,None,None,8],
    [None,7,None,None,None,None,6,None,None],
    [None,3,4,6,8,1,None,2,None],
    [None,2,6,None,7,None,None,3,9]    
    ]

# easy, first box almost solved
sudokuEasyFirstBox2 = [
    [3,8,1,None,4,None,2,9,None],
    [5,4,2,9,1,7,3,8,None],
    [7,None,9,None,None,None,None,4,None],
    [2,None,None,None,None,9,None,7,None],
    [None,None,None,8,3,4,None,None,None],
    [None,1,None,7,None,None,None,None,8],
    [None,7,None,None,None,None,6,None,None],
    [None,3,4,6,8,1,None,2,None],
    [None,2,6,None,7,None,None,3,9]
    ]

# medium
sudokuMedium1 = [
    [None, None, None, 5, None, None, None, None, None],
    [None, 4, None, None, 7, None, 6, 5, None],
    [None, 6, None, 8, 1, None, None, None, 2],

    [None, None, 4, 9, None, None, 8, 7, None],
    [6, None, None, None, None, None, None, None, 4],
    [None, 5, 9, None, None, 8, 2, None, None],

    [9, None, None, None, 5, 3, None, 4, None],
    [None, 7, 2, None, 9, None, None, 3, None],
    [None, None, None, None, None, 7, None, None, None]
]

# very hard difficult
sudokuVeryHard1 = [
    [None,8,None,6,None,None,None,None,None],
    [9,4,None,7,None,None,None,None,None],
    [None,None,5,4,3,None,9,None,6],
    [None,None,None,None,None,None,8,None,None],
    [1,7,None,None,None,None,None,5,4],
    [None,None,9,None,None,None,None,None,None],
    [6,None,3,None,8,7,5,None,None],
    [None,None,None,None,None,4,None,1,8],
    [None,None,None,None,None,6,None,9,None]
]

# only 17 clues
sudoku17Clues = [
    [None,None,None,8,None,1,None,None,None],
    [None,None,None,None,None,None,4,3,None],
    [5,None,None,None,None,None,None,None,None],
    [None,None,None,None,7,None,8,None,None],
    [None,None,None,None,None,None,1,None,None],
    [None,2,None,None,3,None,None,None,None],
    [6,None,None,None,None,None,None,7,5],
    [None,None,3,4,None,None,None,None,None],
    [None,None,None,2,None,None,6,None,None]
]

# Arto Inkalas Escargot
sudokuEscargot = [
    [1,None,None,None,None,7,None,9,None],
    [None,3,None,None,2,None,None,None,8],
    [None,None,9,6,None,None,5,None,None],
    [None,None,5,3,None,None,9,None,None],
    [None,1,None,None,8,None,None,None,2],
    [6,None,None,None,None,4,None,None,None],
    [3,None,None,None,None,None,None,1,None],
    [None,4,None,None,None,None,None,None,7],
    [None,None,7,None,None,None,3,None,None]

]

# Arto Inkalas "Worlds hardest sudoku" https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
sudokuWorldsHardest = [
    [8,None,None,None,None,None,None,None,None],
    [None,None,3,6,None,None,None,None,None],
    [None,7,None,None,9,None,2,None,None],
    [None,5,None,None,None,7,None,None,None],
    [None,None,None,None,4,5,7,None,None],
    [None,None,None,1,None,None,None,3,None],
    [None,None,1,None,None,None,None,6,8],
    [None,None,8,5,None,None,None,1,None],
    [None,9,None,None,None,None,4,None,None]
]

# Unsolvable #28 https://sudokuwiki.org/Weekly_Sudoku.asp?puz=28
sudokuUnsolvable28 = [
    [6,None,None,None,None,8,9,4,None],
    [9,None,None,None,None,6,1,None,None],
    [None,7,None,None,4,None,None,None,None],
    [2,None,None,6,1,None,None,None,None],
    [None,None,None,None,None,None,2,None,None],
    [None,8,9,None,None,2,None,None,None],
    [None,None,None,None,6,None,None,None,5],
    [None,None,None,None,None,None,None,3,None],
    [8,None,None,None,None,1,6,None,None]
]


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

    #
def main(sudoku):
    printSudoku(sudoku)
    sudoku = solve(sudoku)
    if not sudokuLegal(sudoku):
        print("Sudoku is not legal!")

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




main(sudokuWorldsHardest)

#sudoku = guessSolve(sudoku5)
#printSudoku(sudoku)
#sudokuLegal(sudoku)