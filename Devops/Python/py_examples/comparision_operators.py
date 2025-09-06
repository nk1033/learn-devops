temperature = 30
if temperature > 30:
    print("It's WSRM")
    print("dRINK WATER")
elif temperature > 20:
    print("It's nice")
else:
    print("It's Cold")
print("Done")

## ternary operators
age = 12
if age >= 12:
    print("Eligible")
else:
    print("Not eligible")


#or

age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message) 


## Logical operators 
##and /  or /  not 

high_income = False
good_credit = False
student = False 

if ( high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

## chaining comparision operators 
# age should be between 18 & 65
age = 12
if age >= 18 and age <= 65:
    print("Eligible")

## or 

if 18 <= age < 25:
    print("Eligible")
    