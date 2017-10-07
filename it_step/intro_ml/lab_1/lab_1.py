## playing with basic data types
x = 3
print x, type(x)
my_letter = 'a'
print my_letter, type(my_letter)
my_name = "Alexis"
print my_name, type(my_name)
# is there a type difference?
print "my name is", my_name

print "x =", x
# operations
print "x + 1 =", x + 1   # addition;
print "x - 1 =", x - 1   # subtraction;
print "x * 2 =", x * 2   # multiplication;
print "x ** 2 =", x ** 2  # exponentiation;
print "x mod 2 =", x % 2 # modulo

y = 2
print y, type(y) # returns 2 <type 'int'>
print x, "/", y, "=", x / y # returns 1. it is an integer division (returning an integer)

y = 2.0
print y, type(y) # returns 2.0 <type 'float'>
print x, "/", y, "=", x / y # returns 1.5. it is a float operation (returning a float) because y is a float.

# updating a value
x += 1 # this is equivalent to x = x + 1
print "value of x after x += 1:", x  # Prints "4"
x *= 2 # this is equivalent to x = x * 2
print "value of x after x *= 2:", x  # Prints "8"

# boolean values
t, f = True, False # this is equivalent to writing "t = True" and "f = False" on 2 separate lines
print t, type(t) # prints "True <type 'bool'>

# a few basic boolean operations
print t, "and", f, "is", t and f # Logical AND
print t, "or", f, "is", t or f  # Logical OR
print "not", t, "is", not t   # Logical NOT
print "not", f, "is", not f   # Logical NOT
print t, "xor", f, "is", t != f  # Logical XOR

hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter.
print "the length of the word", hello, "is", len(hello)

hello_world = hello + ' ' + world  # String concatenation
print hello_world # prints "hello world"

hello_world_12 = '%s %s %d' % (hello, world, 12) # Another way to concatenate 
print hello_world_12

print hello.capitalize()  # Capitalize a string; prints "Hello"
print hello.upper()       # Convert a string to uppercase; prints "HELLO"
print hello.upper().lower() # lower() converts a string to lowercase. prints "hello"
print hello.rjust(7)      # Right-justify a string, padding with spaces; prints "  hello"
print hello.center(7)     # Center a string, padding with spaces; prints " hello "
print hello.replace('l', '(ell)')  # Replace all instances of one substring with another;
                               # prints "he(ell)(ell)o"
print '  world '.strip()  # Strip leading and trailing whitespace; prints "world"
print ' wor ld '.strip()  # but it does not remove whitespaces in between

xs = [3, 1, 2]   # Create a list
print xs, xs[2]
print xs[-1]     # Negative indices count from the end of the list; prints "2"

xs[2] = 'foo'    # Lists can contain elements of different types
print xs

xs.append('bar') # Add a new element to the end of the list
print xs  

x = xs.pop()     # Remove and return the last element of the list
print x, xs 

nums = range(5)    # range is a built-in function that creates a list of integers
print nums         # Prints "[0, 1, 2, 3, 4]"
print nums[2:4]    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print nums[2:]     # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print nums[:2]     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print nums[:]      # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print nums[:-1]    # Slice indices can be negative; prints ["0, 1, 2, 3]"
nums[2:4] = [8, 9] # Assign a new sublist to a slice
print nums         # Prints "[0, 1, 8, 8, 4]"

# loop over the elements of a list
animals = ['cat', 'dog', 'monkey']
for animal in animals: # for loop
    print animal

for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)


nums = [0, 1, 2, 3, 4]
# let's say we want to compute the squares of the values in the list 'nums'
squares = [] # define another list (empty)
for x in nums:
    squares.append(x ** 2) # compute the square value and append it to 'squares'
print squares

# another way to do it:
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums] # same operation, using "list comprehension"
print squares

# iterating with a condition (only even numbers)
nums = [0, 1, 2, 3, 4]
even_squares = []
for x in nums:
    if x % 2 == 0:
        even_squares.append(x ** 2) # compute the square value and append it to 'squares'
print even_squares

# same thing, with list comprehension:
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares

# check if a list has a given element:
print "is 15 is the even_squares list?", 15 in squares
print "is 16 is the even_squares list?", 16 in squares

# Dictionaries:
d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
# the first element is called the key (e.g. 'cat'), the second is the value (e.g. 'cute')
print d['cat']       # Get an entry from a dictionary; prints "cute"
print 'cat' in d     # Check if a dictionary has a given key; prints "True"

# add an element
d['fish'] = 'wet'    # Set an entry in a dictionary
print d['fish']      # Prints "wet"

# if you uncomment the following line, you'll have an error: "KeyError: 'monkey' not a key of d"
# print d['monkey']  # KeyError: 'monkey' not a key of d
# to avoid that kind of error, we can specify a default value:
print d.get('monkey', 'N/A')  # Get an element with a default; prints "N/A"
print d.get('fish', 'N/A')    # Get an element with a default; prints "wet"

# remove an element
del d['fish']        # remove an element from a dictionary
print d.get('fish', 'N/A') # "fish" is no longer a key; prints "N/A"

# iteration over dictionaries:
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)

# equivalent way of doing it:
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)

# comprehension also exists for dictionaries:
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_square

# functions
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print x, "is", sign(x)
# prints:
# -1 is negative
# 0 is zero
# 1 is positive

def hello(name, loud=False):
    if loud:
        print 'HELLO, %s' % name.upper()
    else:
        print 'Hello, %s!' % name

hello('Bob')
hello('Fred', loud=True)

# plot some data
import matplotlib.pyplot as plt # import a plot library
plt.figure() # define a figure environment
plt.plot(nums, squares) # plot in the figure

# another example:
nums = range(10)
from math import exp
exponentials = [exp(x) for x in nums]
plt.figure()
plt.plot(nums, exponentials)

# an extra exercice, an implementation of the quick sort
# See https://en.wikipedia.org/wiki/Quicksort for explanations
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print quicksort([3,6,8,10,1,2,1])