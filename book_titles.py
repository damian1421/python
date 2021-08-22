#Author: l0gg3r
#Description: This program will  categorize books defining a code based on First Letter + Length of title.
#Author: l0gg3r
#Date: 2021-07
try:
    with open("books.txt", "r") as f:
        for line in f:
	#print(line[0]+str(len(line)-1))
            if line[-1] == "\n":
                print(line[0] + str(len(line)-1))
            else:
                print(line[0] + str(len(line)))
finally:
    f.close()
