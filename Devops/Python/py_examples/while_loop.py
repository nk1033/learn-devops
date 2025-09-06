## will repeat something as long as until the condition true 

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

## Note: if user given QUIT or Quit the loop will continue to execute 

command = ""
while command.lower() != "quit":
    command = input(">>")
    print("ECHO", command)


## infinite loops 

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break