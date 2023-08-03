# String slicing and operations on string
Name = "Jalal,Miyad "
print(Name[0:5])

#length of string

fruit = "Mango"
print(len(fruit)) # everything in python start count from 0
#
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
#slicing
print("Mango is a fruit")
furit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4]) #it is actually is [len(fruit)0 : len(fruit)4]
# it will count 0-3
#for slicing we have to use []

# negative slicing
print(fruit[0:-3]) #output= MA ,,,,,becaise in case of (-) it will count from last and from 1
#=[0:len(fruit)-3]    
# in this case python automatically add [0:len(fruit)-3]

print(fruit[-1:-3]) 
#output= nothing because it is actually is [len(fruit)-1 : len(fruit)-3]
#^len(fruit)=5,,,,,,,-1= 5-1 and -3= 5-3  so it is [4:2]which is not possible
# but
print(fruit[-3:-1]) 
# output= ng,,,,,,,because it is [2:4]
