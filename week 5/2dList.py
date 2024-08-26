#1 Creating 2d Lists
## Static Allocation 
### Create a 2d list with fixed values 
a = [[2,3,4],[5,6,7]]
print(a)

## Dynamic (Variable-Length) Allocation
### Wrong: Cannot use * (Shallow Copy)
rows = 3
cols = 2
a = [[0] * cols] * rows # Error: creates shallow copy
                        # Creates one unique row, the rest are aliases!!

print("This SEEMS ok. At first:")
print("a =", a) # a = [[0,0],[0,0],[0,0]]
a[0][0] = 42
print("But see what happens after a[0][0]=42")
print("a =", a) # a = [[42,0],[42,0],[42,0]]

'''
[[0] * cols] * rows: creates a list where each sublist (row) is a 
reference to the same list object [[0] * cols]. 
Therefore, modifying one sublist a[0][0] will afect all sublist.
'''
### Right: Append each row
a = []
for row in range(rows):
    a += [[0]*cols]
print("This is OK. At first:")
print("a =", a) # a = [[0, 0], [0, 0], [0, 0]]
a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("a =", a) # a = [[42, 0], [0, 0], [0, 0]]
### Another good option: use a list comprehension
a = [([0]*cols) for row in range(rows)]
print("This is ok. At first:")
print("a =", a) # a = [[0, 0], [0, 0], [0, 0]]
a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("a =", a) # a = [[42, 0], [0, 0], [0, 0]]
### Best option: make2dList()
def make2dList(rows, cols):
    return [([0] * cols) for row in range(rows)]

rows = 3
cols = 2

a = make2dList(rows, cols)
print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)

#2 Getting 2d List Dimensions
# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("a = ", a)
# Find its dimensions
rows = len(a)
cols = len(a[0])
print("rows =", rows)
print("cols =", cols)

#3 Copying and Aliasing 2d Lists
## Wrong cannot use copy.copy (shallow copy)
import copy
# Create a 2d list
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
# Try to copy it 
b = copy.copy(a) #Error: creates shallow copy
# At first, things seem ok
print("At first...")
print("   a =", a) # a = [[1, 2, 3], [4, 5, 6]]
print("   b =", b) # b = [[1, 2, 3], [4, 5, 6]] 

# Now modify a[0][0]
a[0][0] = 9
print("But after a[0][0] = 9")
print("   a =", a) # a = [[9, 2, 3], [4, 5, 6]]
print("   b =", b) # b = [[9, 2, 3], [4, 5, 6]]
## Right: use copy.deepcopy
import copy
# Create a 2d list
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
# Try to copy it 
b = copy.deepcopy(a) # correct
# At first, things seem ok
print("At first...")
print("   a =", a) # a = [[1, 2, 3], [4, 5, 6]]
print("   b =", b) # b = [[1, 2, 3], [4, 5, 6]] 

# Now modify a[0][0]
a[0][0] = 9
print("And after a[0][0] = 9")
print("   a =", a) # a = [[9, 2, 3], [4, 5, 6]]
print("   b =", b) # b = [[1, 2, 3], [4, 5, 6]] 
"""
copy.deepcopy creates a new list and also recursively creates new copies of
all objects found in the original list. This means that all objects are all copied perfectly(we will see in next section), 
not just outer list 
Changes to the objects in the original list do not affect the objects in the deep copy
because they are completely independent.
"""

##Limitations of copy.deepcopy
a = [[0]*2]*3 # makes 3 shallow copies of (aliases of) the same row
a[0][0] = 42  # appears to modify all 3 rows
print(a)      # prints [[42, 0], [42, 0], [42, 0]]

# now do it again with a deepcopy

import copy
a = [[0]*2]*3        # makes 3 shallow copies of the same row
a = copy.deepcopy(a) # meant to make each row distinct
a[0][0] = 42         # so we hope this only modifies first row
print(a)             # STILL prints [[42, 0], [42, 0], [42, 0]]

# deepcopy preserves any already-existing aliases perfectly!
# best answer: don't create aliases in the first place, unless you want them.

##Advanced: alias-breaking deepcopy
def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a] 
    else:
        return copy.copy(a)
