#################################################
# hw4.py
# name: Dinh Duc Thanh
# andrew id: Dtaa
#################################################

import cs112_s22_week4_linter
import math, copy
from typing import List

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

def alternatingSum(L: List[int]) -> int:
    """
    Takes a list of numbers and returns the alternating sum,
    where the sign alternates from + to - and vice versa.
    For example, alternating_sum([5, 3, 8, 4]) returns 6 (that is, 5-3+8-4).

    Args:
        L (List[int]): The list of integers to be summed alternately.

    Returns:
        int: The alternating sum of the input list.
    """
    ans = 0
    signPov = True
    for element in L:
        if signPov:
            ans += element
            signPov = False
        else:
            ans += -element
            signPov = True
    return ans 

def median(L: List[int]) -> float:
    """
    non-destructive function that finds the median value of a list

    Args:
        L (): The list of integers or floating point numbers
    
    Return:
        int or float:the value of the middle element, 
        or the average of the two middle elements 
        if there is no single middle element.
        If the list is empty, return None
    """
    newList = sorted(L)
    lengthL = len(newList)
    if lengthL == 0: return
    middleIndex = lengthL // 2
    middleIndexRemainder = lengthL % 2
    if middleIndexRemainder != 0:
        return newList[middleIndex]
    else:
        return (newList[middleIndex-1] + newList[middleIndex]) / 2
    
def smallestDifference(L: List[int]) -> int:
    """
    Find the smallest absolute difference between any two integers in the list
    """
    L.sort()
    lengthL = len(L)
    if lengthL <= 1: 
        return -1
    ans = 0
    for index in range(lengthL):
        if index != lengthL - 1: 
            diff = abs(L[index] - L[index+1])
            if index == 0:
                ans = diff
            elif diff <= ans:
                ans = diff
        else:
            return ans

def nondestructiveRemoveRepeats(L):
    """
    the function is non-destructive, which takes a list L and 
    returns a new list in which any repeating elements in L are removed. 
    """
    ans = list()
    for num in L:
        if not (num in ans):
            ans.append(num)
    return ans

def destructiveRemoveRepeats(L):
    numbers = list()
    index = 0
    while index < len(L):
        if L[index] in numbers:
            L.pop(index)
        else:
            numbers.append(L[index])
            index += 1     
    return

#################################################
# Part B
#################################################

def isSorted(L):
    """
    takes a list of numbers and returns True if the list is sorted
    (either smallest-first or largest first) and False otherwise
    Big(O): O(n) time
    -> particularly not sort the list
    """
    lengthL  = len(L)
    if lengthL <= 2: return True
    
    increase = False
    decrease = False
    finded = False

    for index in range(lengthL - 1):
        if (not finded) and L[index] > L[index+1]:
            decrease = True
            finded = True
            continue
        
        elif (not finded) and L[index] < L[index+1]:
            increase = True
            finded = True
            continue
        
        if decrease and L[index] < L[index+1]:
            return False
        elif increase and L[index] > L[index+1]:
            return False
    
    return True

def lookAndSay(L):
    lengthL  = len(L)
    if lengthL <= 1: return L
    number = L[0]
    count = 0
    ans = list()
    for index in range(lengthL):
        if index != lengthL-1:
            if L[index] == number:
                count += 1
            else:
                ans.append((count, number))
                number = L[index]
                count = 1
        else:
            lastNum = L[index]
            if lastNum == number:
                ans.append((count + 1, number))
            else:
                ans.append((count, number))
                ans.append((1, lastNum))
    return ans

def inverseLookAndSay(L):
    lengthL = len(L)
    if lengthL == 0: return []

    ans = []

    for pair in L: 
        ans += [pair[1]] * pair[0]
    return ans

def multiplyPolynomials(p1, p2):
    lengthAns = len(p1) + len(p2) - 1
    ans = [0] * lengthAns
    for index1 in range(len(p1)):
        for index2 in range(len(p2)):
            indexAns = index1 + index2
            element = ans[indexAns] + p1[index1] * p2[index2]
            ans[indexAns] = element
    return ans

def wordScore(word, letterScores, hand):
    score = 0
    for char in word:
        if char not in hand:
            return False
        else:
            score += letterScores[ord(char) - ord('a')]
            indexOfChar = hand.index(char)
            hand = hand[ : indexOfChar] + hand[indexOfChar+1 : ]
    return score

def bestScrabbleScore(dictionary, letterScores, hand):
    scoreList = []
    for word in dictionary:
        score = wordScore(word, letterScores, hand)
        if type(score) == int:
            scoreList.append((word, score))
        else:
            continue

    maxWordList = []
    maxScore = 0

    if scoreList == []: return 
    else:
        for tuple in scoreList:
            if tuple[1] > maxScore:
                maxScore = tuple[1]

        for tuple in scoreList:
            if tuple[1] == maxScore:
                maxWordList.append(tuple[0])
        
        if len(maxWordList) == 1:
            return (maxWordList[0], maxScore)
        else:   
            return (maxWordList, maxScore)

