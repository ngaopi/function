user=int(input("enter your amount:"))
def indian():
    rupee=user*75
    print(rupee)
def us():
    dollar=user/75
    print("$",dollar)
def choice():
    user=input("enter your choice:")
    if user=="$":
        us
    else:
        indian()
choice()    
    