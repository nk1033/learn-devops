import random

emojis = {"r" : "🪨", "p" : "📄", "s" : "✂️"}
choices = ("r","p","s")

while True:
    user_choices = input("Lets play a game....Rock, Paper, Scissor?  select (r/p/s): ").lower()
    if user_choices not in choices:
        print("Invalid choice.. Please Enter (r/p/s)")
        continue

    computer_choice = random.choice(choices)
    print(f"You'r choice is {emojis[user_choices]}")
    print(f"Computer choice is {emojis[computer_choice]}")

    if user_choices == computer_choice:
        print("Tie...!")
    elif (( user_choices == 'r' and computer_choice == 's') or
( user_choices == 's' and computer_choice == 'p') or
( user_choices == 'p' and computer_choice == 'r')):
        print("You Win...")
    else:
        print("You lose....")

    while True:
        should_continue = input("Continue to play again (y/n): ").lower()

        if should_continue == 'n':
            print("Thanks for playing...")
            break
        elif should_continue == 'y':
            break
        else:
            print("Please Enter valid Input y/n : ")

    if should_continue == 'n':
        break

