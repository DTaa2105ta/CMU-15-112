#1
##  for loops and range
# A for loop repeats an action a specific number of times based on the provided range
'''
def sumFromMtoN(m, n):
    total = 0
    # note that range(x,y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total 
print(sumFromMtoN(5,10) == 5+6+7+8+9+10)


### Actually, we dont need a loop here...
def sumFromMToN(m, n):
    return sum(range(m, n+1))
print(sumFromMToN(5, 10) == 5+6+7+8+9+10)


def sumToN(n):
    # helper function 
    return n*(n+1)//2

def sumFromToN_byFormula(m, n):
    return (sumToN(n) - sumToN(m-1))

print(sumFromToN_byFormula(5, 10) == 5+6+7+8+9+10)

'''

'''
### What if we omit the first parameter?
def sumToN(n):
    total = 0
    # range defaults the staring number to 0
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)

### What if we add a third parameter?
def sumEveryKthFromMtoN(m, n, k):
    total = 0
    # the third parameter becomes a step
    for x in range(m ,n+1, k):
        total += x
    return total 
print(sumEveryKthFromMtoN(5, 20, 7)== (5 + 12 + 19))

### Sum just odd numbers from m to n 
def sumOfOddsFromMtoN(m, n):
    total = 0
    for x in range(m, n+1):
        if (x%2 ==1):
            total += x
    return total 
    
print(sumOfOddsFromMtoN(4,10) == sumOfOddsFromMtoN(5, 9) == (5+7+9))

### Do it backward!
# Here we will range in reverse
# (not wise in this case, but instructional)
def sumOfOddsFromMtoN(m, n):
    total = 0
    for x  in range(n, m-1, -1):
        if (x%2==1):
            total += x
    return total
print(sumOfOddsFromMtoN(4,10) == sumOfOddsFromMtoN(5,9) == (5+7+9))
'''
'''
#2
## nested for loops
### We can put loops inside of loops to repeat actions at multiple levels
def printCoordinates(xMax, yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print("(", x, ",", y, ") ", end="")
        print()
printCoordinates(4,5)

##How about some stars?
def printStarRectangle(n):
    # print an nxn rectangle of asterisks
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()
printStarRectangle(5)

def printMysteryStarShape(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()

printMysteryStarShape(5)
'''
'''
#3
##while loops
### use while loops when there is an inderminate number of iterations
def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n
print(leftmostDigit(7257818581859) == 7)

### Example: nth non-negative integer with some property
#### eg: find the nth number that is a multiple of either 4 or 7
def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)

def nthMultipleOf4or7(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end="")
print()

### misuse; while loop over a fixed range
#sum numbers from 1 to 10
#note: this works, but you should not use "while" here
# instead, do this with "for" 
def sumToN(n):
    # note: even though this works, it is bad style
    # you should  do this with a "for" loop, not a "while" loop
    total = 0
    counter = 1
    while (counter <= n):
        total += counter
        counter += 1
    return total

print(sumToN(5) == 1+2+3+4+5)
'''
'''
#4
## break and continue
#continue, break, and pass are three keywords used in loops
#in order to change the program flow
for n in range(200):
    if (n%3==0):
        continue #skips rest of this pass
    elif (n==8):
        break #skips rest of  entire loop
    else:
        pass #does nothing! pass is a placeholder, not needed here
    print(n, end=" ")
print()
#Infinite "while" loop with break 
##Note, this is advanced content, as it uses strings
def readUntilDone():
    linesEntered = 0
    while (True):
        response = input("Enter a string (or 'done' to quit): ")
        if response == "done":
            break
        print("  You entered:  ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered

linesEntered = readUntilDone()
print("You entered", linesEntered, "lines (not counting 'done').")
'''

#5
#isPrime
# Note: there are faster/better ways. We're just going for clarity and simplicity here
def isPrime(n):
    if (n<2):
        return False
    for factor in range(2,n):
        if (n%factor == 0):
            return False
    return True
# and take it for a spin 
for n in range(100):
    if isPrime(n):
        print(n, end=" ")
print()

#fasterisPrime
def fasterIsPrime(n):
    if (n<2):
        return False
    if (n==2):
        return True
    if (n%2==0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n % factor ==0):
            return False
    return True
'''# And try out thí version
for n in range(100):
    if fasterIsPrime(n):
        print(n, end=" ")
print()
'''

## Verify these are the same 
for n in range(100):
    assert(isPrime(n) == fasterIsPrime(n))
print("They seem to work the same!")


### Now let's see if we really sped things up
'''import time
bigPrime = 499
print("Timing isPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", isPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1-time0)*1000, "ms")

print("Timing fasterIsPrime(", bigPrime, ")", end=" ")
time0 = time.time()
print(", returns ", fasterIsPrime(bigPrime), end=" ")
time1 = time.time()
print(", time = ", (time1 - time0)*1000, "ms")'''

#6
## nthPrime
def isPrime(n):
    if (n<2):
        return False
    if (n==2):
        return True
    if (n%2 ==0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n%factor ==0):
            return False
    return True

def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

for n in range(10):
    print(n, nthPrime(n))
print("Done!")
print(nthPrime(5))
