def area(a, b):
    return a * b

print(area(4, 5)) # positional arguments
print(area(a=4, b=5)) # keyword arguments

# Function with a arbitrary number of non-keyword arguments

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))

##########
# Define a function that takes an indefinite number of strings as parameters and
# returns a list containing all the strings in UPPERCASE and sorted alphabetically.
# Iterate through the list (or do list comrepehension) and apply str.upper() in each iteration. 
# Also, good to know that the sorted(list) method returns a sorted list in alphabetical order. 

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

###########
# Keyword arguments
def mean(**kwargs): 
    return kwargs

print(mean(a=1, b=3, c=3))

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=4, b=5))

##########
# Advanced Functions Examples:

Functions can have more than one parameter:

def volume(a, b, c):
    return a * b * c
Functions can have default parameters (e.g. coefficient):

def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))
Output: 32.808

Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))
An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
Output: 1001

An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

def find_winner(**kwargs):
    return max(kwargs)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
Output: Sim