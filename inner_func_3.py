# Question 3

# 3

# Create a function which takes 3 arguments(all integers) and prints their sum and average as shown below.

# Input:-

# Enter first number :-3

# Enter second number :-4

# Enter third number:-5

# Output :-

# Sum of three numbers :-12
# Average of three numbers :-4

# user1=int(input("enter the number1:"))
# user2=int(input("enter the number2:"))
# user3=int(input("enter the number3:"))
def func():
    user1=int(input("enter the number1:"))
    user2=int(input("enter the number2:"))
    user3=int(input("enter the number3:"))
    i=0
    sum=0
    while i>=0:
        sum=user1+user2+user3
        print("sum is=",sum)
        i=i+1
        break
    avg=sum//3
    print("average of sum is=",avg)
func()
        
