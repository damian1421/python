import numpy
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = (sum(players)/len(players))
print (mean)
variance = float(numpy.var(players))
print (variance)
