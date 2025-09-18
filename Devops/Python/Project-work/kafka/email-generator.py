def signup_user():
    while True:
        email = input("Please Enter your Email for signup..  (or type 'exit' to quit): ")
        if email.lower() == 'exit':
            print("Exiting signup process... Good Bye..!")
            break

        with open("emails.txt", "a") as file:
            file.write(email + "\n")

        print(f"Email {email} stored successfully.")


signup_user()