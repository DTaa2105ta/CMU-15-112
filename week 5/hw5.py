#################################################
# hw5.py
# name: Dtaa
# andrew id: 
#################################################

import cs112_s22_week5_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Part A
#################################################
"""
!!! all your functions must be non-destructive 
unless the problem specifically indicates otherwise.
"""

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    ans = list()
    rowAns = 0
    for rowA in range(len(A)):
        if rowA != row:
            ans += [0]
            if ans != [0]:
                rowAns += 1
            rowToAdd = [(element) for element in A[rowA]]
            ans[rowAns] = rowToAdd
    
    if ans == [ ]: return ans 

    for rowAfterRemoveRow in range(len(ans)):
        for colA in range(len(A[0])):
            if colA == col:
                ans[rowAfterRemoveRow].pop(colA)
    return ans

def destructiveRemoveRowAndCol(A, row, col):
    """
    assume that row and col are both legal values 
    (that is, they are non-negative integers 
    that are smaller than the number of rows and columns, respectively)
    """
    for rowA in range(len(A)):
        if rowA == row:
            A.pop(rowA)
    
    if A == []:
        return 
    
    for rowAfterRemoveRow in range(len(A)):
        for colA in range(len(A[0])):
            if colA == col:
                A[rowAfterRemoveRow].pop(colA)

def sumOverRowAndColumn(m1, m2, rowM1, colM2):
    ans = 0
    rowM2 = 0
    for colElement in m1[rowM1]:
        ans += colElement * m2[rowM2][colM2]
        rowM2 += 1
    return ans

def matrixMultiply(m1,m2):
    if len(m1[0]) != len(m2):
        return 
    ans = [ ]
    for row in range(len(m1)):
        rowAns = [ ]
        for col in range(len(m2[0])):
            rowAns.append(sumOverRowAndColumn(m1, m2, row, col))
        ans.append(rowAns)
    return ans
#################################################
def makeNoneRow(colLen):
    return [None] * (colLen + 2)

def makeFullBoard(board):
    ans = [ ]
    rowLen = len(board)
    colLen = len(board[0])
    for row in range(rowLen):
        rowToAns = board[row].copy()
        ans.append([None] + rowToAns + [None])
    noneRow1 = [makeNoneRow(colLen)]
    noneRow2 = [makeNoneRow(colLen)]
    return noneRow1 + ans + noneRow2

def makeCheckedList(board):
    ans = [ ]
    colLen = len(board[0])
    for _ in range(len(board)):
        rowToAdd = [0] * colLen
        ans.append(rowToAdd)
    return ans
def find1(board):
    #find position of 1
    flag = False
    rowOf1, colOf1 = None, None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return 
            elif board[row][col] == 1:
                if not flag:
                    flag = True
                    rowOf1, colOf1 = row, col
                elif flag:
                    return
    return rowOf1, colOf1

def check(element1, element2):
    if element2 == None:
        return False
    return element2 - element1 == 1

def findNextmove(point, rowP, colP, newBoard, checkedList):
    rowP += 1 # in full board with "None"s, increase current row, 
    colP += 1 # col indices of the point
    for col in range(colP - 1, colP + 1 + 1):
        if check(point, newBoard[rowP-1][col]):
            nextPRow = (rowP - 1) - 1
            nextPCol = col - 1
            if checkedList[nextPRow][nextPCol] == 0:
                return nextPRow, nextPCol
    for col in range(colP - 1, colP + 1 + 1, 2):
        if check(point, newBoard[rowP][col]):
            nextPRow = (rowP) - 1
            nextPCol = col - 1
            if checkedList[nextPRow][nextPCol] == 0:
                return nextPRow, nextPCol
    for col in range(colP - 1, colP + 1 + 1):
        if check(point, newBoard[rowP+1][col]):
            nextPRow = (rowP + 1) - 1
            nextPCol = col - 1
            if checkedList[nextPRow][nextPCol] == 0:
                return nextPRow, nextPCol
    return None, None

