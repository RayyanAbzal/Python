'''
# programme that reads a number, then program displays if the number is positive or negative
hi =float(input("Enter a number:"))
if hi > 0:
    print("Number is positive")
else:
    print("Number is negative")    

# Odd or even number
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Python program to find the greatest of two numbers using the built-in function
Num1 = input("Enter First number:")
Num2 = input("Enter Second number:")

if Num1 < Num2:
    print("second number is greater")
elif Num1 > Num2:
    print("first number is greater")
else:
    print("numbers are equal")

name = input("Please enter your name: ")
sales = int(input("What is your gross sales value? "))

if sales >= 500000:
    print("Congratulations %s! You are entitled to $5000 bonus!" %(name))

if sales < 500000:
    print("Sorry %s! You are NOT entitled to $5000 bonus" %(name))

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
'''
'''
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
'''
'''
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)
'''
'''
age = 
if age < 12:
    print("You're still a child!" )
elif age < 18:
    print("You're a teenager!" )
elif age < 30:
    print("You're pretty young!" )
elif age <50:
    print("Wisening up, are we?" )
else:
    print("Aren't the years weighing heavy?" )
'''
'''
weight = float(input("What is your weight?: "))
if weight>20:
    print("There is a $25 surcharge for luggage that is too heavy.")
elif weight<20:
    print("Have a safe flight!")
elif weight == 20:
    print("The weight is just right!")
'''
'''
grade = float(input("Please enter grade: "))
if grade >= 75 and grade <= 100:
    print("A") 
elif grade >= 60 and grade <= 74.99:
    print("B")
elif grade >= 45 and grade <= 59.99:
    print("C")
elif grade >= 40 and grade <= 44.99:
    print("D")
elif grade >= 0 and grade <= 39.99:
    print("E")
else:
    print("ERROR")
'''
'''
i = 1
while(i<=100):
    print(i)
    i += 1
'''
'''
for x in range(10):
    print(x)
print("done")
'''
'''
for i in range(20, 150, 10):
    print(i)
print("Done")
'''
'''
for i in range(2, 300, 2):
    print(i)
print("Done")
'''
'''
food = ["Chicken", "Chicken", "Chicken"]
for x in food:
    print(x)
'''
for mark in (95, 75, 60, 45, 90, 85, 40):
    if mark<50:
        print("The student fails whole program:(")
        break
    else:
        print("The student passes the course :)")
    