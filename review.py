import json

filename = "revelation1-11-reviewed.json" 
f = open(filename, "r")
jsondata = json.load(f)
words = jsondata["items"]
f.close()
print("total: " +  str(len(words)))
for x in words:
   print(x)
   print("\n\n\n")
   next = input()
   if next=="y":
      words.remove(x)
      with open("revelation1-11-reviewed.json", "w") as outfile:
         result = {"items": words}          
         json.dump(result, outfile)  
   print("\n\n\n")
