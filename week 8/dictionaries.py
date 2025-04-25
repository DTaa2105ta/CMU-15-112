# A dictionary is a data structure that maps keys to values in the same way
# that a list maps indexes to values. Howerver, keys can be any immutable value
"""
stateMap = { 'pittsburgh':'PA', 'chicago':'IL', 'seattle':'WA', 'boston':'MA' }
city = input("Enter a city name --> ").lower()
if (city in stateMap):
    print(city.title(), "is in", stateMap[city])
else:
    print("Sorry, never heard of it.")
"""
"""
counts = dict()
while True:
    n = int(input("Enter an integer (0 to end) --> "))
    if (n == 0): break
    if (n in counts):
        counts[n] += 1
    else:
        counts[n] = 1
    print("I have seen", n, "a total of", counts[n], "time(s)")
print("Done, counts:", counts)

"""
# Creating dictionaries
## Create an empty dictionary
d = dict()
print(d)

d = {}
print(d)
## Create a dictionary from a list of (key, value) pairs
pairs = [("cow", 5), ("dog", 98), ("cat", 1)]
d = dict(pairs)
print(d) 
## Statically-allocated dictionary
d = { "cow":5, "dog":98, "cat":1 }
print(d)

# We can interact with dictionaries in a similar way to lists/sets
d = { "a" : 1, "b" : 2, "c" : 3 }

print(len(d)) # prints 3, the number of key-value pairs

print("a" in d) # prints True
print(2 in d) # prints False - we check the keys, not the values
print(2 not in d) # prints True
print("a" not in d) # prints False

print(d["a"]) # finds the value associated with the given key. Crashes if the key is not in d
print(d.get("z", 42)) # finds the value of the key if the key is in the dictionary,
# or returns the second (default) value if the key is not in d

d["e"] = "wow" # adds a new key-value pair to the dictionary, or updates the value of a current key
del d["e"] # removes the key-value pair specified from the dictionary. Crashes if the key is not in d

for key in d:
    print(key, d[key]) # we can iterate over the keys, then print out the keys or corresponding values

# Properties of dictionaries
## Dictionaries amap keys to values
ages = dict()
key = "fred"
value = 38
ages[key] = value  # "fred" is the key, 38 is the value
print(ages[key])
## keys are sets
## keys are unordered
d = dict()
d[2] = 100
d[4] = 200
d[8] = 300
print(d)  # unpredictable order
## keys are unique
d = dict()
d[2] = 100
d[2] = 200
d[2] = 400
print(d)  # { 2:400 }
## keys must be immutable
'''
d = dict()
a = [1]
d[a] = 42 #Error: unhashable type: 'list'
'''
'''
## values are unrestricted
# values may be mutable
d = dict()
a = [1,2]
d["fred"] = a
print(d["fred"])
a += [3]
print(d["fred"]) # sees change in a!

# but keys may not be mutable
d[a] = 42       # TypeError: unhashable type: 'list'
'''
## 
'''
As mentioned above, a dictionary's keys are stored as a set. 
This means that finding where a key is stored takes constant time. 
This lets us look up a dictionary's value based on a key in constant time too!
'''
from collections import defaultdict

#: Option 1: initializing d[key] to 0:
def letterCounts(s):
    counts = dict()
    for ch in s.upper():
        if ch.isalpha():
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1
    return counts

# Option 2: using d.get(key, defaultValue):
def letterCounts(s):
    counts = dict()
    for ch in s.upper():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts

# Option 3: using defaultdict(lambda: defaultValue)
#    Note that defaultdict is not part of the
#    required 112 subset, but it is very handy.
def letterCounts(s):
    counts = defaultdict(lambda: 0)
    for ch in s.upper():
        if ch.isalpha():
            counts[ch] += 1
    return counts

# Regardless, this makes isAnagram clear and efficient:
def isAnagram(s1, s2):
    return (letterCounts(s1) == letterCounts(s2))

def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testIsAnagram()

def mostFrequent(L):
    # Return most frequent element in L, resolving ties arbitrarily.
    maxValue = None
    maxCount = 0
    counts = dict()
    for element in L:
        count = 1 + counts.get(element, 0)
        counts[element] = count
        if (count > maxCount):
            maxCount = count
            maxValue = element
    return maxValue

def testMostFrequent():
    print("Testing mostFrequent()... ", end="")
    assert(mostFrequent([2,5,3,4,6,4,2,4,5]) == 4)
    assert(mostFrequent([2,3,4,3,5,3,6,3,7]) == 3)
    assert(mostFrequent([42]) == 42)
    assert(mostFrequent([]) == None)
    print("Passed!")

testMostFrequent()


# mostPopularNames.py
# example creating a dictionary
# from real data on the web

# This data is copied from:
# https://www.ssa.gov/oact/babynames/decades/century.html

