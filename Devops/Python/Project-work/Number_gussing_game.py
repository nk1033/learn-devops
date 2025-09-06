import random

number_to_guess = random.randint(1,100)
while True:
   try:
    guess = int(input("Guess The Number Between 1 and 100 : - "))

    if guess < number_to_guess:
        print("Tooo Low...!")
    elif guess > number_to_guess:
        print("Tooo High...!")
    else:
       print("Congratulation You Guessed the correct Number...!")
       break
   except ValueError:
      print("Please Enter the valid Number..")