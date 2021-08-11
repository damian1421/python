# flip input and ommit non alphabetical characters.
coded = input()[::-1]
ascii_letters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
decoded = ""
for i in coded:
	if i in ascii_letters:
		decoded += i
	continue
print (decoded)
