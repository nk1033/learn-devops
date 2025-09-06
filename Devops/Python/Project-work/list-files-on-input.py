# import os

# folders = input("Please provide the list of folders with spaces in between:").split()

# for folder in folders:
#     try:
#       list_dir = os.listdir(folder)
#     except FileNotFoundError:
#       print(f"Please provide a valid folder name...looks like {folder} folder does not exist...")
#       break  ## to ignore error use continue
#     except PermissionError:
#        print(f"You don't have permission to this folder {folder}")

#     for files in list_dir:
#        print(files)


#### wrire above code in modular way ..

import os 

def list_files_in_folder(folder_path):
   try:
      files = os.listdir(folder_path)
      return files, None
   except FileNotFoundError:
      return None, "File Not Found"
   except PermissionError:
      return None, "Permission Denied"

def main():
   folder_paths = input("Please provide the list of folders with spaces in between:").split()

   for folder_path in folder_paths:
      files, error_message = list_files_in_folder(folder_path)
      if files:
         print(f"files in {folder_path}")
         for file in files:
            print(file)
      else:
         print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
   main()

