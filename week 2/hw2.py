#################################################
# hw2.py
# name: Dinh Đuc Thanh
# andrew id: 21053638
#################################################

import cs112_s22_week2_linter
import math

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

#################################################
# Part A
#################################################

def digitCount(n):
    if n == 0: return 1
    count = 0
    n = abs(n)
    while n != 0:
        count += 1
        n = n // 10
    return count

def gcd(a,b):
    #gcd(x, y) == gcd(y, x%y)
    while a != 0 and b != 0:
        if a == b:
            return a
        elif a > b:
            a = a%b
        else:
            b = b%a
    return a if b == 0 else b

def hasConsecutiveDigits(n):
    n = abs(n)
    while digitCount(n) != 1:
        firstDigit = n%10
        secondDigit = (n//10) % 10
        n //= 10
        if firstDigit == secondDigit: 
            return True
    return False
#helper function for nthAdditivePrime()
def isPrime(n):
    if (n<2):
        return False
    if (n==2):
        return True
    if (n%2==0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n%factor==0):
            return False
    return True

def sumOfDigits(n):
    n = abs(n)
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def nthAdditivePrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess) and isPrime(sumOfDigits(guess))):
            found += 1
    return guess

def mostFrequentDigit(n):
    n = abs(n)
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 = 0,0,0,0,0,0,0,0,0,0
    while n != 0:
        digit = n%10

        if digit == 0:
            x0 += 1
        elif digit == 1:
            x1 += 1
        elif digit == 2:
            x2 += 1
        elif digit == 3:
            x3 += 1
        elif digit == 4:
            x4 += 1
        elif digit == 5:
            x5 += 1
        elif digit == 6:
            x6 += 1            
        elif digit == 7:
            x7 += 1
        elif digit == 8:
            x8 += 1
        else:
            x9 += 1
        
        n //= 10

    maxF = max(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9)

    if x0 == maxF:
        return 0
    elif x1 == maxF:
        return 1
    elif x2 == maxF:
        return 2       
    elif x3 == maxF:
        return 3
    elif x4 == maxF:
        return 4 
    elif x5 == maxF:
        return 5
    elif x6 == maxF:
        return 6
    elif x7 == maxF:
        return 7
    elif x8 == maxF:
        return 8
    else:
        return 9                 

def isRotation(x, y):
    if x == y:
        return True 
    sumDigit1 = 0
    sumDigit2 = 0
    digit1 = 0
    digit2 = 0
    
    while x != 0 and y != 0:
        digit1 = x % 10
        digit2 = y % 10
        if digit1 == digit2: return False
        else: 
            sumDigit1 += digit1 
            sumDigit2 += digit2
        x //= 10
        y //= 10
    
    if sumDigit1 == sumDigit2:
        return True
    else:
        return False

def integral(f, a, b, N):
    area = 0
    x1 = 0
    x2 = 0
    width = (b-a)/N
    for i in range(N):
         x1 = a + i*width 
         x2 = a + (i+1)*width
         area += (f(x1) + f(x2)) * width/2
    return area

#################################################
# Part B
#################################################
def findZeroWithBisection(f, x0, x1, epsilon):
    while (x1 - x0) > epsilon:
        xmid = (x0 + x1) / 2
        if almostEqual(f(xmid), 0, epsilon):
            return xmid
        elif f(xmid) * f(x0) > 0:
            x0 = xmid 
            # New range (xmid, x1)
        else: 
            #f(x0) and f(x1) have differnet signs 
            #so now f(xmid) and f(x1) have same sign
            x1 = xmid # New range (x0, xmid)
    return (x0 + x1) / 2
# Helper function for carrylessAdd


def carrylessAdd(x1, x2):
    ans = 0
    count = 0
    while x1 != 0 or x2 != 0:
        count += 1
        d1 = x1 % 10
        d2 = x2 % 10
        ans += ((d1 + d2) % 10) * 10**(count-1)
        x1 //= 10
        x2 //= 10
    return ans

