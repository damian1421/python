import os
try:
    clear = lambda: os.system('clear') #Define 'clear' command
    clear()

    #Ask for input number to define the latest number
    n = int(input('Insert the biggest number of the Pythagorean table needed: '))

    #Create the Pythagorean table
    for i in range(1,n+1):
        for j in range(1,n+1):
            print ('{:3}'.format(i*j), end=' ')
        print()
except Exception as error:
    print(f"{error} has ocurred. Check if the input was a number")
