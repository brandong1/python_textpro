myfile = open("fruits.txt")
content = myfile.read()
myfile.close() # Flush and close out the IO object

print(content)

##########

file = open("fruits.txt")
content = file.read()
file.close()
print(content[:90])

##########

def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

##########

with open("bear.txt") as file:
    content = file.read()

with open("first.txt", "w") as file:
    file.write(content[:90])
    
###########
# Append the text of bear1.txt to bear2.txt.

with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)

############
# Modify the content of data.txt

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    file.seek(0)
    file.write(content)
    file.write(content)
    
#############

You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
    
You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
    
You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
    
You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()