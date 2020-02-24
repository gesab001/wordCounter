import json


jsonFile = open("bibleBooks.json", "r")
booksdata = json.load(jsonFile)
bookName =  input("book: " ).strip()
chapterNumber = int(input("from chapter: ").strip())
totalChapters = int(input("total chapters: ").strip())
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
new = open("result.txt", "w")
new.write("")
new.close()
f = open("result.txt", "a")

for k,v in s:
     string = k + ": " + str(v) + "\n"
     f.write(string)
totalWords = len(s)
f.write("\ntotal words: " + str(totalWords))
f.close()
