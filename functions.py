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