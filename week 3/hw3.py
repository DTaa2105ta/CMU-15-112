#################################################
# hw3.py
# name:
# andrew id:
#################################################

import cs112_s22_week3_linter
import math
from cmu_112_graphics import *
import string
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

def rotateString(s, k):
    placed = ''
    lengthS = len(s)
    if k == 0: 
        return s
    elif k > 0: # for left rotate
        k %= lengthS
        placed = s[:k]
        s = s[k:]
        return s + placed
    else: # for right rotate
        index = None
        k %= (-lengthS) 
        if k == 0: return s 
        #put the condition k=0 
        #otherwise the case when index = lengthS then placed will be nothing
        else:
            index = lengthS - abs(k)
            placed = s[index:]
            s = s[:k]
            return placed + s

def applyCaesarCipher(message, shift):
    # you are guaranteeds that message is a string
    # shift is an integer between -25 and 25
    # Capital letters should stay capital 
    # and lowercase letters should stay lowercase
    # Note that "Z" wraps around to "A"
    # non-letter characters should not be changed
    ans = ''
    lower = string.ascii_lowercase
    lengthOfLetterSet = len(lower)
    upper = string.ascii_uppercase
    for char in message:
        if char in lower:
            newIndex = (lower.find(char) + shift) % lengthOfLetterSet
            ans += lower[newIndex] 
        elif char in upper:
            newIndex = (upper.find(char) + shift) % lengthOfLetterSet 
            ans += upper[newIndex] 
        else:
            ans += char
    return ans

def largestNumber(s):
    # takes a string of text
    # returns the largest int value that occurs within that text
    # returns None if no such value occurs
    numSet = string.digits
    findedNum = False
    maxNum = 0
    num = ''
    s = s + " "
    for char in s:
        if char in numSet:
            num += char
            findedNum = True
        elif (char == ' ' and findedNum):
            num = int(num)
            if num >= maxNum: 
                maxNum = num 
                num, findedNum = '', False
    if maxNum == 0: return
    else:
        return maxNum

def topScorer(data):
    # take a multi-lines string encoding scores as csv data 
    # If there is a tie, return all players in a comma-separated string
    #with the names in same order they appeared in the original data.
    if data == '': 
        return
    winnerName = ''
    winnerScore = 0
    namesForSameScore = ''
    playerScore = 0

    for line in data.splitlines():
        lineSplit = line.split(',')
        for value in lineSplit:
            if value != lineSplit[0]:
                playerScore += int(value)
            else:
                playerName = value
        
        if playerScore > winnerScore:
            findedWinner = True
            winnerName = playerName
            winnerScore = playerScore
        elif playerScore == winnerScore:
            findedWinner = False
            if namesForSameScore == '':
                namesForSameScore += winnerName
            namesForSameScore += ("," + playerName)

        playerScore = 0
    
    if findedWinner == True:
        return winnerName
    else:
        return namesForSameScore

#################################################
# Part B
#################################################

def collapseWhitespace(s):
    #Each space will merge into a single space.
    nonSpace = ''
    whiteSpace = string.whitespace
    findedSpaceChar = False
    for char in s:
        if char in whiteSpace and not findedSpaceChar:
            findedSpaceChar = True
            nonSpace += ' '
        elif char not in whiteSpace:
            findedSpaceChar = False
            nonSpace += char
    return nonSpace

def messageWithoutSpace(msg):
    ans = ''
    for char in msg:
        if char != ' ':
            ans += char
    return ans

def patternedMessage(msg, pattern):
    whiteSpace = string.whitespace
    msg = messageWithoutSpace(msg)
    lengthMsg = len(msg)
    index = 0
    ans = ''
    for symbol in pattern:
        if symbol in whiteSpace:
            ans += symbol
        else:
            ans += msg[index]
            index = (index + 1) % lengthMsg

    ansLen = len(ans)
    if ansLen == 0: return ''
    if ans[0] in whiteSpace:
        ans = ans[1:]
        ansLen -= 1 
    if ans[ansLen - 1] in whiteSpace:
        ans = ans[:(ansLen - 1)]
    return ans

def reverseString(s):
    return s[::-1]

def rowColToIndex(row,col,rowsNum):
    return row + rowsNum * col

def colRowToDecodedIndex(row, col, colsNum):
    return col + colsNum * row

