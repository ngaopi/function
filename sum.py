
# list=[1,7,9]
# i=0
# b=[]
# sum=0
# while i<len(list):
#     b.append(list[i])
#     sum=sum+list[i]
#     c=[sum]
#     i=i+1
# print(b+c)

def num(list):
    i=0
    b=[]
    sum=0
    while i<len(list):
        b.append(list[i])
        sum=sum+list[i]
        c=[sum]
        i=i+1
    print(b+c)
num([1,7,9])