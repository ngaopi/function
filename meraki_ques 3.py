# write a function named add_numbers which takes two numbers as arguments and then print
# their sum.the name of the arguments should be number1 and number2.

# def add_numbers(number1,number2):
#     add=number1+number2
#     return add 
# print(add_numbers(56,12))

# write a function named add_numbers_list which takes 2 list of two integers and then
# print the sum of the integers with the same position.
def add_numbers_list(list1,list2):
    i=0
    b=[]
    while i<len(list1):
        j=0
        while j<len(list2):
            d=list1[i]+list2[j]
            b.append(d)
            j=j+1
            i=i+1
    return b
print(add_numbers_list([50,60,10],[10,20,13]))