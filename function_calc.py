def calculator(num1,num2):
    choice=input("enter your choice:")
    num1=float(input("enter num1:"))
    num2=float(input("enter num2:"))
    if choice=="1":
        print(num1,"+",num2,"=",(num1+num2))
    elif choice=="2":
        print(num1,"*",num2,"=",(num1*num2))
    elif choice=="3":
        print(num1,"-",num2,"=",(num1-num2))
    elif choice=="4":
        if num2==0.0:
            print("divided by 0 error")
        else:
            print(num1,"/",num2,"=",(num1/num2))
    else:
        print("invalid choice")
calculator("1 addition","choice1")
# calculator("2 multiplication","choice2")
# calculator("3 subtraction","choice3")
# calculator("4 division","choice4")


