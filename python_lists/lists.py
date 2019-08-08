# temps = [221, 234, 340, 230]

# # new_temps = []
# # for temp in temps:
# #     new_temps.append(temp / 10)
    
# # print(new_temps)

# ##########

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

##########
# Define a function that takes, as a parameter, a list that contains numbers and strings
# and returns the list containing only numbers

def foo(list):
    return [i for i in list if not isinstance(i, str)]

##########
# Returns the list containing only the numbers that are greater than 0

def foo(list):
    return [i for i in list if i > 0]

##########

