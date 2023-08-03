import time

intime = int(time.strftime('%H'))
print(intime)

if (intime <=00 and intime >=10):
    print("Good morning")
elif(intime >=11 and intime <=21):
    print("Good evening")
else:
    print("Good night")
    
#Write a Python program to check if a number is even or odd
a = int(input("Enter your number:"))

if (a %2 == 0) :
    print("The number is even")
else:
    print("This number is odd")

#Write a Python program to check if a number is positive, negative, or zero
a = int(input("Write your number:"))
 
if (a > 0):
     print("The is positive.")
elif (a == 0):
    print("The number is Zero.")
else:
    print("The number is negative.")