mostPopularNamesData = '''\
1    James   4,735,694   Mary    3,265,105
2   John    4,502,387   Patricia    1,560,897
3   Robert  4,499,901   Jennifer    1,467,664
4   Michael 4,330,025   Linda   1,448,309
5   William 3,601,719   Elizabeth   1,428,981
6   David   3,563,170   Barbara 1,402,428
7   Richard 2,467,544   Susan   1,104,407
8   Joseph  2,352,889   Jessica 1,045,519
9   Thomas  2,160,330   Sarah   993,847
10  Charles 2,106,078   Karen   985,728
11  Christopher 2,032,843   Nancy   969,544
12  Daniel  1,889,640   Lisa    965,003
13  Matthew 1,600,285   Margaret    944,344
14  Anthony 1,403,920   Betty   938,638
15  Donald  1,348,220   Sandra  873,609
16  Mark    1,346,509   Ashley  847,504
17  Paul    1,286,846   Dorothy 847,468
18  Steven  1,281,302   Kimberly    838,235
19  Andrew  1,252,016   Emily   826,262
20  Kenneth 1,226,558   Donna   823,285
21  Joshua  1,214,872   Michelle    811,401
22  Kevin   1,172,372   Carol   807,303
23  Brian   1,166,797   Amanda  772,882
24  George  1,159,331   Melissa 753,157
25  Edward  1,097,742   Deborah 739,809
26  Ronald  1,073,062   Stephanie   738,123
27  Timothy 1,069,165   Rebecca 729,683
28  Jason   1,035,285   Laura   721,299
29  Jeffrey 975,104 Sharon  720,816
30  Ryan    937,629 Cynthia 705,685
31  Jacob   925,412 Kathleen    689,366
32  Gary    899,858 Amy 680,682
33  Nicholas    891,818 Shirley 668,154
34  Eric    877,492 Angela  658,437
35  Jonathan    844,121 Helen   652,923
36  Stephen 840,005 Anna    629,400
37  Larry   802,430 Brenda  606,286
38  Justin  777,285 Pamela  592,694
39  Scott   769,663 Nicole  588,265
40  Brandon 759,155 Samantha    576,029
41  Benjamin    730,425 Katherine   574,858
42  Samuel  710,086 Emma    570,150
43  Frank   707,244 Ruth    563,391
44  Gregory 706,987 Christine   563,333
45  Raymond 679,913 Catherine   550,466
46  Alexander   666,982 Debra   548,279
47  Patrick 663,725 Rachel  546,309
48  Jack    637,347 Carolyn 542,250
49  Dennis  611,319 Janet   541,277
50  Jerry   602,696 Virginia    531,894
51  Tyler   589,687 Maria   528,760
52  Aaron   579,578 Heather 524,161
53  Jose    559,823 Diane   515,256
54  Henry   553,392 Julie   506,315
55  Adam    551,342 Joyce   500,601
56  Douglas 549,324 Victoria    481,786
57  Nathan  544,555 Kelly   471,257
58  Peter   540,603 Christina   471,012
59  Zachary 537,934 Lauren  469,625
60  Kyle    480,276 Joan    469,101
61  Walter  476,581 Evelyn  466,314
62  Harold  448,640 Olivia  464,246
63  Jeremy  437,552 Judith  449,885
64  Ethan   435,390 Megan   437,186
65  Carl    431,805 Cheryl  436,878
66  Keith   431,764 Martha  434,595
67  Roger   429,723 Andrea  434,410
68  Gerald  428,208 Frances 429,429
69  Christian   425,034 Hannah  426,616
70  Terry   422,106 Jacqueline  420,348
71  Sean    418,691 Ann 412,411
72  Arthur  415,722 Gloria  409,072
73  Austin  411,665 Jean    407,127
74  Noah    409,039 Kathryn 406,120
75  Lawrence    407,197 Alice   404,664
76  Jesse   388,484 Teresa  404,603
77  Joe 388,230 Sara    401,653
78  Bryan   381,581 Janice  400,210
79  Billy   379,560 Doris   395,048
80  Jordan  378,141 Madison 387,071
81  Albert  377,227 Julia   383,225
82  Dylan   377,049 Grace   379,239
83  Bruce   375,986 Judy    378,014
84  Willie  367,775 Abigail 373,862
85  Gabriel 352,072 Marie   373,633
86  Alan    348,591 Denise  371,019
87  Juan    345,375 Beverly 370,608
88  Logan   341,413 Amber   369,981
89  Wayne   339,139 Theresa 369,848
90  Ralph   338,689 Marilyn 369,847
91  Roy 338,079 Danielle    367,791
92  Eugene  330,306 Diana   358,617
93  Randy   327,821 Brittany    358,579
94  Vincent 322,824 Natalie 352,644
95  Russell 321,274 Sophia  351,883
96  Louis   320,157 Rose    351,296
97  Philip  315,423 Isabella    342,345
98  Bobby   313,302 Alexis  339,548
99  Johnny  308,243 Kayla   339,169
100 Bradley 306,339 Charlotte   338,315'''

# remove the commas in the numbers:
mostPopularNamesData = mostPopularNamesData.replace(',','')

def mostPopularNames():
    mostPopularNameCounts = dict()

    for line in mostPopularNamesData.splitlines():
        index,name1,count1,name2,count2 = line.split()
        mostPopularNameCounts[name1] = int(count1)
        mostPopularNameCounts[name2] = int(count2)

    while True:
        name = input('Enter a name (or leave blank to quit) --> ')
        name = name.capitalize()
        if (name == ''): break
        if (name in mostPopularNameCounts):
            print(f'  {name} has a count of {mostPopularNameCounts[name]}')
        else:
            print(f'  {name} is not in the list!')

mostPopularNames()