#################################################
# Bonus/Optional
#################################################
def linearRegression(pointsList):
    #Step1: Find mean(x), mean(y)
    xSum, ySum = 0, 0
    lenlist = len(pointsList)
    for point in pointsList:
        xSum += point[0]
        ySum += point[1]
    xMean = xSum / lenlist
    yMean = ySum / lenlist
    #Step2: Compute variances: SS_{xx} and SS_{yy} 
    ##Step2.1: Compute (x_i - mean(x)) and (y_i - mean(y))
    varXX, varYY = 0, 0
    corXY = 0
    for point in pointsList:
        diffX = (point[0] - xMean)
        varXX += diffX ** 2
        diffY = (point[1] - yMean)
        varYY += diffY ** 2
        corXY += diffX * diffY
    """
    the regress line: y = ax + b
    """
    #Step3: Compute the slope of the line (\hat{y}) and 
    # correlation coefficient
    if varYY == 0: ## horizontal line
        a = 0 
        r = 1
    else:
        a = corXY / varXX
        r = (corXY ** 2 / (varXX * varYY)) ** (1/2)
    ##if varXX == 0:  vertical line -> not the form: y = ax + b instead x = b
    #Step4: Compute "b" the y-intercept of \hat{y}
    b = yMean - a * xMean
    return (a, b, r)

#def afterLocal(line, local, argns):
def prefixCal(sign, opd1, opd2):
    if sign == '+':
        return opd1 + opd2
    elif sign == '-':
        return opd1 - opd2

def extractElement(element, locals, args=None):
    if element[0] == "A":
        return args[int(element[1])]
    elif element[0] == "L":
        return locals[int(element[1])]
    else:
        return int(element)
    
def jmpParser(jmp, expr, locals):
    if jmp == "JMP+":
        return extractElement(expr, locals) > 0
    elif jmp == "JMP0":
        return extractElement(expr, locals) == 0

def runSimpleProgram(program, args):
    locals = list()
    label, countLine = None, 0
    lines = list()

    for line in program.splitlines():
        line = line.strip()
        lines.append(line)

    while True:
        line = lines[countLine].strip()
        if line.startswith("JMP"):
            line = line.split(" ")
            if line[0] == "JMP":
                label = line[1] + ":"
                countLine = lines.index(label)
            elif jmpParser(line[0], line[1], locals):
                label = line[2] + ":"
                countLine = lines.index(label)
        elif line.startswith("L"):
            line = line.split(" ")
            localIndexInLine = int(line[0][1])
            if ("+" in line) or ("-" in line):
                value = prefixCal(line[1], 
                                  extractElement(line[2], locals, args),
                                  extractElement(line[3], locals, args))
                if localIndexInLine > len(locals) - 1:
                    locals.append(value)
                elif localIndexInLine <= len(locals) - 1:
                        locals[localIndexInLine] = value
            else:
                if localIndexInLine > len(locals) - 1:
                    locals.append(int(line[1]))
                elif localIndexInLine <= len(locals) - 1:
                    locals[localIndexInLine] = int(line[1])
        
        elif line.startswith('RTN'):
            line = line.split(" ")
            return extractElement(line[1], locals, args)  
            
        countLine += 1


#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed!')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed!')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = a + [ ] # copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed!")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    c = [0,1,1,1,2,4,-6]
    assert(destructiveRemoveRepeats(c) == None)
    assert(c == [0,1,2,4,-6])
    print("Passed!")

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = a + [ ] # copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = a + [ ] # copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def relaxedAlmostEqual(d1, d2):
    epsilon = 10**-3 # really loose here
    return abs(d1 - d2) < epsilon

def tuplesAlmostEqual(t1, t2):
    if (len(t1) != len(t2)): return False
    for i in range(len(t1)):
        if (not relaxedAlmostEqual(t1[i], t2[i])):
            return False
    return True

def testLinearRegression():
    print("Testing bonus problem linearRegression()...", end="")

    ans = linearRegression([(1,3), (2,5), (4,8)])
    target = (1.6429, 1.5, .9972)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,0), (1,2), (3,4)])
    target = ((9.0/7), (2.0/7), .9819805061)
    assert(tuplesAlmostEqual(ans, target))

    #perfect lines
    ans = linearRegression([(1,1), (2,2), (3,3)])
    target = (1.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    
    ans = linearRegression([(0,1), (-1, -1)])
    target = (2.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    #horizontal lines
    ans = linearRegression([(1,0), (2,0), (3,0)])
    target = (0.0, 0.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))

    ans = linearRegression([(1,1), (2,1), (-1,1)])
    target = (0.0, 1.0, 1.0)
    assert(tuplesAlmostEqual(ans, target))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing bonus problem runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testAlternatingSum()
    testMedian()
    testSmallestDifference()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

    # Part B:
    testIsSorted()
    testLookAndSay()
    testInverseLookAndSay()
    testMultiplyPolynomials()
    testBestScrabbleScore()

    # Bonus:
    testLinearRegression()
    testRunSimpleProgram() 

def main():
    cs112_s22_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()