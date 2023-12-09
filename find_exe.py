import os
import sys

def list_exe_files(directory):
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith(".exe"):
        print(os.path.join(root, file))
        
if __name__ == '__main__':
  try:
    list_exe_files(sys.argv[1])
  except:
    list_exe_files(os.getcwd())