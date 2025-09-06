name = 'youtube'
print(name)
print(name[0])
print(name[0:2])
print(name[:3])
print(name[4:])
print(len(name))
print(name[-1])
course = "Python \"Programming"
print(len(course))
print(course[:])
course1 = "Pthon \n new \n programming!"
print(course1)

# Below are escape sequences in python.

# \"
# \'
# \\
# \n

########################################

# here we have two variables 
first = "naresh"
last = "revalla"

full_name = first + " " + last 
full = f"{first} {last}"

print(full_name)
print(full)

### Below are the functions

# len # upper - to conver in upper case 

print(full_name.upper())


### To trim white spaces from string , it will remove space from beggining / end of the string

value = "Mynewvalue"
print(value.strip())

### find - to find a index -- it will disply the index number 

topic = " Python Programming"
print(topic.find("Pro"))

## replace  -  it will replace a charectors 

print(topic.replace("P","j"))

### print( "Pro" in topic ) -- it is a bool will disply True / False  -- in / not in 

print("Pro" in topic)

