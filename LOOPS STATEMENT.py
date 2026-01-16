# first = [1,2,3,4,5]
# for num in first:
#     print(num)


# first = [10,20,30,40,50]
# for num in first:
#     print(num**2)   


## FIND THE SUM OF ALL THE ELEMENTS IN THE LIST

# first = [1,2,3,4,5,6,7]
# sum = 0
# for i in first:
#     sum = sum + i
#     print(sum)

## FIND THE SUM OF EVEN AND ODD NUMBERS
first = [1,2,3,4,5,6,7,8,9,10]
even_sum = 0
odd_sum = 0
for i in first:
    if(i % 2 == 0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