def isKingsTour(board):
    if find1(board) == None: return False
    else:
        pRow, pCol = find1(board)

    size = len(board)
    
    checkedList = makeCheckedList(board)
    point = board[pRow][pCol]
    checkedList[pRow][pCol] = 1
    
    newBoard = makeFullBoard(board)

    while True:
        nextPRow, nextPCol = findNextmove(point, pRow, pCol, 
                                          newBoard, checkedList)
        if nextPRow != None and nextPCol != None:
            checkedList[nextPRow][nextPCol] = 1
            pRow = nextPRow
            pCol = nextPCol
            point = board[pRow][pCol]
            if point == size ** 2: 
                break
        else:
            return False
    return True
#################################################
# Part B
#################################################
def isMagicSquare(a):
    # Verify whether or not 'a' is a list
    if not isinstance(a, list):return False
    # Check square condition
    if len(a) != len(a[0]): return False
    """
    Verify the uniqueness of each element in each square, 
    and we'll concurrently calculate the total of each row.
    """
    rowSum = 0
    checkedSquare = list()
    for row in range(len(a)):
        if not isinstance(a[row], list): return False # Verify 2-d list
        sumEachRow = 0
        for col in range(len(a[0])):
            element = a[row][col]
            if not isinstance(element, int): return False 
            if element not in checkedSquare: checkedSquare.append(element)
            else: return False
            sumEachRow += element
        if row == 0:
            rowSum = sumEachRow
        else:
            if sumEachRow != rowSum: return False
    # The square's column sums have to match one another
    for col in range(len(a[0])):
        sumEachCol = 0
        for row in range(len(a)):
            sumEachCol += a[row][col]
        if sumEachCol != rowSum: return False
    # The square's diagonal sums have to equal one another
    firstDiagonalSum = sum((a[i][i]) for i in range(len(a)))
    secondDiagonalSum = sum((a[i][(len(a) - 1) - i]) for i in range(len(a)))
    if firstDiagonalSum != secondDiagonalSum: return False

    return True

#def wordSearchWithIntegerWildcards(board, word):

def wordSearchWithIntegerWildcards(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return False

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if (drow, dcol) != (0, 0):
                result = wordSearchFromCellInDirection(board, word,
                                                        startRow, startCol,
                                                        drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    i = 0
    while i < len(word): 
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)):
            return None
        element = board[row][col]
        if isinstance(element, int):
            if len(word) == element: return True
            elif len(word) > element:
                word = word[:i+1] + word[i+element:]
                i += 1
                continue
        if element != word[i]:
                return None
        i += 1
    return True
#################################################
def areLegalValues(values):
    checkedList = []
    rangeList = range(0, len(values) + 1)
    for number in values:
        if not (number in rangeList):
            return False
        elif not (number in checkedList):
            checkedList.append(number)
        elif number != 0:
            return False
    return True 
def isLegalRow(board, row):
    theRow = board[row]
    return areLegalValues(theRow)

def isLegalCol(board, col):
    theCol = []
    for row in range(len(board)):
        theCol.append(board[row][col])
    return areLegalValues(theCol)

def isLegalBlock(board, block):
    n = int(math.sqrt(len(board)))
    blockList = []
    for i in range(n):
        for j in range(n):
            blockList.append(board[(block // n) * n + i][(block % n) * n + j])
    return areLegalValues(blockList)

def isLegalSudoku(board):
    n = len(board[0])
    for num in range(n):
        if not (isLegalRow(board, num) and isLegalCol(board, num) 
                and isLegalBlock(board, num)):
            return False
    return True
#################################################
# Bonus/Optional
#################################################
def checkFullBoard(board):
    for row in board:
        if '-' in row:
            return False
    return True

def wordAdd(board, word):
    (rows, cols) = (len(board), len(board[0]))
    ways = list()
    locationOpti, countMax = tuple(), 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0] or board[row][col] == '-':
                result = wordAddFromCell(board, word, row, col)
                if (result != None):
                    ways.append(result)
    if len(ways) > 0:                
        for way in ways:
            if way[1] > countMax:
                locationOpti, countMax = way[0], way[1]
    else:
        return None
    if locationOpti:
        for element in locationOpti:
            board[element[0]][element[1]] = word[element[2]]
        return board       
    else:         
        return None

def wordAddFromCell(board, word, startRow, startCol):
    possibleDirections = 8 # 3^2 - 1
    ways = list()
    locationOpti, countMax = tuple(), 0
    for direction in range(possibleDirections):
        result = wordAddFromCellInDirection(board, word,
                                        startRow, startCol, direction)
        if (result != None):
            ways.append(result)
    
    if len(ways) > 0:
        for way in ways:
            if way[1] > countMax:
                locationOpti, countMax = way[0], way[1]
        return locationOpti, countMax
    else:
        return None
    
def wordAddFromCellInDirection(board, word, startRow, startCol, direction):
    # Check wheter we have '-' slots to add letters or not
    count = 0
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[direction]  
    locationOfEmptiesToAdd = list()

    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols)):
            return None 
        elif board[row][col] == '-':
            locationOfEmptiesToAdd.append((row,col,i))
        elif board[row][col] == word[i]:
            count += 1
        else:   
            return None
    return (locationOfEmptiesToAdd, count)

