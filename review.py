import json

filename = "revelation1-11-reviewed.json" 
f = open(filename, "r")
jsondata = json.load(f)
words = jsondata["items"]
f.close()
print("total: " +  str(len(words)))
count = 1
for x in words:
   print(str(count)+". "+ x[:-3])
   print("\n\n\n")
   next = input()
   if next=="y":
      words.remove(x)
      with open("revelation1-11-reviewed.json", "w") as outfile:
         result = {"items": words}          
         json.dump(result, outfile)  
   print("\n\n\n")
   count = count + 1
