## to read or write a file in python we have inbuilt option called  --  with open("file_path", "access_mode")  -- access_mode = r / w ( read / write)

#Task: Update server.conf file when maximim connections update request on the server 

def update_server_config(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_server_config("c:/Devops/Python/Project-work/server.conf", "MAX_CONNECTIONS", "18790")