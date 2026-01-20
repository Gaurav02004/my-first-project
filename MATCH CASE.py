# x = int(input("Enter a number: "))
# match x:
#     case 0:
#         print("You entered zero")
#     case 1:
#         print("You entered one")
#     case 2:
#         print("You entered two")
#     case _: 
#         print("You entered a number other than 0, 1, or 2")


day = input("Enter the day of the week: ").lower()
match day:
    case "monday":
        print("It's the start of the work week!")

    case "friday":
        print("It's almost the weekend!")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular weekday.")
fruit = input("Enter a fruit name: ").lower()
match fruit:

    case "apple":
        print("Apples are red or green.")

    case "banana":
        print("Bananas are yellow.")
    case "orange":
        print("Oranges are orange.")








