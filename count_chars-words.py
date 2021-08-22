#Description: Count letters in text
#Author: l0gg3r
#This is written in spanglish!

from string import ascii_lowercase

dict = {} #Initizalize empty dictionary wich will include (later) chars as keys and chars_occurrences as values.
text = input("Ingreso el texto a analizar: ") #Ingreso texto a analizar
text = text.lower() #Convierto todo el texto a minúscula para no difereciar 'e' de 'E'...
words = {} #Initizalize empty dictionary which will include words as keys  (later) words_occurrences as values. I ommit spaces!
for char in ascii_lowercase: #Recorro el abecedario
    if char in text: #Itero entre cada carácter del texto
        char_count = text.count(char) #Defino char_count como la cuenta de cada carácter
        dict[char] = char_count #Busco (y lo creo si no existe), definiendo el valor como la suma de todas las ocurrencias

for word in text.split(" "): #Itero entre cada palabra del texto, omitiendo espacios vacíos
        word_count = text.count(word) #Defino word_count como la cuenta de cada palabra
        words[word] = text.count(word) #Actualizo el valor de cada palabra como la suma de todas sus ocurrencias

print ("Dictionary of chars: ",dict) # Imprimo diccionario con cada "Key : Value"
print ("Dictionary of words: ",words) # Imprimo diccionario de palabras con cada "Key : Value"
