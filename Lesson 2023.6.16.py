# Replit - Python Starter (Teams) - Larger of Two Numbers

num1 = input ("Please enter the first number: ")
num2 = input ("Please enter the second number: ")

if num1 == num2:
    print ("Both numbers are equal.")
elif num1 > num2:
    print (num1, "is larger than", num2)
elif num2 > num1:
    print (num2, "is larger than", num1)
else:
    print ("Error!")
