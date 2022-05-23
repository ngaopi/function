def my(list):
    i=0
    b=[]
    while i<len(list):
        if list[i]!=list[i-1]:
            b.append(list[i])
        i=i+1
    print(b)
my(list=input("enter the character:"))

    
    