# It means that we can find the word in the board in some direction

def makeWordSearch(wordList, replaceEmpties):
    """
    It is possible that this process completes with no place to add the word. 
    In that case, add one more row and one more column of empty cells 
    to the board, keeping it square, 
    and then add the word to the bottom row starting at column 0 
    and heading to the right.
    """
    wordListLen = len(wordList)
    if wordListLen == 0:
        return None
    board  = [[]]  
    for word in wordList:
        letters = list(word)
        wordLen = len(word)
        # Keeping the board square
        if wordLen > len(board):
            board = []
            for row in board:
                row.extend(list('-' * (wordLen - len(row))))
            for _ in range(wordLen):
                rowToAdd = list('-' * wordLen)
                board.append(rowToAdd)
        # Adding words according to provided rules

        if word == wordList[0]:
            board[0] = letters
        else:
            if not checkFullBoard(board):
                wordAdd(board, word)
            else:
                board.append(list(word))
                for row in board:
                    row.append('-')
    
    if replaceEmpties == False:
        return board 
    elif replaceEmpties == True:
        board = fillLetters(board)
        return board

def fillLetters(board):
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    
    (rows, cols) = (len(board), len(board[0]))

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '-':
                checkNeighbor = list()
                for (x,y) in dirs:
                    rowD = row + x
                    colD = col + y 
                    if ((rowD < 0) or (rowD >= rows) or
                        (colD < 0) or (colD >= cols) or
                        (board[rowD][colD] == '-')): 
                        continue
                    
                    neighborOrd = ord(board[rowD][colD])
                    checkNeighbor.append(neighborOrd)
                    minOrd = min(checkNeighbor)
                    maxOrd = max(checkNeighbor)
                    if minOrd > ord('a'):
                        board[row][col] = 'a'
                    else:
                        nextMinOrd = minOrd + 1
                        while nextMinOrd != maxOrd:
                            if (nextMinOrd) not in checkNeighbor:
                                board[row][col] = chr(nextMinOrd)
                                break
                            else:
                                nextMinOrd += 1
                        else:
                            board[row][col] = chr(maxOrd+1)
    return board 

                
#################################################
# Test Functions (#ignore_rest)
#################################################

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare([[42]]) == True)
    assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True)
    assert(isMagicSquare([[4-7, 9-7, 2-7], [3-7, 5-7, 7-7], [8-7, 1-7, 6-7]])
           == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMagicSquare(a) == True)
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMagicSquare(a) == False)
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMagicSquare(a) == False)
    assert(isMagicSquare([[1, 2], [2, 1]]) == False)
    assert(isMagicSquare([[0], [0]]) == False) # Not square!
    assert(isMagicSquare([[1, 1], [1, 1]]) == False) # repeats
    assert(isMagicSquare('do not crash here!') == False)
    assert(isMagicSquare(['do not crash here!']) == False)
    assert(isMagicSquare([['do not crash here!']]) == False)
    print("Passed!")

