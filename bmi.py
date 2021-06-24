#your code goes here
import os
os.system("clear")
print ("Welcome to BMI calculator")
weight = float(input("What's your weight in kg? "))
height = float(input("What's your height in meters? "))
result = round((weight / (height ** 2)))
if (result  < 18.5):
	bmi = "Underweight"
	print (bmi)
elif (result < 25):
	bmi = "Normal"
	print (bmi)
elif (result < 30):
	bmi = "Overweight"
	print (bmi)
elif (result >= 30): 
	bmi = "Obesity"
	print (bmi)
os.system("clear")
print ("Your BMI is:", bmi," (",result,")")
