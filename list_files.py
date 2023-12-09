import os
import sys

def list_exe_files(type, directory):
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith(type):
        print(os.path.join(root, file))
        
if __name__ == '__main__':
  print("******************************************************")
  print("*  How to run script: py list_files.py <type> <dir>  *")
  print("******************************************************")

  try:
    type = sys.argv[1]  # Get type
    try:
      dirs = sys.argv[2]  # Get directory
      list_exe_files(type = f'.{type}', directory = dirs) # List type file in directory
    except:
      list_exe_files(type = f'.{type}', directory = os.getcwd())  # List type file in current directory
  except:
    list_exe_files(type = ".exe", directory = os.getcwd())