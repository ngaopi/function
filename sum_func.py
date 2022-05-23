# l=[5,4,0,1,9]
# i=0
# b=[]
# while i<len(l):
#     d=l[i]+l[-(i+1)]
#     b.append(d)
#     if len(b)==2:
#         break
#     i=i+1
# print(b)


list='1,2,4,5,3,7,2'
a=int(list)
i=0
b=[]
while i<len(a):
    d=int(a[i])+int(a[i+1])
    b.append(d)
    i=i+1
    

