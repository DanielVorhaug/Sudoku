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