import random

emojis = {"r" : "🪨", "p" : "📄", "s" : "✂️"}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choices = input("Lets play a game....Rock, Paper, Scissor?  select (r/p/s): ").lower()
        if user_choices in choices:
            return user_choices
        else:
           print("Invalid choice.. Please Enter (r/p/s)")

def disply_choices(user_choices, computer_choice):
    print(f"You'r choice is {emojis[user_choices]}")
    print(f"Computer choice is {emojis[computer_choice]}")

def determine_winner(user_choices, computer_choice):
    if user_choices == computer_choice:
        print("Tie...!")
    elif (( user_choices == 'r' and computer_choice == 's') or
         ( user_choices == 's' and computer_choice == 'p') or
         ( user_choices == 'p' and computer_choice == 'r')):
        print("You Win...")
    else:
        print("You lose....")

def get_continue_choice():
    while True:
        should_continue = input("Continue to play again (y/n): ").lower()
        if should_continue in ('y', 'n'):
            return should_continue
        else:
            print("Please Enter valid Input y/n : ")


def Play_game():
    while True:
        user_choices = get_user_choice()

        computer_choice = random.choice(choices)

        disply_choices(user_choices, computer_choice)

        determine_winner(user_choices, computer_choice)
        
        should_continue = get_continue_choice()


        if should_continue == 'n':
            print("Thanks for playing...")
            break

Play_game()