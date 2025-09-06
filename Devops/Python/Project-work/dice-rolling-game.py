# Roll the dice? If user enter Y , Generate two random numbers & print them
# If user enter No,Print thank you message and terriminate 
# ELSE print invalid 
import random

while True:
    choice = input("Roll the Dice.....? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1},{die2})")
    elif choice == 'n':
        print("Thanks for Playing.....!")
        break
    else:
        print("Invalid choice...Please enter correct value (y/n): ")