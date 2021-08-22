points = int(0) # Initialize points
lives = int(5) # Initialize counter of turns
hit = str("hit") #Initialize value 'hit' for future reference
while lives > 0: #Gives you 5 lives
    x = input("Insert your input ...: ") #Waits for your input
    if x in hit: #Verifies input
        points += 10 #HIT = +10 points
    else:
        points -= 20 #Missed HIT = -20 points
    lives -= 1
    print(points) #Display partial points
print("Final points: ", points) #Display final points
