#sololearn exercise: sets
"""Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.

You can use the split() function to get a list of words in a string and then use the set() function to convert it into a set. For example, to convert the list x to a set you can use: set(x)

"""
#I receive the inputs (two different strings)
s1 = input()
s2 = input()

#I convert strings to sets of words
s1 = set(s1.split())
s2 = set(s2.split())

#I find the lenght of the words in common in both texts
print(len(s1 & s2))