def testNondestructiveRemoveRowAndCol():
    print('Testing nondestructiveRemoveRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testMatrixMultiply():
    print("Testing matrixMultiply()...", end='')
    m1 = [[1,2],
          [3,4]] # 2x2
    m2 = [[4],
          [5]]     # 2x1
    m3 = [[14],
          [32]]
    assert(matrixMultiply(m1,m2) == m3) 
    assert(matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], 
                          [[9, 8, 3],
                           [5, 1, 3]])==
                          [[62, 31, 30],
                           [61, 37, 27],
                           [65, 44, 27],
                           [75, 46, 33],
                           [117, 73, 51],
                           [83, 60, 33]])
    assert matrixMultiply([[8]],[[5]])==[[40]]
    print("Passed!")

def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    a = [ [  3, 2, 1 ],
          [  6, 4, 9 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  2, 8, 9 ],
          [  3, 1, 7 ],
          [  4, 5, 6 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
    assert(isKingsTour(a) == True)
    a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
    assert(isKingsTour(a) == False)
    a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
    assert(isKingsTour(a) == False)
    b = [ [  1, 14, 15, 16],
          [ 13,  2,  7,  6],
          [ 12,  8,  3,  5],
          [ 11, 10,  9,  4] ]
    assert(isKingsTour(b) == True)
    b = [ [  1, 14, 15, 16],
          [ 13,  2,  7,  6],
          [ 12,  8,  3,  5],
          [ 11, 10,  9,  1] ]
    assert(isKingsTour(b) == False)
    b = [ [  1, 14, 15, 16],
          [ 13,  2,  7,  6],
          [ 12,  8,  3,  3],  # Duplicate 3
          [ 11, 10,  9,  4] ]
    assert(isKingsTour(b) == False)
    c = [ [  2,  3,  4,  5,  6],
          [  1, 22, 15, 14,  7],
          [ 23, 21, 16, 13,  8],  # Duplicate 3
          [ 24, 20, 17, 12,  9],
          [ 25, 19, 18, 11, 10] ]
    assert(isKingsTour(c) == True)
    print("Passed!")

def testWordSearchWithIntegerWildcards():
    print("Testing wordSearchWithIntegerWildcards()...", end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "dog") == True)
    assert(wordSearchWithIntegerWildcards(board, "cat") == True)
    assert(wordSearchWithIntegerWildcards(board, "tad") == True)
    assert(wordSearchWithIntegerWildcards(board, "cow") == False)
    board = [ [ 'd', 'o',  1  ],
              [  3 , 'a', 'c' ],
              [ 'o', 'q' ,'t' ],
            ]
    assert(wordSearchWithIntegerWildcards(board, "z") == True)
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "dzzo") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzd") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzo") == True)
    board = [ [ 3 ] ]
    assert(wordSearchWithIntegerWildcards(board, "zz") == False)
    assert(wordSearchWithIntegerWildcards(board, "zzz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzzz") == False)
    board = [ [ 'a', 'b', 'c' ],
              [ 'd',  2 , 'e' ],
              [ 'f', 'g', 'h' ]]
    assert(wordSearchWithIntegerWildcards(board, "aqqh") == True)
    assert(wordSearchWithIntegerWildcards(board, "aqqhh") == False)
    assert(wordSearchWithIntegerWildcards(board, "zz") == True)
    assert(wordSearchWithIntegerWildcards(board, "zzc") == True)
    assert(wordSearchWithIntegerWildcards(board, "zaz") == False)
    print("Passed!")

