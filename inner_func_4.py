# Define a function which takes one argument which is the limit upto which the function has to print the numbers and their label(even or odd) as shown below.

# For example :-

# Input:-

# 3

# Output :-

# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

user=int(input("enter the number:"))
i=0
while i<=user:
    if i%2==0:
        print("even")
    else:
        print("odd")
    i=i+1