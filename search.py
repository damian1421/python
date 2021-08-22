#Searches a word in text
text = input("Insert source text: ")
word = input("Insert word to search: ")
def search(x,y):
	if y in x:
		print("Word found")
	else:
		print("Word not found")
search(text,word)
