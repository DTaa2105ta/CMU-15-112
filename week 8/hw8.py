#################################################
# hw8.py:
#
# Your name:
# Your andrew id:
#################################################

import cs112_s22_week8_linter
from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Midterm1 Free Responses
#################################################
# Helper function
def isPreSquareNumber(n):
    # takes a possibly-negative integer n and returns bool
    n = abs(n)
    def getLength(num):
        length = 1
        while num >= 10:
            length += 1
            num //= 10
        return length
    
    l = getLength(n) - 1
    def isPreSN_tail(n, l):
        tdiv = 10 ** l
        right_part = n % tdiv
        left_part = n // tdiv
        if l == 0:
            return False
        elif left_part * left_part == right_part:
            return True
        else:
            return isPreSN_tail(n, l-1)
    return isPreSN_tail(n, l)

def nearestPreSquareNumber(n):
    def t_nearestPreSquareNumber(acc1, acc2):
        if acc1 == 0:
            if isPreSquareNumber(acc2):
                return acc2
            return t_nearestPreSquareNumber(0, acc2 + 1)
        elif isPreSquareNumber(acc1):
            return acc1
        elif isPreSquareNumber(acc2):
            return acc2
        else:
            return t_nearestPreSquareNumber(acc1 - 1, acc2 + 1)
    if n < 0:
        return t_nearestPreSquareNumber(0, 0)
    else:
        return t_nearestPreSquareNumber(n, n)

def getRecord(team, scores):

	w, l, t = 0, 0, 0
	scores = scores.split("\n")
	scores = [record.split(" ") for record in scores]
	l_record = len(scores[0])
	
	for record in scores:
		for i in range(l_record-1):
			if record[i] == team:
				team_i = i
				score_i = team_i + 1
				r_score_i = score_i - 3 if score_i == l_record - 1 else score_i + 3
				score, r_score = int(record[score_i]), int(record[r_score_i])
				if score > r_score:
					w += 1
				elif score < r_score:
					l += 1
				else:
					t += 1
	return (w, l, t)

#################################################
# Other Classes and Functions for you to write
#################################################

class Person(object):
    def __init__(self, name, age, friendL=None):
        self.name = name
        self.age = age
        self.friends = friendL if friendL is not None else []
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getFriends(self):
        return self.friends
    def addFriend(self, friend):
    # Don't add if already friends
        if friend not in self.friends:
            self.friends.append(friend)
            if self not in friend.friends:
                friend.friends.append(self)
    def addFriends(self, friend):
         for fr in friend.friends:
             self.addFriend(fr)
    def getFriendsNames(self):
        return sorted([fr.getName() for fr in self.friends])

def getPairSum(L, target):
    seen = set()     # Use set for O(1) lookup
    for num in L:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    # No pair found
    return None
def containsPythagoreanTriple(L):
    for i in range(len(L)):
        a = L[i]
        seen = set()
        for b in L[i:]:
            c_squared1 = a**2 + b**2
            c1 = roundHalfUp(c_squared1 ** 0.5)
            if almostEqual(c1 * c1, c_squared1):   
                if c1 in seen:
                    return True
            
            c_squared2 = abs(a**2 - b**2)
            c2 = roundHalfUp(c_squared2 ** 0.5)
            if almostEqual(c2 * c2, c_squared2):   
                if c2 in seen:
                    return True
            seen.add(b)
    return False
#from collections import defaultdict
def movieAwards(oscarResults):
    results = dict()
    for record in oscarResults:
        movie = record[1]
        results[movie] = results.get(movie, 0) + 1
    return results

def friendsOfFriends(friends):
    return 42

#################################################
# Bonus Animation
#################################################

def bonus_appStarted(app):
    app.counter = 0

def bonus_keyPressed(app, event):
    pass

def bonus_mousePressed(app, event):
    pass

def bonus_timerFired(app):
    app.counter += 1

def bonus_redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'bonusAnimation', font='Arial 30 bold')
    canvas.create_text(app.width-20, app.height-20, text=str(app.counter))

def bonusAnimation():
    runApp(width=400, height=400, fnPrefix='bonus_')

