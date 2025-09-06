# for number in range(3):
#     print("Attempt")

# ############################

# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and Failed")


# ## Nested loops 


# for x in range(5):
#     for y in range(3):
#         print(f"{x},{y}")

# ## range objects are not only the itterable objects in python strings are also itterable.

# for x in "python":
#     print(x)
# ## each itteration will get one charector 

numbers = [1,2,3,4,5,6]

print("Executing break condition.....")
for number in numbers:
    if number == 3:
        break
    print(number)

print("Executing continue condition....")
for number in numbers:
    if number == 3:
        continue
    print(number)
