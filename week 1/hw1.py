#################################################
# hw1.py
# name:
# andrew id:
#################################################

import cs112_s22_week1_linter
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

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if d == abs(r1 - r2) or d <= (r1 + r2):
        return True
    return False 

def getInRange(x, bound1, bound2):
    if  bound1 > bound2:
        bound1, bound2 = bound2, bound1
    
    if x < bound1:
        return bound1
    elif bound1 <= x <= bound2:
        return x
    else:
        return bound2

def eggCartons(eggs):
    if eggs % 12 == 0:
        return eggs // 12
    else:
        return eggs // 12 + 1

def pascalsTriangleValue(row, col):
    if row < 0 or col < 0 or col > row:
        return 
    return (math.factorial(row))/(math.factorial(row-col) * math.factorial(col))

def getKthDigit(n, k):
    n = abs(n) % (10**(k+1))
    if n < 10**k:
        return 0
    else:
        return n // (10**k)
 
def setKthDigit(n, k, d):
    if n < 0:
        nev = True
    else: 
        nev = False
    
    n = abs(n)
    old_KthDigit = getKthDigit(n, k)
    n += 10**(k) * (d - old_KthDigit)
    
    if nev:
        return (-1) * n
    else:
        return n 

#################################################
# Part B
#################################################
        
def nearestOdd(n):
    left = (n - 1) // 1
    right = (n + 1) // 1
    if left % 2 == 0 and right % 2 == 0:
        return int((n // 1))
    elif n % 1 == 0:
        return int(left)
    else:
        return int(right)

def numberOfPoolBalls(rows):

    return rows*(rows + 1)/2

def numberOfPoolBallRows(balls):
    '''if balls == 0:
        return 0'''
    sol = (((1 + 8 * balls)**(1/2) - 1)/2)
    r = roundHalfUp(sol) 
    if r < sol:
        return r + 1
    else:
        return r

def d1rgb(rgb):
    return rgb // (10**6)
def d3rgb(rgb):
    return rgb % (10**3)
def d2rgb(rgb):
    return (rgb - d1rgb(rgb)*(10**6) - d3rgb(rgb)) // (10**3)
def calculate(drgb1, drgb2, midpoints, n):
    
    digit_diff = drgb1 - drgb2
    space = abs(digit_diff) / (midpoints + 1)
    remainder = abs(digit_diff) % (midpoints + 1)
    r = roundHalfUp(space)

    if remainder <= (midpoints + 1)//2:
        if math.floor(n/2) <= remainder:
            if digit_diff < 0:
                drgb1 += r * n + math.floor(n/2)
            else:
                drgb1 -= r * n + math.floor(n/2)
            return drgb1
        else:
            if digit_diff < 0:
                drgb1 += r * n + remainder
            else:
                drgb1 -= r * n + remainder
            return drgb1
    else:
        if math.floor(n/2) <= ((midpoints + 1)-remainder):
            if digit_diff < 0:
                drgb1 += r * n - math.floor(n/2)
            else:
                drgb1 -= r * n - math.floor(n/2)
            return drgb1
        else:
            if digit_diff < 0:
                drgb1 += r * n - ((midpoints + 1)-remainder)
            else:
                drgb1 -= r * n - ((midpoints + 1)-remainder)
            return drgb1

def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > midpoints + 1:
        return 
    d1 = calculate(d1rgb(rgb1), d1rgb(rgb2), midpoints, n) * 10**6
    d2 = calculate(d2rgb(rgb1), d2rgb(rgb2), midpoints, n) * 10**3 
    d3 = calculate(d3rgb(rgb1), d3rgb(rgb2), midpoints, n)
    return d1 + d2 + d3
#################################################
# Bonus/Optional
#################################################

def handToDice(hand):
    return (getKthDigit(hand,2),getKthDigit(hand,1),getKthDigit(hand,0))

def diceToOrderedHand(a, b, c):
    maxd = max(a,b,c)
    mind = min(a,b,c)
    median = (a+b+c) - maxd - mind
    return maxd*10**2 + median*10 + mind

def playStep2(hand, dice):
    diceForHand = handToDice(hand)
    maxd = max(diceForHand)
    mind = min(diceForHand)
    median = sum(diceForHand) - maxd - mind
    if maxd == mind: 
        return (hand, dice)
    elif median == maxd:
        return (diceToOrderedHand(maxd, maxd, dice%10), dice//10)
    elif median == mind:
        return (diceToOrderedHand(mind, mind, dice%10), dice//10)
    else:
        return (diceToOrderedHand(maxd, (dice%10**2)//10, dice%10), dice//10**2)
    
def score(hand):
    diceForHand = handToDice(hand)
    maxd = max(diceForHand)
    mind = min(diceForHand)
    median = sum(diceForHand) - maxd - mind
    if maxd == mind: 
        return 20 + maxd * 3
    elif median == maxd or median == mind:
        return 10 + median * 2
    else:
        return maxd
    
def bonusPlayThreeDiceYahtzee(dice):
    hand = dice % 10**3
    dice //= 10**3
    (hand1,dice1) = playStep2(hand, dice)

    if hand1 == hand:
        return (hand1, score(hand1))
    (hand2, dice2) = playStep2(hand1, dice1)
    return (hand2, score(hand2))

def bonusFindIntRootsOfCubic(a, b, c, d):
    #Guaranteed the function has 3 real roots (HERE, all integers)
    p = -b/(3*a) 
    q = p**3 + (b*c-3*a*d)/(6*a**2)
    r = c/(3*a)
    x1  = (q + (q**2 + (r-p**2)**3)**(1/2))**(1/3) \
        + (q - (q**2 + (r-p**2)**3)**(1/2))**(1/3) + p
    
    x1 = x1.real
    x1 = int(x1)
    discrimination = (b**2 - 4*a*c - 2*a*b*x1 - 3 * a**2 * x1**2)**(1/2)
    x2 = int(((-b-x1*a + discrimination) / 2*a).real)
    x3 = int(((-b-x1*a - discrimination) / 2*a).real)
    r1 =  min(x1,x2,x3)
    r3 = max(x1,x2,x3)
    r2 = (x1+x2+x3) - r1 - r3
    return r1, r2, r3
#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    # Part B:
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    testBonusPlayThreeDiceYahtzee()
    #testBonusFindIntRootsOfCubic()

def main():
    cs112_s22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