#Helper function of nthSmithNumber():
def sumOfPrimeFactors(number):
    sum_factors_digits = 0
    # Check for the number of 2s that divide number
    while number % 2 == 0:
        sum_factors_digits += 2
        number //= 2
    # Check for odd number that divides number
    i = 3
    while i * i <= number:
        while number % i == 0:
            sum_factors_digits += sumOfDigits(i) 
            # Using sumOfDigits() for i since we can hanlde odd factor
            # like 11, 17
            number //= i
        i += 2
    # Final remaining prime factor 
    if number > 1:
        sum_factors_digits += sumOfDigits(number)
    return sum_factors_digits

def isSmithNumber(number):
    if isPrime(number):
        return False
    return sumOfDigits(number) == sumOfPrimeFactors(number)

def nthSmithNumber(n):
    #base 10, 
    #22=2^1*11^1, 2+2=2*1+(1+1)*1
    #4937775 = 3*5^2*65837, 4+9+3+7+7+7+5=3+5+5+(6+5+8+3+7) 
    #SmithNumber: non-prime number whose sum of digits are the sum of the 
    #digits of its prime factors (excuding 1)
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isSmithNumber(guess):
            found += 1
    return guess

import random
def testPlayPig():
    score = 0
    while True:
        userInput = input("Roll or Hold ? [roll/hold]: ").strip().lower()
        if userInput == 'roll':
            num = random.randint(1, 6)
            print(f"You rolled a {num}.")
            if num == 1:
                print("You rolled a 1! \
                Your turn is over and you score 0 points this turn.")
                return 0
            else:
                score += num
                if score == 100:
                    print('You win')
                print(f"Your current score this turn is: {score}")
        elif userInput == 'hold':
            print(f"You chose to hold. Your final score this turn is: {score}")
            return score
        else:
            print("Invalid input. Please type 'roll' or 'hold'.")
    #print('** Note: You need to manually test playPig()')

#################################################
# Bonus/Optional
#################################################
def makeBoard(moves):
    board = 0
    for i in range(moves):
        board += 8 * 10**i
    return board

def digitCount(n):
    n = abs(n)
    count = 0
    if n == 0: return 1
    while n != 0:
        n //= 10
        count += 1
    return count

def kthDigit(n, k):
    n = abs(n)
    #if k == 1
    for i in range(k):
        n //= 10
        if n == 0: return 0
    return n % 10

def replaceKthDigit(n, k, d):
    n += (d - kthDigit(n,k)) * 10 ** k
    return n

def getLeftmostDigit(n):
    return kthDigit(n, digitCount(n)-1)

def clearLeftmostDigit(n):
    return replaceKthDigit(n, digitCount(n)-1, 0)

def makeMove(board, position, move):
    lenBoard = digitCount(board)
    if move != 1 and move != 2:
        return "move must be 1 or 2!"
    elif position > lenBoard:
        return "offboard!"
    elif kthDigit(board, lenBoard - position) == 1 \
        or kthDigit(board, lenBoard - position) == 2:
        return "occupied!"

    return replaceKthDigit(board, lenBoard - position, move)

