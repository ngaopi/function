a=[1,2,3,4]
b=[5,6,7,8]
i=0
j=0
k=0
c=[]
d=[]
e=[]
while i<len(a):
    c.append(a[-i-1])
    d.append(b[-j-1])
    e.append((a[-i-1])+(b[-j-1]))
    k=k+1
    j=j+1
    i=i+1
print("a=",c)
print("b=",d)
print("p=",e)

# o/p a=[4,3,2,1]
#     b=[8,7,6,5]
#     p=[12,10,8,6]
