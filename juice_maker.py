#Sololearn Exercise
class Juice:
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self,obj):
        name = self.name + "&" + obj.name
        cap = self.capacity + obj.capacity
        return Juice(name,cap)
    def __str__(self):
        return (self.name + '('+str(self.capacity) + 'L)')

a = Juice('Orange',1.5)
b = Juice('Apple',2.0)
result = a + b
print (result)