#################################################
# Test Functions
#################################################
def testIsPreSquareNumber():
    print('Testing isPreSquareNumber(n)...', end='')
    assert(isPreSquareNumber(11) == True)         # 1|1, 1²=1
    assert(isPreSquareNumber(15225) == True)      # 15|225, 15²=225
    assert(isPreSquareNumber(12144) == True)       
    assert(isPreSquareNumber(20400) == True)      # 20|400, 20²=400
    assert(isPreSquareNumber(10010000) == True)   # 100|10000, 100²=10000
    assert(isPreSquareNumber(360129600) == True)    # 360|1296, 360²=129600
    assert(isPreSquareNumber(3664) == False)       
    assert(isPreSquareNumber(2500) == False)       
    assert(isPreSquareNumber(0) == False)         # No possible split
    assert(isPreSquareNumber(1) == False)         # No split (1| → invalid)
    assert(isPreSquareNumber(100) == False)       
    assert(isPreSquareNumber(1649) == False)      # 16|49, 16²=256≠49
    assert(isPreSquareNumber(1216) == False)      # 12|16, 12²=144≠16
    assert(isPreSquareNumber(104) == False)       # 1|04 (leading zero)
    assert(isPreSquareNumber(999801) == True) 
    assert(isPreSquareNumber(25125) == False)     # 25|125, 25²=625≠125
    assert(isPreSquareNumber(1236) == False)      # 12|36, 12²=144≠36
    assert(isPreSquareNumber(-15225) == True)    
    print('Passed!')

def testNearestPreSquareNumber():
    print('Testing nearestPreSquareNumber(n)...', end='')
    assert(nearestPreSquareNumber(0) == 11)
    assert(nearestPreSquareNumber(6000) == 6036)
    assert(nearestPreSquareNumber(-100) == 11)
    #Negatives should still work
    assert(nearestPreSquareNumber(20202) == 20004)
    #Halfway between 20004 and 20400
    assert(nearestPreSquareNumber(30100) == 30009)
    #Some solutions may be too slow!
    print('Passed!')

def testGetRecord():
    print('Testing getRecord()...', end='')
    scores = '''\
    Chi 2 - Pit 1
    Chi 2 - Pit 11
    Mia 13 - Pit 0
    Pit 4 - Mia 4
    Chi 2 - Mia 3'''
    assert(getRecord('Pit', scores) == (1, 2, 1))
    assert(getRecord('Mia', scores) == (2, 0, 1))
    assert(getRecord('Chi', scores) == (1, 2, 0))
    assert(getRecord('Det', scores) == (0, 0, 0))
    print('Passed')

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    # Note that fred != "fred" - one is an object, and the other is a string.
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    #       are the friends of this person, listed in the order that
    #       they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    #       names of the friends of this person.  This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])

    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])

    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

def testGetPairSum():
    print("Testing getPairSum()...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
                      [ (10, -8), (-8, 10),(-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, 0, 5], 10) in
                      [ (10, 0), (0, 10)] )
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10) in
                      [ (19, -9), (-9, 19)] )
    assert(getPairSum([1, 4, 3], 2) == None) # catches reusing values! 1+1...
    print("Passed!")

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,8,1,4]) == False)
    # 54, 728, 730
    assert(containsPythagoreanTriple([730,54,728,4])== True) 
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,728,4])== True) 
                                      
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,729,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4, 
                                6253, 7800, 9997]) == True) # 6253, 7800, 9997
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4, 
                                6253, 7800, 9998]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,6253, 
                                7800, 9996]) == False)
                                      
    assert(containsPythagoreanTriple([1, 2, 3, 67, 65, 35,83, 72,97, 
                                      25, 98, 12]) == True) # 65, 72, 97
                                      
    assert(containsPythagoreanTriple([1, 1, 1]) == False)
    assert(containsPythagoreanTriple([1, 1, 2]) == False)
    assert(containsPythagoreanTriple([3, 5, 5]) == False)
    print("Passed!")

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")

def testBonusAnimation():
    print('Note: You must visually inspect your bonus animation to test it.')
    bonusAnimation()

def testAll():
    #testIsPreSquareNumber()
    #testNearestPreSquareNumber()
    #testGetRecord()
    #testPersonClass()
    #testGetPairSum()
    #testContainsPythagoreanTriple()
    
    testMovieAwards()
    #testFriendsOfFriends()
    
    # testBonusAnimation()

#################################################
# main
#################################################

def main():
    cs112_s22_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()    
