temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

##########
# Define a function that takes as parameter a list that contains both numbers and strings
# and returns the same list with zeros instead of strings.

def foo(list):
    return [i if not isinstance(i, str) else 0 for i in list ]

##########
# Define a function that takes as parameter a list that contains decimal numbers as strings
# and returns the sum of those numbers.

def foo(lst):
    return sum([float(i) for i in lst])