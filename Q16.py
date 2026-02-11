#Question
#Swap two numbers using a third variable

#Logic
#Create two variable 
#store two numbers 
#a = c , c = b , b = a

#Steps
# a= 08
# b = 09
# c = a , a = b , b = c

#Code
a = int(input("Num1 : "))
b = int(input("Num2 : "))
c = a
a = b
b = c
print(a)
print(b)