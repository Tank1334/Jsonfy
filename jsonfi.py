import json
from ColoredText import bcolors
from time import sleep
import os
import os.path

class doc:
  # Setting default values and looking for name of the json file.
  def __init__(self, filename, OperatingSystem="linux"):
    filename = f"{filename}.json"

    self.filename = filename
    self.OperatingSystem = OperatingSystem
    try:
      with open(filename,'r'):
        print("File:",filename, "Has been loaded up")
    except FileNotFoundError:
      if OperatingSystem == "linux":
        check = input("File does not exist. Would you like to create one? [y/n] ")
        if check == 'y':
          print("File being created.")
          os.system(f"touch ./{filename}")
          while not os.path.exists(filename):
            print(".", end="")
            sleep(0.01)
          print("\nFile created.")
          os.system(f"touch ./{filename}")
        else:
          print(bcolors.FAIL + bcolors.UNDERLINE + "ERROR:" + bcolors.ENDC + bcolors.FAIL + f" File \"{filename}\" Does not exist. Please try again.")
      else:
        print("Im sorry, Other OSes not yet supported.")
  # function to simply print out the text
  def list_json(self, warns=True):
    if warns == True:
      print(bcolors.WARNING + "\nWARNING: This feature will probably be removed in a future version. Please use other options like \"list_pretty\" to print.\n" + bcolors.BOLD + bcolors.UNDERLINE + "To stop seeing these error please add \"False\" as an argument\n\n" + bcolors.ENDC)

    with open(self.filename, "r") as f:
      k = json.load(f)
      return(k)
  def pretty_json(self, warns=True):
    pass


####Declaeration tags:
##Needs file Name
##OPTIONAL: add os tag. Default=Linux

#### Feature:
### List all keys/vals
## Usage: print(list())
#Notes: No need for any arguments holders for now.