def isWin(board):
    while board >= 112:
        if (board // 10 ** (digitCount(board) - 3)) == 112:
            return True
        board = clearLeftmostDigit(board)
    return False

def isFull(board):
    digit = 0
    while board != 0:
        digit = board % 10
        if digit == 8: 
            return False
        else:
            board //= 10
    return True

def bonusPlay112(game):
    turn = 0
    boardSize = getLeftmostDigit(game)
    game = clearLeftmostDigit(game)
    gameSize = digitCount(game) // 2
    board = makeBoard(boardSize)
    boardNum = board
    
    for i in range(gameSize):
        position = getLeftmostDigit(game)
        game = clearLeftmostDigit(game)
        
        move = getLeftmostDigit(game)
        game = clearLeftmostDigit(game)
        
        turn += 1

        if isinstance(board, int):
            boardNum = board
        
        board = makeMove(board, position, move)

        if isinstance(board, str):
            if turn%2==0:
                return f"{boardNum}: Player 2: " + board
            else:
                return f"{boardNum}: Player 1: " + board
            
    if isWin(board):
        if turn%2==0:
                return f"{board}: Player 2 wins!"
        else:
            return f"{board}: Player 1 wins!"
    elif not isFull(board):
        return f"{board}: Unfinished!" 
    else:
        return f"{board}: Tie!"
        
def bonusCarrylessMultiply(x1, x2):
    x1, x2 = abs(x1), abs(x2)
    x2Digit = 0
    nthDigit = 0
    sumPerDigit = 0
    ans = 0 

    while x2 != 0:
        x2Digit = x2 % 10
        
        for i in range(x2Digit):
            sumPerDigit = carrylessAdd(sumPerDigit, x1)
        sumPerDigit *= 10 ** nthDigit
        
        nthDigit += 1
        ans = carrylessAdd(ans, sumPerDigit)
        sumPerDigit = 0
        
        x2 //= 10

    return ans

############################
# spicy bonus: integerDataStructures
############################
# Use normal Python integers to represent  
# lists, sets, maps, strings, and finite state machines

def intCat(n, m): 
    #Take two non-negative integers and 
    #return their concatenation
    if n == 0: return
    elif n is None: return m
    elif m is None: return n
    return n * (10 ** digitCount(m)) + m

def lengthEncode(value): 
    signDigit = 1 if value >= 0 else 2
    count = digitCount(value)
    countCount = digitCount(count)
    ans = ((intCat(signDigit, countCount)) * (10 ** countCount) + count) \
        * (10 ** count) + abs(value)
    return ans
def extractSubstring(s, e, value):
    lengthValue = digitCount(value)
    if s > lengthValue - 1 or e > lengthValue - 1:
        return 
    headPart = lengthValue - s
    tailPart = (lengthValue - 1) - e
    return (value % 10 ** headPart) // (10 ** tailPart)

def lengthDecode(encoding): 
    lenghEncoding = digitCount(encoding)
    neg = 1
    newLengthEncoding = lenghEncoding - 1
    sign = encoding // 10 ** newLengthEncoding
    if sign == 2: neg = -1
    encoding = encoding % 10 ** newLengthEncoding
    
    nonSignedEncoding = encoding + 10 ** newLengthEncoding
    
    num = None
    ans = None
    start = newLengthEncoding
    while num != 0:
        num = encoding % (10 ** start)
        if lengthEncode(num) == nonSignedEncoding:
            ans = neg * num
            break
        start -= 1  
    return ans

def lengthDecodeLeftmostValue(encoding): 
    encodingCopy = encoding
    lengthEncoding = digitCount(encodingCopy)
    # The number 4 is for the simplest case 1110
    lengthDecodeLeftmostValue = lengthEncoding - 4
    startNextValue = 4

    while True:
        encodedValue = encodingCopy // 10 ** lengthDecodeLeftmostValue
        decodedValue = lengthDecode(encodedValue)
        if isinstance(decodedValue, int):
            break
        lengthDecodeLeftmostValue -= 1
        startNextValue += 1

    nextValue = extractSubstring(startNextValue, lengthEncoding - 1, 
                                 encodingCopy)
    return (decodedValue, nextValue)

def clearDecodeLeftmostValue(encoding): 
    encodingCopy = encoding
    lengthEncoding = digitCount(encodingCopy)
    # The number 4 is for the simplest case 1110
    lengthDecodeLeftmostValue = lengthEncoding - 4
    startNextValue = 4

    while True:
        encodedValue = encodingCopy // 10 ** lengthDecodeLeftmostValue
        decodedValue = lengthDecode(encodedValue)
        if isinstance(decodedValue, int):
            break
        lengthDecodeLeftmostValue -= 1
        startNextValue += 1

    nextValue = extractSubstring(startNextValue, lengthEncoding - 1, 
                                 encodingCopy)
    return nextValue

def lengthDecodeLeftmostValue1(encoding): 
    lengthEncoding = digitCount(encoding)
    # The number 4 is for the simplest case 1110
    lengthDecodeLeftmostValue = lengthEncoding - 4

    while True:
        encodedValue = encoding // 10 ** lengthDecodeLeftmostValue
        decodedLeftmostValue = lengthDecode(encodedValue)
        if isinstance(decodedLeftmostValue, int):
            break
        lengthDecodeLeftmostValue -= 1

    return decodedLeftmostValue

def newIntList(): 
    # return empty list
    # an empty list is just a list of length 0
    return lengthEncode(0)

def intListLen(intList): 
    # takes a list, return its length (the leftmost encoded value)
    return lengthDecodeLeftmostValue1(intList)

def intListGet(intList, i):
    # Takes a list and an index
    # and returns the decoded value at that index
    inListCopy = intList
    error = 'index out of range'
    if intListLen(inListCopy) == 0: return error

    intListEncodeLength = digitCount(inListCopy)
    lengthEncodedPartition = 4
    # The number 4 is for the simplest case 1110
    count = 0
    # Start at 1 to skip intListLen
    i += 1
    
    while inListCopy != 0:

        intLeftMostEncode = inListCopy // \
              (10 ** (intListEncodeLength - lengthEncodedPartition))

        if lengthDecode(intLeftMostEncode) is None:
            lengthEncodedPartition += 1

        elif count == i:
            return lengthDecode(intLeftMostEncode)
        
        else:
            count += 1
            inListCopy %= 10 ** (intListEncodeLength - lengthEncodedPartition)
    return error

def intListSet(intList, i, value):
    """
    Takes a list and an index, returns a new list with the value at the given 
    index changed to be encoded.
    
    Args:
        intList (list of int): The list of integers.
        i (int): The index at which to update the value.
        value (int): The new value to be encoded to set at the specified index.
    
    Returns:
        list of int: A new encoded list 
        with the updated value or an error message if the index is out of range.
    """
    # Constants
    PARTITION_BASE = 10
    INITIAL_ENCODE_LENGTH = 4
    OUT_OF_RANGE_ERROR = 'index out of range'
    # To skip intListLen
    i = i + 1
    # Ensure index is within range
    intListLength = intListLen(intList)
    if intListLength == 0 or i > intListLength:
        return OUT_OF_RANGE_ERROR
    
    # Copy the list to avoid modifying the original
    intListCopy = intList
    intListEncodeLength = digitCount(intListCopy)
    lengthEncodedPartition = INITIAL_ENCODE_LENGTH
    count = 0
    ans = None

    while intListCopy != 0:
        # Extract left-most encoded segment
        intLeftMostEncode = intListCopy // \
            (PARTITION_BASE ** (intListEncodeLength - lengthEncodedPartition))

        if lengthDecode(intLeftMostEncode) is None:
            # Increase partition length if decoding fails
            lengthEncodedPartition += 1
        elif count == i:
            # Update the value at the specified index
            intListCopy %= PARTITION_BASE ** \
                (intListEncodeLength - lengthEncodedPartition)
            valueEncode = lengthEncode(value)
            if i == intListLength:
                ans = intCat(ans, valueEncode)
            else:
                ans = intCat(intCat(ans, valueEncode), intListCopy)
            return ans
        else:
            # Continue traversing the list
            count += 1
            ans = intCat(ans, intLeftMostEncode)
            intListCopy %= PARTITION_BASE ** \
                (intListEncodeLength - lengthEncodedPartition)
    
    return OUT_OF_RANGE_ERROR
def appendOrPop(intList, state):
    intEncodedListLen = digitCount(intList)
    intListLength = intListLen(intList)
    oldEncodedIntListLength = lengthEncode(intListLength)
    oldEncodedIntListLengthLen = digitCount(oldEncodedIntListLength)
    
    if state == 1:
        intListLength += 1
    elif state == -1:
        intListLength -= 1
    newEncodedIntListLength = lengthEncode(intListLength)

    withoutOldEncodeListLength = intEncodedListLen - oldEncodedIntListLengthLen
    intList %= 10 ** (withoutOldEncodeListLength)
    intList += newEncodedIntListLength * 10 ** withoutOldEncodeListLength
    return intList

def intListAppend(intList, value): 
    valueEncode = lengthEncode(value)
    return intCat(appendOrPop(intList, 1), valueEncode)

def intListPop(intList): 
    intListCopy = appendOrPop(intList, -1)
    # Constants
    PARTITION_BASE = 10
    INITIAL_ENCODE_LENGTH = 4
    NULL_ERROR = 'The list has nothing to pop!'

    intListLength = intListLen(intList)
    if intListLength == 0:
        return NULL_ERROR 

    lengthEncodedPartition = INITIAL_ENCODE_LENGTH
    
    while True:
        # Extract right-most encoded segment
        intRightMostEncode = intListCopy % \
            (PARTITION_BASE ** (lengthEncodedPartition))
        intRightMostDecode = lengthDecode(intRightMostEncode)
        if intRightMostDecode is None:
            # Increase partition length if decoding fails
            lengthEncodedPartition += 1
        else:
            break 
    
    intListCopy //= 10 ** lengthEncodedPartition
    return  intListCopy, intRightMostDecode

def newIntSet(): 
    return lengthEncode(0)

def intSetAdd(intSet, value): 
    
    if intSetContains(intSet, value):
        return intSet
    else:
        return intListAppend(intSet, value)
    
def intSetContains(intSet, value): 
    #valueEncode = lengthEncode(value)
    intSetLength = intListLen(intSet)
    for i in range(intSetLength):
        if value == intListGet(intSet, i):
            return True
    return False

def newIntMap(): 
    return lengthEncode(0)

def intMapGet(intMap, key): 
    intMapLength = intListLen(intMap)
    for i in range(intMapLength):
        if i == intMapLength - 1: break
        elif key == intListGet(intMap, i):
            return intListGet(intMap, i+1)
    return 'no such key'
def intMapContains(intMap,key):
    intMapLength = intListLen(intMap)
    for i in range(intMapLength):
        if i == intMapLength - 1: break
        elif key == intListGet(intMap, i):
            return True
    return False

def intMapSet(intMap, key, value): 
    intMapCopy = intMap
    intMapCopyCopy = None
    intMapLen = digitCount(intMapCopy)
    intMapLength = None
    encodeValue = lengthEncode(value)
    ans = None
    flagListLength = True
    flagKey = False
    
    # Constants
    PARTITION_BASE = 10
    INITIAL_ENCODE_LENGTH = 4

    while intMapLength != 0 and intMapCopy != 0:
        intEachEncode = intMapCopy // \
            (PARTITION_BASE ** (intMapLen - INITIAL_ENCODE_LENGTH))
        
        intEachDecode = lengthDecode(intEachEncode)
        
        if isinstance(intEachDecode, int):            
            intMapCopy %=  \
            (PARTITION_BASE ** (intMapLen - INITIAL_ENCODE_LENGTH))  
            
            if flagListLength:
                intMapLength = intEachDecode
                intMapLengthCopy = intMapLength
                ans = intCat(ans, intEachEncode)
                flagListLength = False
                if intMapCopy == 0:
                    intMapCopyCopy = None
                else: 
                    intMapCopyCopy = intMapCopy
            
            elif intEachDecode == key: 
                ans = intCat(ans, intEachEncode)
                ans = intCat(ans, encodeValue)
                flagKey = True
            
            elif flagKey:
                intMapCopy %=  \
                    (PARTITION_BASE ** (intMapLen - INITIAL_ENCODE_LENGTH))
                if intMapCopy == 0:
                    intMapCopy = None
                ans = intCat(ans, intMapCopy)
                return ans

            elif not flagListLength:
                ans = intCat(ans, intEachEncode)
                intMapLength -= 1
            
        else:
            INITIAL_ENCODE_LENGTH += 1

    ans = intCat(intCat(lengthEncode(intMapLengthCopy + 2), intMapCopyCopy), 
                  intCat(lengthEncode(key)
                  , encodeValue))
    return ans


def newIntFSM(): 
    # Return an empty FSM, 
    # empty map of transitions and an empty set ò accepting states
    # maps startState to yet another map, that second map 
    # mapping symbols (digit) to endStates
    '''
    We need to encode the numerous objects, such as maps and sets in lists, 
    in order to distinguish between individual values.
    '''
    intFSM = newIntList()
    intMap, intSet = newIntMap(), newIntMap()
    intFSM = intListAppend(intFSM, intMap)
    intFSM = intListAppend(intFSM, intSet)
    return intFSM

def isAcceptingState(fsm, state): 
    fsmCopy = fsm
    mapAndState = clearDecodeLeftmostValue(fsmCopy)
    stateSet = clearDecodeLeftmostValue(mapAndState)
    decodeStateSet = lengthDecode(stateSet)
    # To clear encode length of it
    decodeStateSet = clearDecodeLeftmostValue(decodeStateSet) 

    while decodeStateSet:
        (value, decodeStateSet) = lengthDecodeLeftmostValue(decodeStateSet)
        if value == state:
            return True
    return False

def addAcceptingState(fsm, state): 
    fsmCopy = fsm
    (decodeLength, mapState) = lengthDecodeLeftmostValue(fsmCopy)
    (decodeMap, stateSet) = \
        lengthDecodeLeftmostValue(mapState)
    encodeLength = lengthEncode(decodeLength)
    encodeMap = lengthEncode(decodeMap)
    
    decodeStateSet = lengthDecode(stateSet)
    return intCat(encodeLength, intCat(encodeMap, \
                            lengthEncode(intSetAdd(decodeStateSet, state))))

def setTransition(fsm, fromState, digit, toState): 
    # Update two maps
    # Outer map: mapping each fromState to its own map
    # Inner map: mapping each digits to its toState
    fsmCopy = fsm
    mapAndState = clearDecodeLeftmostValue(fsmCopy)
    (decodeMap, stateSet) = lengthDecodeLeftmostValue(mapAndState)
    #print(decodeMap, stateSet)
    # Constant
    MAP_LENGTH = 1112

    if intMapContains(decodeMap, fromState):
        digitMap = intMapGet(decodeMap, fromState)
        #print(digitMap)
        digitMap = intMapSet(digitMap, digit, toState)
        #print(digitMap)
    else:
        digitMap = intCat(MAP_LENGTH, \
                      (intCat(lengthEncode(digit),lengthEncode(toState))))
        #print(digitMap)

    decodeMap = intMapSet(decodeMap, fromState, digitMap)
    #print(decodeMap)
    ans = intCat(intCat(MAP_LENGTH, lengthEncode(decodeMap)), stateSet)
    #print(ans)
    return ans

def getTransition(fsm, fromState, digit): 
    fsmCopy = fsm
    mapAndState = clearDecodeLeftmostValue(fsmCopy)
    (decodeMap, stateSet) = lengthDecodeLeftmostValue(mapAndState)
    fromStateValueCheck = intMapContains(decodeMap, fromState)
    if fromStateValueCheck == False:
        return 'no such transition'
    else:
        innerMap = intMapGet(decodeMap, fromState)
        innerMapCheck = intMapContains(innerMap, digit)
        if innerMapCheck:
            return intMapGet(innerMap, digit)
        else:
            return 'no such transition'

def accepts(fsm, inputValue): 
    fromState = 1
    runtime = digitCount(inputValue)
    step = None
    
    for i in range(runtime):
        step = inputValue // 10 ** ((runtime - 1) - i)
        inputValue %= 10 ** ((runtime - 1) - i) 
        toState = getTransition(fsm, fromState, step)
        fromState = toState

    if isAcceptingState(fsm, toState):
        return True
    else:
        return False

def states(fsm, inputValue): 
    ans = newIntList()
    fromState = 1
    ans = intListAppend(ans, fromState)
    runtime = digitCount(inputValue)
    step = None
    
    for i in range(runtime):
        step = inputValue // 10 ** ((runtime - 1) - i)
        inputValue %= 10 ** ((runtime - 1) - i) 
        toState = getTransition(fsm, fromState, step)
        ans = intListAppend(ans, toState)
        fromState = toState

    if isAcceptingState(fsm, toState):
        return ans
    else:
        return 

def encodeString(s): 
    stringLength = 0
    ans = None
    for char in s:
        stringLength += 1
        ans = intCat(ans, lengthEncode(ord(char)))
    return intCat(lengthEncode(stringLength), ans)         

def decodeString(intList):
    intListCopy = intList
    intListLen = digitCount(intListCopy)
    intStringLength = 0
    ans = ''
    count = 0
    flagListLength = True
    # Constants
    PARTITION_BASE = 10
    INITIAL_ENCODE_LENGTH = 4
    OUT_OF_RANGE_ERROR = 'index out of range'
    
    while intListCopy != 0:
        
        intEachEncode = intListCopy // \
            (PARTITION_BASE ** (intListLen - INITIAL_ENCODE_LENGTH))
        
        intEachDecode = lengthDecode(intEachEncode)
        
        if isinstance(intEachDecode, int):
            if flagListLength:
                intStringLength = intEachDecode
                flagListLength = False
            elif isinstance(chr(intEachDecode), str): 
                ans += chr(intEachDecode)
                count += 1
                if count == intStringLength:
                    return ans
            intListCopy %=  \
            (PARTITION_BASE ** (intListLen - INITIAL_ENCODE_LENGTH))
        else:
            INITIAL_ENCODE_LENGTH += 1

    return OUT_OF_RANGE_ERROR

    #the function will be developed later
#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed!')

def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed!')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed!')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(2) == 5)
    assert(nthAdditivePrime(3) == 7)
    assert(nthAdditivePrime(4) == 11)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed!')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed!')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    '''
    def f1(x): return 10 - x**2 
    x = findZeroWithBisection(f1, -2, 5, 0.000000001)
    assert(almostEqual(x, 3.25)) 
    '''
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    
    print('Passed!')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed!')

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed!')

