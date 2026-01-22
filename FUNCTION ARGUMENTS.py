# def average(a=9,b=1):
#     print("The average is ", (a+b)/2)


# def name(fname, mname ="jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
#     name("Amy", "Agarwal", "jain")


# VARIABLE LENGTH ARGUMENTS

# def average(*numbers):
#     for i in numbers:
#         sum = sum + i
#         print("Average is:", sum/len(numbers))
#         average(5,6,7,1)


def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
    name(mname = "Buchanan", lname = "Barnes", fname ="james")