def encodeRightLeftRouteCipher(text, rows):
    # assume the message only contains uppercase letters
    # clever  scheme of  indexing the message string where
    # you translate a row and column into single index into the message string.
    ans = ''
    paddedString = ''
    lowerCaseLetter = string.ascii_lowercase

    textLength = len(text)

    ## Find the dimension of the conceptual 2d grid
    columns = math.ceil(textLength/rows)
    ## Pad the string
    paddedString += text
    maxTextLen = rows * columns
    numberOfLettersToAdd = maxTextLen - textLength
    for i in range(1, numberOfLettersToAdd + 1):
        paddedString += lowerCaseLetter[-i]

    ## Label the padded string with row, col, and i
    ### Find the function that takes any row and col
    ### returns the coresponding index i in the padded string
    '''
    we have rowColToIndex(row,col,rowsNum)
    '''
    ## Firstly, every row goes right-to-left
    ### Two loops: one going over every row
    for i in range(rows):
        for j in range(columns): 
            ans += paddedString[rowColToIndex(i,j,rows)]
    ## Now alternate left-to-right and right-to-left
    beginIndex = 1
    endIndex = 0
    for otherRow in range(1, rows, 2):
        beginIndex = columns * otherRow  
        endIndex = beginIndex + columns-1
        if endIndex != maxTextLen - 1:
            ans = ans[:beginIndex] + \
                reverseString(ans[beginIndex:endIndex+1]) + ans[endIndex+1:]
        else:
            ans = ans[:beginIndex] + \
                reverseString(ans[beginIndex:])
    return str(rows) + ans

def decodeRightLeftRouteCipher(cipher):
    lowerCase = string.ascii_lowercase

    rows, cipherText = int(cipher[0]), cipher[1:]
    cipherTextLen = len(cipherText)
    columns = cipherTextLen // rows

    beginIndex = 1
    endIndex = 0
    cipherTextLeftToRight = cipherText
    for otherRow in range(1, rows, 2):
        beginIndex = columns * otherRow  
        endIndex = beginIndex + columns-1
        if endIndex != cipherTextLen - 1:
            cipherTextLeftToRight = cipherTextLeftToRight[:beginIndex] + \
                reverseString(cipherTextLeftToRight[beginIndex:endIndex+1]) + \
                    cipherTextLeftToRight[endIndex+1:]
        else:
            cipherTextLeftToRight = cipherTextLeftToRight[:beginIndex] + \
                reverseString(cipherTextLeftToRight[beginIndex:])

    decodedText = ''
    for i in range(columns):
        for j in range(rows): 
            char = cipherTextLeftToRight[colRowToDecodedIndex(j, i, columns)]
            if char not in lowerCase:
                decodedText += char

    return decodedText

#################################################
# Part B Drawings
#################################################

# Make sure you have cmu_112_graphics downloaded to the 
# same directory as this file!

# Note: If you don't see any text when running graphics code, 
# try changing your computer's color theme to light mode. 

def drawFlagOfTheEU(canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0, y0, x1, y1, fill='blue', outline='black')
    size = (x1 - x0) // 12
    canvas.create_text((x0 + x1)/2, (y0 + y1)/2, fill='black',
                       text='Draw the EU flag here!', font=f'Arial {size} bold')
    # Your code goes here!
    cx, cy = (x0+x1)/2, (y0+y1)/2
    r = min((x1-x0), (y1-y0))/3
    rS = min((x1-x0), (y1-y0)) / 22
    for starTh in range(12):
        angle = math.pi/2 - starTh * (2 * math.pi/12)
        xAxe = cx + r * math.cos(angle)
        yAxe = cy - r * math.sin(angle)
        canvas.create_oval(xAxe-rS, yAxe-rS, xAxe+rS, yAxe+rS, fill='yellow')

def drawSimpleTortoiseProgram(program, canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill='white', outline='black')

    # Your code goes here!
    ## 'left n' or 'right n'
    ## Tortoise will turn to the left or to the right, \
    ## without moving, where n is a non-negative number 
    turtoiseX = width / 2
    turtoiseY = height / 2
    color = 'none'      #default color
    angle = math.radians(0) #dafault angle

    canvas.create_text(2*width/5, height/4, text=program, 
                           font='Arial 10',fill='gray')

    for line in program.splitlines():

        if not (line.startswith('#') or line == ''):
            lineSplit = line.split(' ')
            command, value = lineSplit[0], lineSplit[1]
            if command == 'color':
                    color = value
            elif command == 'right':
                value = math.radians(int(value))
                angle = (angle + value) 
            elif command == 'left':
                value = math.radians(int(value))
                angle = (angle - value) 
            elif command == 'move':
                    value = int(value)
                    turtoiseXNew = turtoiseX + value * math.cos(
                        angle)
                    turtoiseYNew = turtoiseY + value * math.sin(
                        angle)
                    if color != 'none':
                        canvas.create_line(turtoiseX, turtoiseY,
                                                turtoiseXNew, turtoiseYNew,
                                                fill=color, width=4)
                    turtoiseX = turtoiseXNew
                    turtoiseY = turtoiseYNew
            
