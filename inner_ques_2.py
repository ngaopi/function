# Question 2

# Perfect Number?
# A perfect number is the one which is equal to the sum of all it's factors(including 1 and excluding itself).

# Define a function named perfect() which takes one argument(integer) and checks if it is a perfect number or not. Now use this code to write a program that prints all the perfect numbers between 1-1000.

# Example:-

# 6 ek perfect number hai 6=1+2+3.

# Expected Output :-

# 6,28,496

def func():
    user=int(input("enter the number:"))
    sum=0
    i=1
    while i<user:
        if user%i==0:
            sum=sum+i
        i=i+1
    if user==sum:
        print("perfect")
    else:
        print("not perfect")
func()
    
   