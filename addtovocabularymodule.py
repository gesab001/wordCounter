import json


def save(data):
  f = open("vocabulary.json")
  string = f.read()
  jsondata = json.loads(string)
  f.close()
  jsondata["items"].append(data)
  with open("vocabulary.json", "w") as outfile:
     json.dump(jsondata, outfile, indent=4)

def converToJson(filename):
      f = open(filename)
      string = f.readlines()
      jsondata = {"items":[]}
      for x in range(0, len(string)):
         word = string[x]
         jsondata["items"].append(word)
      jsonfilename = filename[:-4] + ".json"
      with open(jsonfilename, "w") as outfile:
         json.dump(jsondata, outfile, indent=4)
    
def addGroup2(filename):
 print(filename)

def addGroup(filename):
    newgroup = {}
    newgroup["group"] = filename
    newgroup["words"] = []
    newgroup["total"] = 0 
    f = open(filename)
    string = f.read()
    jsondata = json.loads(string)
    f.close()
    words = jsondata["items"][:-2]
    total = jsondata["items"][-1].split(":")[1].strip()
    newgroup["total"] = total
    for word in words:
       string = word.split(":")[0].strip()
       frequency = word.split(":")[1].strip()
       newWord = {"word": string, "frequency": frequency}
       newgroup["words"].append(newWord)
    print(newgroup)
    save(newgroup)