#################################################
# Bonus/Optional
#################################################

def bonusTopLevelFunctionNames(code):
    ans = ''
    flagQuote1 = False
    flagQuote2 = False
    flagComment = False
    tripleQuotes1 = 3 * '"' 
    tripleQuotes2 = 3 * "\'"
    for line in code.splitlines():
        if line.startswith("#"):
            continue
        elif line.startswith("def"):
            thisLine = line.split(" ")
            for word in thisLine:
                if word == '#' and not flagComment:
                    break
            else:
                if (not flagQuote1) and (tripleQuotes1 in thisLine):
                        flagQuote1 = True
                        flagComment = True
                elif (not flagQuote2) and (tripleQuotes2 in thisLine):
                        flagQuote2 = True 
                        flagComment = True
                else:
                    if tripleQuotes2 in thisLine[-1]:
                        flagQuote2 = False
                        flagComment = False
                        continue
                    elif tripleQuotes1 in thisLine[-1]:
                        flagQuote1 = False
                        flagComment = False
                        continue
            funcName = thisLine[1][0]
            if ans == '': ans += funcName
            elif funcName not in ans: 
                ans += ("." + funcName)
            else: continue 
    return ans

def findLeftOpt(expr,indexOpt):
    leftNumIndex = indexOpt
    while True:
        leftNumIndex -= 1
        if expr[leftNumIndex].isdigit() == False:
            break
        elif leftNumIndex == 0:
            return leftNumIndex
    return leftNumIndex + 1

def findRightOpt(expr,indexOpt):
    rightNumIndex = indexOpt
    while True:
        rightNumIndex += 1
        if expr[rightNumIndex].isdigit() == False:
            break
        elif rightNumIndex == (len(expr) - 1):
            return rightNumIndex
    return rightNumIndex - 1

