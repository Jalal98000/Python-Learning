#Typecasting. It means making any command specific.
#1
a = "1"
b = "2"
print(a + b)
# answer will be 12
#2
a = "Jalal " 
b = "Ahmed Joy"
print(a + b)
#It happens cz in the " " every thing becomes/acts like as string. But number is Not string
#3
a = 1
b = 2
print(a + b)
# What to do if we want to convert any string to number/ intiger:  ?
#4
a = "1"
b = "2"
print(int(a) + int(b))
# ^ In that line by using int() we maked a string number into intiger number..
#5
a = 5
b = 6.5 #6.5 is a float
print(a + b)
# print(int(a) + float(b))
# ....But we can not make any string into  intiger like 
#6
a = "Jalal"
b = "Ahmed"
print(int(a) + int(b))
#It will be error because ^ (a) and (b) was not an intiger.



# Two types fo typecasting......1=Explicit typecasting....2=Implicit typecasting
# ..1=Explicit typecasting: In this typecasting as a programmer I'm specifying to python to make this datatype to this datatype.
# ..As like #4th programme.. to convert string to int
# ..2=Implicit typecasting: In this typecasting python automatically make any datatype to another datatype...
# ..As like #5th programme.. in that programme python make b=6.5 as a float automatically.