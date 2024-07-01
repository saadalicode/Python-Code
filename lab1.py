
# (#)hash symbol use for comment in Python lang

# print function or display on console
print("----Simple print statement function----\nProgramming makes life easy!!!\n")

# user input and output on console
# input function always take string as input from user 
print("----input/output function use----")
txt = input("Enter any String: ")
print(txt)

# indentation
x=1
if x>0:
    print("----Use of indentation----\nWith if condition")

# data types in python
print("\n----Different Data Types----")
a=12
print(str(a),"is belongs to",str(type(a)))
b=-12
print(str(b),"is belongs to",str(type(b)))
c=2.2
print(str(c),"is belongs to",str(type(c)))
d=-2.2
print(str(d),"is belongs to",str(type(d)))
st="Strings"
print(str(st),"is belongs to",str(type(st)))
com=complex(7,7)
print(str(com),"is belongs to",str(type(com)))
bol=True
print(str(bol),"is belongs to",str(type(bol)))

# special characters 
print("\n---Special Characters or Escape Sequence---")
print("\\ symbol represent backslash.")
print("\'\t\' symbol represent tab")
print("\'Python is interpretable language.\' symbol for single quote.")
print("\"Python is interpretable language.\" symbol for double quote.")

# string access
print("\n----String Access via indices----")
s="Simplicity is the only beauty."
# s="Hello World"
print(s)
length=int(len(s))
print("Enter 1 to ",str(length),"to display a character from above string : ")
num=int(input())
print("Requested character:",s[num-1])

# slicing in string
print("\n----Slicing and Methods in String----")
sli_s=s[1:7]
print(sli_s)
# replace function
print(s.replace('the','a'))
# upper function 
print(s.upper())
# starting character check function it will return True if correct otherwise False
print(s.startswith("S"))

# List Data structure
print("\n----List in python----")
lang=['csharp','dart','kotlin','java']
print(lang)
number=[2,4,6,8,10]
print(number)
mix=['app',7,2.2]
print(mix)

# slicing in list
print("\n----Slicing in List----")
sli_num=number[1:4]
print(sli_num)

# arithmatic operator (+, -, *, /, ^, %)
# so we are performing type casting here in input function using int 
print("\n----Arithmatic Operators----")
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
print(f"{num1} + {num2} = ", num1+num2)
print(f"{num1} - {num2} = ", num1-num2)
print(f"{num1} / {num2} = ", num1/num2)
print(f"{num1} * {num2} = ", num1*num2)
print(f"{num1} ^ {num2} = ", num1**num2)
print(f"{num1} % {num2} = ", num1%num2)

# conditional Operator (and) (or) (not)
# if else conditions
print("\n----Conditional Operators----")
num1 = int(input("Enter your age: "))
if(num1%2==0 and num1<18):
    print(f"{num1} is even and under 18")
elif(num1%2!=0 and num1<18):
    print(f"{num1} is odd and under 18")
elif(num1%2==0 and num1>18):
    print(f"{num1} is even and above 18")
elif(num1%2!=0 and num1>18):
    print(f"{num1} is odd and above 18")
else:
    print(f"{num1} is even and equal to 18")
        
# comperision operator
# input function always take string as input from user 
# so we are performing type casting here in input function using int 
print("\n----Comperision operators----")
month= int(input("Enter your birthday month:" ))
if(month==1):
    print("January")
elif(month==2):
    print("February")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("June")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
    print("Entered wrong month!!!")

# >= operator with if else conditions
# so we are performing type casting here in input function using int 
marks=int(input("Enter your Marks in AI: "))
if(marks>=85):
    print("Your Grade is A+")
elif(marks>=80):
    print("Your Grade is A")
elif(marks>=75):
    print("Your Grade is B+")
elif(marks>=71):
    print("Your Grade is B")
elif(marks>=68):
    print("Your Grade is B-")
elif(marks>=64):
    print("Your Grade is C+")
elif(marks>=61):
    print("Your Grade is C")
elif(marks>=58):
    print("Your Grade is C-")
elif(marks>=54):
    print("Your Grade is D+")
elif(marks>=50):
    print("Your Grade is D")
else:
    print("Your Grade is F")