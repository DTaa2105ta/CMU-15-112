"""
# A set is a data structure that can hold multiple elements in no particular order 
# We can not index into it, but we can iterate over it
s = set([2,3,5])
print(3 in s)
print(4 in s)
for x in range(7):
	if (x not in s):
		print(x)

# Creating Sets
## Create an empty set 
s = set()
print(s)
## Create a set from a list
s = set(["cat", "cow", "dog"])
print(s)
## Create a statically-allocated set
s = {2, 3, 5}
print(s)
## Caution: {} is not empty set
s = {}
print(type(s) == set) # False
print(type(s)) # This is a dict 

# Using Sets
## Sets can do many of the same things as lists and tuple 
s = set([1, 2, 3])
print(len(s))
print(2 in s)
print(4 in s)
print(4 not in s)
print(2 not in s)
## use add instead of append to add an element to a set
s.add(7)
s.remove(3)

for item in s:
	print(item)

# Properties of Sets
## ! Sets are unordered
### Elements may be arranged in a different order order than they are provided
### and we cannot index into a set
s = set([2, 4, 8])
print(s)
for element in s:
	print(element)
## ! Elements are unique
s = set([2, 2, 2])
print(s)
print(len(s))
## ! Elements must be immmutable
### Sets can only hold elements that are immutable (cannot be changed)
### such as numbers, boolean, strings, and tuples
a = ["lists", "are", "mutable"]
s = set([a]) #TypeError: unhashable typpe: 'list'
print(s)
s1 = set(["sets", "are", "mutable", "too"])
s2 = set([s1])     # TypeError: unhashable type: 'set'
print(s2)
## ! Sets are very efficient
### The whole point of having sets is because they are are very efficient, in fact O(1), for most common operations including 
### adding elements, removing elements, and checking for membership
"""
# How sets work: HASHINGGG
## Return the same INTEGER for the same any input values
"""
### How sets are faster than lists is shown below:
# 0. Preliminaries
import time
n = 1000

# 1. Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2,n+1,2))

print("Using a list... ", end="")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1
end = time.time()
elapsed1 = end - start
print(f'count={count} and time = {elapsed1:0.5f} seconds')

# 2. Repeat, using a set
print("Using a set.... ", end="")
start = time.time()
s = set(a)
count = 0
for x in range(n+1):
    if x in s:
        count += 1
end = time.time()
elapsed2 = end - start
print(f'count={count} and time = {elapsed2:0.5f} seconds')
print(f'At n={n}, sets ran ~{elapsed1/elapsed2:0.1f} times faster than lists!')
print("Try a larger n to see an even greater savings!")
"""
# Some worked examples using sets
## isPermutation(L)
def isPermutation(L):
    # return True if L is a permutation of [0,...,n-1]
    # and False otherwise
    return (set(L) == set(range(len(L))))

def testIsPermutation():
    print("Testing isPermutation()...", end="")
    assert(isPermutation([0,2,1,4,3]) == True)
    assert(isPermutation([1,3,0,4,2]) == True)
    assert(isPermutation([1,3,5,4,2]) == False)
    assert(isPermutation([1,4,0,4,2]) == False)
    print("Passed!")

testIsPermutation()
## repeat(L)
def repeats(L):
    # return a sorted list of the repeat elements in the list L
    seen = set()
    seenAgain = set()
    for element in L:
        if (element in seen):
            seenAgain.add(element)
        seen.add(element)
    return sorted(seenAgain)

def testRepeats():
    print("Testing repeats()...", end="")
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))
    print("Passed!")

testRepeats()