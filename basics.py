# import datetime
# print(datetime.datetime.now())

# Data Types

# mynumber = 10
# mytext = "Hello"
# print(mynumber, mytext)

# List

# student_grades = [9.1, 8.8, 7.5]
# student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

# mysum = sum(student_grades.values())
# length = len(student_grades)
# mean = mysum / length
# print(mean)

# def mean(value):
#     if type(value) ==dict:
#         the_mean = sum(value.values()) / len(value))
#     else:
#         the_mean = sum(mylist) / len(mylist)
#     return the_mean

# monday_temperatures = [8.8, 9.1, 9.9]
# student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

# print(mean([monday_temperatures))
##########
# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"
    
# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))

##########

# user_input = input("Enter your name: ")
# message1 = "Hello %s!" % user_input
# message2 = "Hello {}!".format(user_input)
# print(message1)
# print(message2)

##########

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")

# # These print the same thing
# message1 = "Hello %s %s!" % (name, surname)
# message2 = "Hello {} {}!".format(name, surname)

# print(message1)
# print(message2)

############

# def foo(name):
#     return "Hi {}".format(name)

# def foo(name):
#     return "Hi {}".format(name.title()) # Returns uppercase first letter

############