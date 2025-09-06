myfile = open('C:/Devops/Python/Notes/Input_output.txt')

with open('Python/Notes/Input_output.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)