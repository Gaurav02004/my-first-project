# import math
# math.ceil(43.67)
# math.floor(43.67)
# math.sqrt(64)
# math.factorial(5)
# math.gcd(12,15)
# math.pow(2,3)
# math.log10(1000)
# math.sin(90)
# math.cos(0)
# math.tan(45)
# math.radians(180)
# math.degrees(3.14)
# math.exp(2)
# math.pi


## PROGRAM TO CHECK PRIME NUMBER

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

## PROGRAM TO CHECK MAX OF 3 NUMBERS

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# if (a >= b) and (a >= c):
#     print(a, "is the largest number")
# elif (b >= a) and (b >= c):
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")


## PROGRAM TO PRINT MULTIPLICATION TABLE

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, 'x', i, '=', num*i)


## PROGRAM TO FIND FACTORIAL OF A NUMBER

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print("The factorial of", num, "is", factorial)


## PROGRAM TO CHECK EVEN OR ODD

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")


## PROGRAM TO PRINT FIBONACCI SERIES

# terms = int(input("Enter the number of terms: "))
# n1, n2 = 0, 1
# count = 0
# if terms <= 0:
#     print("Please enter a positive integer")
# elif terms == 1:
#     print("Fibonacci sequence upto", terms, ":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < terms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

## PROGRAM TO CHECK ARMSTRONG NUMBER

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")




