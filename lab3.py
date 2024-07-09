# Question no 1
# Numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
print("Question number 1:\nNUmbers which are divisible by 7 and mulitple of 5, between 1500 and 2700")
i=1500
for  i in range(i,2701):
    print(i)
    if(i%7==0 and i%5==0):
        print(i)
    else:
        continue

# Question no 2
# Temperature conversion between Fahrenheit and Celsius based on user choice
choice = int(input("Enter 1 to convert Fahrenhiet to Celsius or Enter 2 to convert Celsius to Fahrenhiet: "))
if(choice==1):
    fah=int(input("Enter temperature in Fahrenheit: "))
    cel=5*(fah-32)/9
    print("Temperature in Celsius: ",int(cel))
elif(choice==2):
    cel=int(input("Enter temperature in Celsius: "))
    fah=9*cel/5+32
    print("Temperature in Celsius: ",fah)
else:
    print("Invalid Choice!!!")

#Question no 3
# Number guessing game
import random
num=random.randint(1,9)
i=True
while(i==True):
    guess=int(input("Guess any number between 1 to 9: "))
    if(num==guess):
        print("Well guessed!")
        i=False
    else:
        print("Try again!!!\n")
        continue

# Question no 4
# Pattern printing
i=1
star=6
for i in range(star):
    j=1
    for j in range(i):
        print("*", end="")
    print()
star=4
i=1
for i in range(star):
    j=1
    for j in range(star-i):
        print("*", end="")
    print()

# Question no 5
# Reverse a word
word=input("Enter a word: ")
length=len(word)-1
for i in range(len(word)):
    print(word[length],end="")
    length-=1

# Question no 6
# Count even and odd numbers in a tuple
# numbers = (1,2,3,4,5,6,7,8,9)
user_input=input("Enter space separated integers (like 20 3 18): ")
my_tuple=tuple(int(item) for item in user_input.split())
even=0
odd=0
i=1
for i in range(i,len(my_tuple)+1):
    print(i)
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even, " Number of odd numbers: ", odd)

# Question no 7
# Append elements to a list and print their types
# my_list=[2,3.2,-3,'w3resources',(0,3),[3,12],{"class":"S","number":32}]
my_list=[]
no=int(input("Enter number of elements you want to enter in list: "))
for i in range(no):
    value=input("Enter element: ")
    my_list.append(value)

for i in my_list:
    print(i," ", type(i))


#Question no 8
# Print numbers except 3 and 6
for x in range(7):
    if(x==3 or x==6):
        continue
    else:
        print(x, end=" ")

# Question no 9
# Fibonacci series up to 50
num1=1
num2=1
total=0
bol=True
print(num1,num2,end=" ")
while(bol==True):
    total=num1+num2
    if(total<=50):
        print(total, end=" ")
        num1=num2
        num2=total
    else:
        bol=False

# FizzBuzz program
i=1
for i in range(i,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

# Question no 10
# Create and print a 2D array
m=int(input("Enter no. of rows: "))
n=int(input("Enter no. of columns: "))
arr=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j]=i*j

for i in range(m):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

# Question no 11
# Convert input to lowercase
line=input("Enter sequence of lines and enter to terminate: ")
print(line.lower())

# Question no 12
# Validate binary numbers and print those divisible by 5
my_list=[]
choice=True
while(choice==True):
    num=input("Enter four digit binary number: ")
    my_list.append(num)
    choice=int(input("Enter 1 to add more numbers or 2 to terminate: "))
    if(choice==1):
        choice==True
    else:
        choice==False

for l in my_list:
    decimalNumber= int(l,2)
    if(decimalNumber%5==0):
        print(l, end=" ")
    else:
        continue


# Question no 13
# Count digits and letters in a string
user_string=input("Enter any string: ")
digit=0
letter=0
for i in range(len(user_string)):
    if(user_string[i].isdigit()):
        digit+=1
    elif(user_string[i].isalpha()):
        letter+=1
    else:
        continue
print(f"Leters: {letter}\nDigits: {digit}")

#Question no 14
# Validate password based on given criteria
password=input("Enter your password that contains\nAt least 1 letter between [a-z] and 1 letter between [A-Z].\nAt least  1 number between [0=9].\nAt least 1 character from [$#@].\nMinimum length 6 characters.\nMaximum length 16 characters.\n")
print()
password_length=len(password)
small_letter=0
capital_letter=0
digit=0
special_letter=0
if(password_length>=6 and password_length<=16):
    for i in range(password_length):
        if(password[i]>='a' and password[i]<='z'):
            small_letter+=1
        elif(password[i]>="A" and password[i]<="Z"):
            capital_letter+=1
        elif(password[i]>="0" and password[i]<="9"):
            digit+=1
        elif(password[i]=="$" or password[i]=="#" or password[i]=="@"):
            special_letter+=1
        else:
            print(f"{password[i]} invalid character!")
else:
    print("Length should be between [6-16]")
    digit+=1

if(small_letter==0):
    print("Password must contain atleast 1 letter between [a-z]")
if(capital_letter==0):
    print("Password must contain atleast 1 letter between [A-Z]")
if(digit==0):
    print("Password must contain atleast 1 digit between [1-9]")
if(special_letter==0):
    print("Password must contain atleast 1 character [$#@]")
elif(small_letter!=0 and capital_letter!=0 and digit!=0 and special_letter!=0):
    print("Valid password")