def testMakeBoard():
    print('Testing testMakeBoard()...', end='')
    assert(makeBoard(1)==8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)
    print('Passed!')

def testDigitCount():
    print('Testing testDigitCount()...', end='')
    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)
    print('Passed!')

def testKthDigit():
    print('Testing testKthDigit()...', end='')
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print('Passed!')

def testReplaceKthDigit():
    print('Testing testRepaceKthDigit()....', end='')
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    print('Passed!')

def testGetleftMostdigit():
    print('Testing testGetleftMostdigit()...', end='')
    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)
    print('Passed!')

def testClearleftMostdigit():
    print('Testing testClearleftMostdigit()...', end='')
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    assert(clearLeftmostDigit(60789) == 789)
    print('Passed!')   

def testMakemove():
    print('Testing makeMove()...', end='')
    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")
    print('Passed!')

def testIswin():
    print('Testing isWin()...', end='')
    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)
    print('Passed!')

def testIsfull():
    print('Testing isFull()...', end='')
    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)
    print("Passed!")

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

# Integer Data Structures
def testIntCat():
    print('Testing testIntCat()...', end='')
    assert(intCat(123, 45) == 12345)
    assert(intCat(123, 1005) == 1231005)
    assert(intCat(123, 0) == 1230)
    assert(intCat(123, 10) == 12310)
    assert(intCat(100, 10) == 10010)
    assert(intCat(100, 0) == 1000)
    assert(intCat(0, 45) is None)
    print('Passed!')

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testExtractSubstring():
    print('Testing extractSubstring()...', end='')
    assert(extractSubstring(2, 4, 1511242) == 112)
    assert(extractSubstring(3, 4, 1511242) == 12)
    assert(extractSubstring(3, 5, 1511242) == 124)
    assert(extractSubstring(2, 5, 1511242) == 1124)
    assert(extractSubstring(2, 4, 15112422) == 112)
    assert(extractSubstring(3, 4, 15112422) == 12)
    assert(extractSubstring(3, 5, 15112422) == 124)
    assert(extractSubstring(2, 5, 15112422) == 1124)
    assert(extractSubstring(0, 4, 1511242) == 15112)
    assert(extractSubstring(0, 0, 1511242) == 1)
    assert(extractSubstring(2, 4, 1230) is None)
    assert(extractSubstring(2, 4, 1511000) == 110)
    assert(extractSubstring(2, 4, 15110000) == 110)
    assert(extractSubstring(5, 7, 15110000) == 0)
    assert(extractSubstring(0, 4, 15110) == 15110)
    print("Passed!")

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')
def testIntListGet():
    print('Testing intListGet()...', end='')
    a1 = 111111242
    a2 = 111211191148888
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a2, 0) == 9)
    assert(intListGet(a2, 1) == 8888)
    assert(intListGet(a1, 1) == 'index out of range')
    print('Passed!')

