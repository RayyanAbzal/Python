'''
# Functions
def first_function():
    print("Good Morning Auckland, This is my function pr")
first_function()

def getContactInformation():
    email=input("Enter your email: ")
    phonenumber = int(input("Enter your phone number: "))
    print("Email:", email, "Phone number:", phonenumber)

getContactInformation()

def Greetings (firstName, lastName):
    print("Hello", firstName, " ", lastName)

Greetings(input("Enter your firstname: "), input("Enter your lastname: "))

def Greeting (firstName, lastName):
    print("Hello", firstName,"",lastName)
Greeting("John", "Smith")
Greeting("Python", "Class")

def Greetings (firstName, lastName):
    print("Greetings ", firstName, " ", lastName)

def Hi (firstName):
    print("Hi", firstName)

Greetings("John", "Smith")
Hi("Python")
print(firstName)

# Exercise 1
def Add (i, j):
    print(i + j)
Add(10, 9)

# Exercise 2
def Add (i, j):
    print(i + j)
Add(10, 9)

def Greetings (firstName, lastName):
    print("Greetings ", firstName, lastName)

def Hi (firstName):
    print("Hi", firstName)

Greetings("John","Smith")
Hi("Python")

def Add(x, y):
    return x + y
print(Add(5,6))

def Add(x, y):
    z = x + y
    return z
result = Add(5, 6)
print(result)

def Calculate (x,y):
    add=x+y
    sub=x-y
    div=x/y
    mul=x*y
    return add, sub, div, mul

addResult, subResult, divResult, mulResult = Calculate(9, 3)
print("9+3=", addResult)
print("9-3=", subResult)
print("9/3=", divResult)
print("9*3=", mulResult)

# CALLING A FUNCTION WITH A FUNCTION
def Function1():
    statement A
    statement B
def Function2():
    Function1()

# 2 functions
def printX(i):
    for i in range(i):
        print("x")
def MultipleX():
    printX(int(input("Please enter an integer number: ")))
MultipleX()

num=int(input("Enter a number for check odd or even: "))
def IsEven(num):
    
    if(num%2==0):
        print(num," Is an even number!")
    else:
        print(num," is an odd number!")
IsEven(num) 

def IfEven(n): 
      
    if(n==0): 
        return True
        
    elif(n==1): 
        return False
    else: 
        return IfEven(n-2) 
        
num = int(input("Please enter a number: "))
if(IfEven(num)): 
    print("Number",num ,"is even!") 
else: 
    print("Number",num ,"is odd!")

food = "kebab"

def ChangeFood():
    global food
    food = "hsp"
print ("Before calling the function: ", food)
ChangeFood()
print ("After calling the function: ", food)
'''
def multi(n):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)
multi(int(input("Input a number: ")))
