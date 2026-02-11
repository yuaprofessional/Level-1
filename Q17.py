#Question
#Swap two numbers without using a third variable

#Logic
#Create two variable 
#store two numbers 
#

#Steps
# a= 08
# b = 09
# c = a , a = b , b = c

#Code
a = int(input("a : "))
b = int(input("b : "))
a = a + b
b = a - b
a = a - b
print(a)
print(b)

#Another Logic
a = a * b
b = a // b
a = a // b
print(a)
print(b)