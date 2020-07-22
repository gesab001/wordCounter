import json
import addtovocabularymodule as add


jsonFile = open("bibleBooks.json", "r")
booksdata = json.load(jsonFile)
booklist = list(booksdata.keys())
keystodelete = ["1 Samuel", "2 Samuel", "Daniel", "Deuteronomy", "Exodus", "Genesis", "Judges", "John", "Joshua", "Leviticus", "Luke", "Mark", "Matthew", "Numbers", "Psalms", "Revelation", "Ruth"]
for key in keystodelete:
   booklist.remove(key)
print(booklist)
bookName =  input("book: " ).strip()
chapterNumber = int(input("from chapter: ").strip())
totalChapters = len(booksdata[bookName])
result_filename = bookName + str(chapterNumber) + "-" + str(totalChapters+chapterNumber-1)  + ".txt"
book = booksdata[bookName]
dict = {}

for x in range(totalChapters):
	chapter = book[chapterNumber-1][str(chapterNumber)]
	print(chapter)
	string = " ".join(chapter)
	array = string.split(" ")
	for word in array:
	  word = word.replace(",", "")
	  word = word.replace("[", "")
	  word = word.replace("]", "")
	  word = word.replace("!", "")
	  word = word.replace(";", "")
	  word = word.replace(":", "")
	  word = word.replace(".", "")
	  if word!="":
	   if not word in dict:
	     dict[word]= 1
	   else:
	     dict[word]+= 1
	chapterNumber = chapterNumber + 1
s = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse=True)]
#result_filename = bookName + str(chapterNumber) + "-" + str(chapterNumber+totalChapters-1) + ".txt"
new = open(result_filename, "w")
new.write("")
new.close()
f = open(result_filename, "a")

newwords = []
fj = open("oldwords.json")
string = fj.read()
json_data = json.loads(string)
fj.close()
for k,v in s:
    if k in json_data:
      print("already learned")
      json_data[k] = json_data[k] + v
    else:  
      json_data[k] = v
      string = k + ": " + str(v) + "\n"
      f.write(string)
      newwords.append(k)

f.write("\ntotal words: " + str(len(newwords)))
f.close()

with open("oldwords.json", "w") as outfile:
  json.dump(json_data, outfile)

add.converToJson(result_filename)  
jsonfilename = result_filename[:-4] + ".json"
print(jsonfilename)
add.addGroup(jsonfilename)
