# Methods vs Functions
## Methods using s.f() rather than f(s)
s = "This could be any strings"
print(len(s)) # len is a  function
print(s.upper()) # upper is a string method, called using the . notation
                 # we say that we call the method upper on the string s
print(s.replace('could', 'may')) #  some methods take additional arguments

# Classes and Instances
## Classes are also called "Typed" in Python
   ### int, float, str, bool
## Instances are values of a given class or type
   ### Dor example, 'abc' is a str instance (also called a string)

# Writing classes
class Dog:
    # a class must have a body, even if it does nothing, so we will
    # use "pass" for now
    pass

# Create instances of our class
d1 = Dog()
d2 = Dog()
# Verify the type of these our class
print(type(d1))
print(isinstance(d2, Dog)) #True
# Set and get properties (aka "fields" or "attributes") of these instance
d1.name = "Dot"
d1.age = 4
d2.name = 'Elf'
d2.age = 3
print(d1.name, d1.age)
print(d2.name, d2.age)

# Writing constructors
## Constructor let us pre-load our new instances with properties
## We would like to write our constructor like this
class Dog:
    def __init__(self, name, age):
        # pre-load the dog instance with the given name and age:
        self.name = name
        self.age = age
 
# Create instances of our class, using our new constructor
d1 = Dog('Dot', 4)
d2 = Dog('Elf', 3)

print(d1.name, d1.age) # Dot 4
print(d2.name, d2.age) # Elf 3

# Writing methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Now we are using self, as convention requires:
    def sayHi(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old!')

d1 = Dog('Dot', 4)
d2 = Dog('Elf', 3)

# Notice how we change the function calls into method calls:

d1.sayHi() # Hi, my name is Dot and I am 4 years old!
d2.sayHi() # Hi, my name is Elf and I am 3 years old!
#Methods can take additional parameters
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method takes a second parameter -- times
    def bark(self, times):
        print(f'{self.name} says: {"woof!" * times}')

d = Dog('Dot', 4)

d.bark(1) # Dot says: woof!
d.bark(4) # Dot says: woof!woof!woof!woof!

#Methods can also set properties, like so
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.woofCount = 0   # we initialize the property in the constructor!

    def bark(self, times):
        # Then we can set and get the property in this method
        self.woofCount += times
        print(f'{self.name} says: {"woof!" * times} ({self.woofCount} woofs!)')

d = Dog('Dot', 4)

d.bark(1) # Dot says: woof! (1 woofs!)
d.bark(4) # Dot says: woof!woof!woof!woof! (5 woofs!)

# Advantages of Classes and Methods
## Encapsulation
'''
Organizes code
    a class includes the data and methods for that class
Promotes intuitive design
    well-designed classes should be intuitive, so the data and methods in the class match commonsense expectations
Restricts access
    len is a function, so we can call len(True) which crashes
    upper is a method on strings but not booleans, so we cannot even call True.upper()
'''
## Polymorphism
'''
polymorphism the same method name can run different code based on type, like so
'''
class Dog:
    def speak(self):
        print("Woof!")
class Cat:
    def speak(self):
        print("Meow!")

for animal in [Dog(), Cat()]:
    animal.speak() # Woof! Meow!

# Objects are mutable so aliases change!
import copy

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog1 = Dog('Dino', 10, 'shepherd')
dog2 = dog1            # this is an alias
dog3 = copy.copy(dog1) # this is a copy, not an alias

dog1.name = 'Spot'
print(dog2.name) # Spot (the alias changed, since it is the same object)
print(dog3.name) # Dino (the copy did not change, since it is a different object)
