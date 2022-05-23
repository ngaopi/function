# def num(list):
#     i=0
#     sum=0
#     b=[]
#     while i<len(list):
#         sum=sum+list[i]
#         b.append(sum)
#         i=i+1
#     return b
# print(num([1,2,3,4,5]))
        

def num(list):
    user=int(input("enter the number:"))
    i=0
    b=[]
    while i<len(list):
        j=0
        c=[]
        while j<len(list):
            if list[i]+list[j]==user:
                c.append(i)
                c.append(j)
            j=j+1
        b.append(c)
        i=i+1
    return b
print(num([1,2,3,4,5,6,7,8,9]))
