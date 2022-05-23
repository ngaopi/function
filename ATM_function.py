# language=["english","hindi"]
# def func():
#     print("insert your ATM")
#     print("welcome to the State Bank of India")
#     pin_code=int(input("enter your pin number:"))
#     balance=30000
#     pin=1234
#     if pin_code==pin:
#         print("1: cash_withdrawal")
#         print("2: balance_enquiry")
#         print("3: deposit")
#         print("4: pin_generation")
#         print("5: exit")
#         transaction=int(input("please choose the transaction:"))
#         if transaction==1:
#             withdrawal=int(input("enter the withdrawal amount:"))
#             if withdrawal<=balance:
#                 print("please collect your cash",withdrawal)
#                 print("remaining balance",balance-withdrawal)
#             else:
#                 print("not enough cash in your account")
#         elif transaction==2:
#             print("your balance",balance)
#         elif transaction==3:
#             deposit=int(input("enter the deposit amount:"))
#             if pin_code==pin_code:
#                 print("total amount",balance+deposit)
#         elif transaction==4:
#             pin_generation=int(input("enter the new pin:"))
#             if pin_code==pin_code:
#                 print("new_pin:",pin_generation)
#         elif transaction==5:
#             print("thank you for visiting")
#     else:
#         print("incorrect pin")
# def lan():
#     user=input("enter your choice: ")
#     if user==language[0]:
#         func()
#     else:
#         print("sorry we don't have hindi option" )
# lan()


language=["english","hindi"]
transaction=["balance_enquiry","cash withdrawl","deposit","pin_generation","quit"]
def function():
    pin=1234
    balance=50000
    user=int(input("enter the option:"))
    if user==1:
        print("balance_enquiry")
        print("enter your pin")
        user=int(input("enter your pin"))
        if user==pin:
            print("your account balance=",balance)
    elif user==2:
        print("cash withdrawl")
        user=int(input("enter the pin:"))
        if pin==user:
            withdrawal=int(input("enter the amount:"))
            print("please collect your cash:",withdrawal)
            print("remaining balance=",balance-withdrawal)
            if withdrawal>balance:
                print("not enough cash in your account")
    elif user==3:
        print("deposit")
        amount=int(input("enter the amount"))
        current_balance=balance+amount
        print("total amount= ",current_balance)
    elif user==4:
        print("pin_generation")
        if pin==pin:
            new_pin=int(input("enter the new_pin number"))
            pin=new_pin
            print("new_pin = ",pin,"\n","thank you for visiting SBI bank")
    else:
        print("quit\nthank you for visiting the SBI bank")
def code():   
    print("welcome to SBI world")
    print("insert your card\ndo not remove it until the transaction is completed")
    i=0
    while i<len(language):
        user1=input("choose your language:")
        if user1==language[i]:
            print("english")
            print("select your option\n1.balance_enquiry\n2.cash withdrawl\n3.deposit\n4.pin_generation\n5.quit")
            return(function())
        else:
            break
code()