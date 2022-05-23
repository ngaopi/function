def my(name):
    a=len(name)-1
    b=[]
    while a>=0:
        b.append(name[a])
        a=a-1
    if name==b:
        print("pallindrome")
    else:
        print("not pallindrome")
my(['m','a','a','m'])

