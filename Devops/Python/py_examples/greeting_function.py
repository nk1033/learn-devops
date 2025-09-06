def greeting():
    print("Hello Team")
    print("How are you doing....!!!!!!!")

greeting()

##############################################

def greet(first_name,last_name):
    print(f"Hello {first_name} {last_name}...!")
    print("Welcome to aboard")

greet("naresh","revalla")

###########  Define optional parameters -- Types of functions
# there are 2 types of functions.
#1) perform a task 
#2) return a value 

def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi...{name}"

message = get_greeting("Naresh")
file = open("content.txt", "w")
file.write(message)

## None is the return value of the function, All functions by default return a None value, None is a object that represents obsence of a value

## Keyword Arguments

def increment(number, by):
    return number + by

increment(2,1)
#or
print(increment(2,1))


#############

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total 

print(multiply(1,3,4,5))