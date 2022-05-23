# list=[55,23,00]
# i=0
# sum=""
# while i<=len(list):
#     sum=sum+str(list[i])
#     i+=1
# print(sum)
    
# def func(x):
#     i=0
#     sum=''
#     while i<len(x):
#         sum=sum+str(x[i])
#         i=i+1
#     return sum
# print(func([55,23,10]))

list=["r","i","n","g","n","i","m"]
i=0
a=[]
while i<len(list):     
    count=0
    j=0
    b=[]
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    b.append(list[i])
    b.append(count)
    if b not in a:
        a.append(b)
    i=i+1
print(a)