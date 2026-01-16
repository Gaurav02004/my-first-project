val = input("Enter the number")
value_float = float(val)
if (value_float >100):
    print("The number is greater than 100")
 
 val = input("Enter the number")
value_float = float(val)
if(value_float % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

## AGE FORM
age = float(input("enter the age"))
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

age = float(input("enter the age")) 
if(age<18):
    print("Minor Age")
elif(age>=18 and age<60):  
    print("Adult Age")
else:
    print("Senior Citizen")

 ## NESTED IF ELSE
 age = float(input("enter the age"))  
if(age>=18):
    print("You are eligible to vote")
    if(age>=60):
        print("You are a senior citizen")
    else:
        print("You are an adult")


 age = float(input("Enter the age"))
if(age<18):
    print("Minor Age")
    if(age<15):
        print("You are in school")
    else:
        print("You are in college")
else:   
       elif(age>=18 and age<60):
    print("Adult Age") 
    elif(age>=60):
        print("Senior Citizen")
        if(age>80):
            print("You are above 80 years")
            
 