def testIsLegalSudoku():
    # From Leon Zhang!
    print("Testing isLegalSudoku()...", end="")
    board = [[0]]
    assert isLegalSudoku(board) == True
    board = [[1]]
    assert isLegalSudoku(board) == True

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [[0, 4, 0, 0],
             [0, 0, 3, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 2]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 1, 2],
             [2, 1, 4, 3],
             [4, 3, 2, 1]]
    assert isLegalSudoku(board) == True
    board = [[1, 2, 3, 4],
             [3, 4, 4, 2],
             [2, 4, 4, 3],
             [4, 3, 2, 1]]    
    assert isLegalSudoku(board) == False

    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert isLegalSudoku(board) == True
    
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 9, 7, 9 ]
    ]
    assert isLegalSudoku(board) == False
    board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert isLegalSudoku(board) == True
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6, 8]]
    assert isLegalSudoku(board) == True
    # last number is supposed to be 8, not 10
    board = [
    [ 2,11, 9, 5, 8,16,13, 4,12, 3,14, 7,10, 6,15, 1],
    [ 4,12,15,10, 3, 6, 9,11,13, 5, 8, 1,16, 7,14, 2],
    [ 1,14, 6, 7,15, 2, 5,12,11, 9,10,16, 3,13, 8, 4],
    [16,13, 8, 3,14, 1,10, 7, 4, 6, 2,15, 9,11, 5,12],
    [12, 2,16, 9,10,14,15,13, 8, 1, 5, 3, 6, 4,11, 7],
    [ 6, 7, 1,11, 5,12, 8,16, 9,15, 4, 2,14,10, 3,13],
    [14, 5, 4,13, 6,11, 1, 3,16,12, 7,10, 8, 9, 2,15],
    [ 3, 8,10,15, 4, 7, 2, 9, 6,14,13,11, 1,12,16, 5],
    [13, 9, 2,16, 7, 8,14,10, 3, 4,15, 6,12, 5, 1,11],
    [ 5, 4,14, 6, 2,13,12, 1,10,16,11, 8,15, 3, 7, 9],
    [ 7, 1,11,12,16, 4, 3,15, 5,13, 9,14, 2, 8,10, 6],
    [10,15, 3, 8, 9, 5,11, 6, 2, 7, 1,12, 4,14,13,16],
    [11,10,13,14, 1, 9, 7, 8,15, 2, 6, 4, 5,16,12, 3],
    [15, 3, 7, 4,12,10, 6, 5, 1, 8,16,13,11, 2, 9,14],
    [ 8, 6, 5, 1,13, 3,16, 2,14,11,12, 9, 7,15, 4,10],
    [ 9,16,12, 2,11,15, 4,14, 7,10, 3, 5,13, 1, 6,10]]
    assert isLegalSudoku(board) == False
    print("Passed!")

def testMakeWordSearch():
    print("Testing makeWordSearch()...", end="")
    board = makeWordSearch([], False)
    assert(board == None)

    board = makeWordSearch(["ab"], False)
    assert(board == [['a', 'b'], ['-', '-'] ])
    board = makeWordSearch(["ab"], True)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd"], False)
    assert(board == [['a', 'b'], ['c', 'd'] ])
    board = makeWordSearch(["ab", "bc", "cd", "de"], False)
    assert(board == [['a', 'b', '-'], ['c', 'd', '-'], ['d', 'e', '-']])
    board = makeWordSearch(["ab", "bc", "cd", "de"], True)
    assert(board == [['a', 'b', 'a'], ['c', 'd', 'c'], ['d', 'e', 'a']])

    board = makeWordSearch(["abc"], False)
    assert(board == [['a', 'b', 'c'], ['-', '-', '-'], ['-', '-', '-']])
    board = makeWordSearch(["abc"], True)
    assert(board == [['a', 'b', 'c'], ['c', 'd', 'a'], ['a', 'b', 'c']])

    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], False)
    assert(board == [['a', 'b', 'c'], ['d', 'e', '-'], ['c', 'f', 'g']])
    board = makeWordSearch(["abc", "adc", "bd", "bef", "gfc"], True)
    assert(board == [['a', 'b', 'c'], ['d', 'e', 'a'], ['c', 'f', 'g']])

    board = makeWordSearch(["abcd", "abc", "dcb"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['-', '-', '-', '-'], 
                     ['-', '-', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya"], False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', '-', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', '-', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           False)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', '-'], 
                     ['-', 'a', '-', '-'],
                     ['-', '-', 'b', '-']])
    board = makeWordSearch(["abcd", "abc", "dcb", "xa", "bya", "bax", "dca"],
                           True)
    assert(board == [['a', 'b', 'c', 'd'],
                     ['x', 'y', 'c', 'a'], 
                     ['b', 'a', 'd', 'e'],
                     ['c', 'e', 'b', 'a']])

    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testMatrixMultiply()
    testIsKingsTour()

    # Part B:
    testIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    testIsLegalSudoku()

    # Bonus:
    testMakeWordSearch()

def main():
    cs112_s22_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()