a = [[0]*2]*3     # makes 3 shallow copies of the same row
a = myDeepCopy(a) # once again, meant to make each row distinct
a[0][0] = 42      # so we hope this only modifies first row
print(a)          # finally, prints [[42, 0], [0, 0], [0, 0]]

#4 Printing 2d list
## Basic version:
#Here are two helpful fucntions:
def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def print2dList(L):
    print(repr2dList(L))

#######################################

# Let's give the new function a try!
L = [ [ 1, 23, 'a' ] , [ 4, 5, 6789, 10, 100 ] ]

assert(repr2dList(L) == '''\
[
 [ 1, 23,  'a'          ],
 [ 4,  5, 6789, 10, 100 ]
]''')

print2dList(L)

## Fancy Version
# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            maxLen = max(maxLen, len(repr(a[row][col])))
    return maxLen

def print2dList(a):
    if a == []:
        print([])
        return
    print()
    rows, cols = len(a), len(a[0])
    maxCols = max([len(row) for row in a])
    fieldWidth = max(maxItemLength(a), len(f'col={maxCols-1}'))
    rowLabelSize = 5 + len(str(rows-1))
    rowPrefix = ' '*rowLabelSize+' '
    rowSeparator = rowPrefix + '|' + ('-'*(fieldWidth+3) + '|')*maxCols
    print(rowPrefix, end='  ')
    # Prints the column labels centered
    for col in range(maxCols):
        print(f'col={col}'.center(fieldWidth+2), end='  ')
    print('\n' + rowSeparator)
    for row in range(rows):
        # Prints the row labels
        print(f'row={row}'.center(rowLabelSize), end=' | ')
        # Prints each item of the row flushed-right but the same width
        for col in range(len(a[row])):
            print(repr(a[row][col]).center(fieldWidth+1), end=' | ')
        # Prints out missing cells in each column in case the list is ragged
        missingCellChar = chr(10006)
        for col in range(len(a[row]), maxCols):
            print(missingCellChar*(fieldWidth+1), end=' | ')
        print('\n' + rowSeparator)
    print()

# Let's give the new function a try!
a = [ [ 1, -1023, 3 ] , [ 4, 5, 678 ] ]
b = [ [123, 4567, 891011], [567890, 'ABC'], ['Amazing!', True, '', -3.14, None]]
print2dList(a)
print2dList(b)

#5. Nested Looping over 2d List

# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("Before: a =", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])

# And now loop over every element
# Here, we'll add one to each element,
# just to make a change we can easily see
for row in range(rows):
    for col in range(cols):
        # This code will be run rows*cols times, once for each
        # element in the 2d list
        a[row][col] += 1

# Finally, print the results
print("After:  a =", a)

#6. Accessing 2d lists bt row or column
## Accessing a whole row
a = [[1,2,3], [4,5,6]]
row = 1
rowList = a[row]
print(rowList)
## Accessing a whole column
col = 1
colList = [ ]
for i in range(len(a)):
    colList += [a[i][col]]
print(colList)
## Accessing a whole column with a list comprehension
a = [[1,2,3], [4,5,6]]
col = 1
colList = [a[i][col] for i in range(len(a))]
print(colList)

#7 Non-Rectangular ("Ragged") 2d Lists
# 2d lists do not have to be rectangular
a = [ [ 1, 2, 3 ] ,
      [ 4, 5 ],
      [ 6 ],
      [ 7, 8, 9, 10 ] ]

rows = len(a)
for row in range(rows):
    cols = len(a[row]) # now cols depends on each row
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(a[row][col], " ", end="")
    print()

#8 3d lists
# 2d lists do not really exist in Python.
# They are just lists that happen to contain other lists as elements.
# And so this can be done for "3d lists", or even "4d" or higher-dimensional lists.
# And these can also be non-rectangular, of course!

a = [ [ [ 1, 2 ],
        [ 3, 4 ] ],
      [ [ 5, 6, 7 ],
        [ 8, 9 ] ],
      [ [ 10 ] ] ]

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(f'a[{i}][{j}][{k}] = {a[i][j][k]}')