# mplement a function named generateRange(min, max, step), which takes three arguments and
# generates a range of integers from min to max, with the step. The first integer is the minimum value,
# the second is the maximum of the range and the third is the step. (min < max)
# Task
# Implement a function named
# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# Note
# min < max
# step > 0
# the range does not HAVE to include max (depending on the step)

# def my(list):
#     i=0
#     while i<len(list):
#         print(list[0:10:3])
#         i=i+1
#         break
# my(list([1,2,3,4,5,6,7,8,9,10]))


def range(min, max, step):
    i=min
    a=[]
    while i<=max:
        a.append(i)
        i=i+step
    return a
min=int(input("enter your number: "))
max=int(input("enter your number: "))
step=int(input("enter your number: "))
print(range(min,max,step))