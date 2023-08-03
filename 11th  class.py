#Details about string, indexing and about (for) loop.
Name = "Jalal"
print("Hello,", Name,"!")
#1
Jalal = ("Joy")
# print(Jalal)
print(Jalal[0])
print(Jalal[1])
print(Jalal[2])
#its call indexing
#0 , 1, 2 means.... in python inder = position
# print(Jalal[012]) #this is a error

#2
Jalal = '''My name is "Jalal".
I am a student.
(98000)'''
print(Jalal)
#what to do if we want to make #2 Jalal's every eliment index? 
#lets see!!Now we are going to use (for) loop...
for charecter in Jalal:
    print(charecter)