def testIntListSet():
    print('Testing intListSet()...', end='')
    a1 = 111111242
    a2 = 111211191148888
    a3 = 1113111121191148888
    assert(intListSet(a1, 0, 567) == 1111113567)
    a1 = 111111242
    assert(intListSet(a1, 1, 567) == 'index out of range')
    assert(intListSet(a2, 1, 567) == 11121119113567)
    a2 = 111211191148888
    assert(intListSet(a2, 0, 567) == 11121135671148888)
    a2 = 111211191148888
    assert(intListSet(a2, 0, 0) == 111211101148888)
    a2 = 111211191148888
    assert(intListSet(a2, 1, 0) == 111211191110)    
    assert(intListSet(a3, 1, 9) == 1113111111191148888)    
    a3 = 1113111121191148888
    assert(intListSet(a3, 2, -2) == 1113111121192112)    
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length = 0, list = []
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # length = 1, list = [42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # length = 1, list = [567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # length = 2, list = [9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # length = 1, list = [9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # length = 0
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # length = 0
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # length = 2, map = [42, 73]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # length = 2, map = [42, 98765]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # length = 4, 
                                            # map = [42, 98765, 99, 0]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3) # At state 1, receive 8, move to state 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # length = 3, list = [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # length = 4, 
                                                     # list = [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # length = 1, str = [65]
    assert(encodeString('f') == 1111113102) # length = 1, str = [102]
    assert(encodeString('3') == 111111251) # length = 1, str = [51]
    assert(encodeString('!') == 111111233) # length = 1, str = [33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # length = 4, 
                                                          # str = [65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    #testDigitCount()
    #testGcd()   
    #testHasConsecutiveDigits()   
    #testNthAdditivePrime()   
    #testMostFrequentDigit()
    #testIsRotation()
    #testIntegral()

    # Part B:
    #testFindZeroWithBisection()
    #testCarrylessAdd()
    #testNthSmithNumber()
    #testMakeBoard()
    #testDigitCount()
    #testKthDigit()
    #testReplaceKthDigit()
    #testGetleftMostdigit()
    #testClearleftMostdigit()
    #testMakemove()
    #testIswin()
    #testIsfull()

    #testPlayPig()

    # Bonus:
    #testBonusPlay112()
    #testBonusCarrylessMultiply()
    #testIntCat()
    #testLengthEncode()
    #testExtractSubstring()
    #testLengthDecode()
    #testLengthDecodeLeftmostValue()
    #testIntListGet()
    #testIntListSet()
    #testIntList()
    #testIntSet()
    testIntegerDataStructures()
    #testEncodeDecodeStrings()
    #testIntMap()
    #testIntFSM()
    #testAccepts()
def main():
    cs112_s22_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
