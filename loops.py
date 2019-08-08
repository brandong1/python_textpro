# Round each number in the list

monday_temperatures = [9.1, 8.8, 7.6]

print(round(monday_temperatures[0]))

for temperature in monday_temperatures:
    print(round(temperature))
    print("Done!")
    
for letter in 'hello':
    print(letter.title())
    
##########

colors = [11, 34, 98, 43, 45, 54, 54]

for number in colors:
    print(number)
    
##########

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int): #print only integers
        print(color)

##########
# Iterate over Dictionary

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)
    
##########
# You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))