def applyOpt(leftNum, opt, rightNum):
    leftNum = int(leftNum)
    rightNum = int(rightNum)
    if opt == "**":
        return str(leftNum ** rightNum)
    elif opt == "//":
        return str(leftNum // rightNum)
    elif opt == "*":
        return str(leftNum * rightNum)
    elif opt == "/":
        return str(leftNum / rightNum)
    elif opt == "%":
        return str(leftNum % rightNum)
    elif opt == "+":
        return str(leftNum + rightNum)
    elif opt == "-":
        return str(leftNum - rightNum)

def applyOptForAns(expr, precedence):
    indexOpt = expr.find(precedence)
    leftNumIndex = findLeftOpt(expr,indexOpt)
    if len(precedence) == 1:
        rightNumIndex = findRightOpt(expr,indexOpt)
        return expr[:leftNumIndex] + \
            applyOpt(expr[leftNumIndex:indexOpt], precedence, 
                     expr[indexOpt+1:rightNumIndex+1]) + \
                expr[rightNumIndex+1:]
    elif len(precedence) == 2:
        #since for the case "**" and "//" we skip the next index of '/' and '*'
        rightNumIndex = findRightOpt(expr,indexOpt+1)
        return expr[:leftNumIndex] + \
            applyOpt(expr[leftNumIndex:indexOpt], precedence, 
                     expr[indexOpt+2:rightNumIndex+1]) + \
                expr[rightNumIndex+1:]

def buildRealAns(expr, ans, realAns):
    lenExpr = len(expr)
    if realAns == '':
        realAns = expr + ' = ' + ans
    else:
        realAns += '\n' + lenExpr * ' ' + ' = ' + ans 
    return realAns

def bonusGetEvalSteps(expr):
    # Numbers are limited to non-negative integers
    # Operators are limited to +,-,*,/,//,% and **
    # Precedence ** first, then *,/,//,%, then +, -
    if len(expr) == 1:
        return expr + ' = ' + expr
    
    realAns = ''
    ans = expr

    precedence1, precedence2, precedence3 = '**', '//%*/', '+-'
    
    while ans.find(precedence1) != -1:
        ans = applyOptForAns(ans, precedence1)
        realAns = buildRealAns(expr, ans, realAns)

    for char in ans:
        charIndex = ans.find(char)
        if (charIndex < (len(ans) - 1)) and (char + ans[charIndex+1]) == '//':
            ans = applyOptForAns(ans, '//')
            realAns = buildRealAns(expr, ans, realAns)
       
        elif char in precedence2 and \
            (charIndex > 0) and ans[charIndex-1] != '/':
            ans = applyOptForAns(ans, char)
            realAns = buildRealAns(expr, ans, realAns)
    
    for char in ans:
        if char in precedence3:
            ans = applyOptForAns(ans, char)
            realAns = buildRealAns(expr, ans, realAns)

    return realAns

#################################################
# Test Functions
#################################################

def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
John,1,30,20,10
'''
    assert(topScorer(data) == 'Fred,Wilma,John')
    assert(topScorer('') == None)

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
Elly,10,20,30,2
John,1,30,20,10
'''
    assert(topScorer(data) == 'Elly')
    assert(topScorer('') == None)

    data = '''\
Elly,10,20,30,2
Fred,11,20,30
Wilma,10,20,30,1
John,1,30,20,10
'''
    assert(topScorer(data) == 'Elly')
    assert(topScorer('') == None)

    data = '''\
Elly,10,20,30,1
Fred,10,20,30,2
Wilma,10,20,30,3
John,10,20,30,3
Emma,10,20,30,3
'''
    assert(topScorer(data) == 'Wilma,John,Emma')
    assert(topScorer('') == None)
    print('Passed!')

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    #assert(patternedMessage("abc def",   "***** ***** ****")   ==
           #"abcde fabcd efab")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")

    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
    print("Passed!")

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testBonusTopLevelFunctionNames():
    print("Testing bonusTopLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(bonusTopLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(bonusTopLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing bonusGetEvalSteps()...", end="")
    assert(bonusGetEvalSteps("0") == "0 = 0")
    assert(bonusGetEvalSteps("2") == "2 = 2")
    assert(bonusGetEvalSteps("3+2") == "3+2 = 5")
    assert(bonusGetEvalSteps("3-2") == "3-2 = 1")
    assert(bonusGetEvalSteps("3**2") == "3**2 = 9")
    assert(bonusGetEvalSteps("31%16") == "31%16 = 15")
    assert(bonusGetEvalSteps("31*16") == "31*16 = 496")
    assert(bonusGetEvalSteps("32//16") == "32//16 = 2")
    assert(bonusGetEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(bonusGetEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(bonusGetEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(bonusGetEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# Graphics Test Functions
#################################################

def testDrawFlagOfTheEU(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfTheEU(canvas, 50, 125, 350, 275)
    drawFlagOfTheEU(canvas, 425, 100, 575, 200)
    drawFlagOfTheEU(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-25, fill='black',
                       text="Testing drawFlagOfTheEU")
    canvas.create_text(app.width/2, app.height-10, fill='black',
                       text="This does not need to resize properly!")

def testDrawSimpleTortoiseProgram(app, canvas, programName, program):
    drawSimpleTortoiseProgram(program, canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-10, fill='black',
          text=(f'testing drawSimpleTortoiseProgram with {programName} ' + 
                f'(canvas, {app.width}, {app.height})'))

def testDrawSimpleTortoiseProgram_with_program_A(app, canvas):
    programA = '''\
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program A', programA)

def testDrawSimpleTortoiseProgram_with_program_B(app, canvas):
    programB = '''\
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50'''
    testDrawSimpleTortoiseProgram(app, canvas, 'program B', programB)

def drawSplashScreen(app, canvas):
    text = f'''\
Press the number key for the 
exercise you would like to test!

1. drawFlagOfTheEU
2. drawSimpleTortoiseProgram (with program A)
3. drawSimpleTortoiseProgram (with program B)

Press any other key to return
to this screen.
'''
    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text, fill='black',
                       font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.timerDelay = 10**10

def keyPressed(app, event):
    app.lastKeyPressed = event.key

def redrawAll(app, canvas):
    if app.lastKeyPressed == '1':
      testDrawFlagOfTheEU(app, canvas)
    elif app.lastKeyPressed == '2':
      testDrawSimpleTortoiseProgram_with_program_A(app, canvas)
    elif app.lastKeyPressed == '3':
      testDrawSimpleTortoiseProgram_with_program_B(app, canvas)
    else:
      drawSplashScreen(app, canvas)

def testGraphicsFunctions():
    runApp(width=600, height=600)

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testRotateString()
    testApplyCaesarCipher()
    testLargestNumber()
    testTopScorer()

    # Part B:
    testCollapseWhitespace()
    testPatternedMessage()
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

    # Part B Graphics:
    # testGraphicsFunctions()

    # Bonus:
    testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()

def main():
    cs112_s22_week3_linter.lint()
    testAll()
    # testGraphicsFunctions()

if __name__ == '__main__':
    main()
