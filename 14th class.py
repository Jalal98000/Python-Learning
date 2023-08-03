# Condition, loop
#if, if-else-elif, nested if-else-elif
#Conditional operators (true of false)
#>, <, >=, <=, == ,!=not


a = int(input("Enter your age"))
print("Your age is:", a )

print(a > 18)
print(a <= 18)
print(a == 18)
print(a!= 18) #you cannot use (_)before !
if (a > 18):
     print("You can drive")
else:
    print("You can not drive")

# #if-else

applePrice = 210
budget = int(input("Your budget:"))
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
elif (budget >= 200 and budget < 210):
    print("It's ok you can gat 1 kg apple")
else:
    print("Budget insufficent.")
    

