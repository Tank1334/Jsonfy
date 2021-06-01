import json
class doc:
  def __init__(self, filename, OperatingSystem="linux"):
    filename = f"{filename}.json"

    self.filename = filename
    self.OperatingSystem = OperatingSystem
    try:
      with open(filename,'a') as f:
        print("File:", filename, "Has been loaded up")
    except:
      if OperatingSystem == "linux":
        pass
      else:
        print("Im sorry, Other OSes not yet supported.")
  def list(self):
    with open(self.filename, "r") as f:
      k = json.load(f)
      return(k)

####Declaeration tags:
##Needs file Name
##OPTIONAL: add os tag. Default=Linux

#### Feature:
### List all keys/vals
## Usage: print(list())
#Notes: No need for any plave holders for now.  