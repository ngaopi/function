# Question 5

# Define a function which takes one parameter(positive integer). This function returns the sum of all multiples of 3 and 5 (not neccessary common multiples) in the range 1 to the integer passed as the parameter.

# Input:-

# 10

# 3 aur 5 ke multiples => 3, 5, 6, 9, 10

# Output :-

# 33

# list=[1,2,3,4,5,6,7,8,9,10]
def my(list):
    i=0
    b=[]
    while i<len(list):
        if list[i]%3==0 or list[i]%5==0:
            print(list[i],end=" ")
        i=i+1
my([1,2,3,4,5,6,7,8,9,10])

