

# def func(list):
#     i=0
#     while i<len(list)-1:
#         if list[i]==list[i+1]:
#             return True
#         i=i+1
#     return False
# print(func(list="moon"))

# list="123456"
# a=str(list)
# d=a
# i=0
# b=[]
# while i<len(list):
#     c=d[i]+d[i+1]
#     b.append(c)
#     i=i+1
# print(b)

# # list=[20,2,9,4,1,6]
# # i=0
# # b=[]
# # while i<len(list)-1:
# #     c=list[i]+list[i+1]
# #     b.append(c)
# #     i=i+1
# # print("addition of list =",b)
# # j=0
# # max=0
# # while j<len(b):
# #     if b[j]>max:
# #         max=b[j]
# #     j=j+1
# # print("maximum =",max)
# # d=max*max
# # print("square of max =",d)

# list="12345"
# i=0
# b=[]
# while i<len(list):
#     b.append(int(list[i]))
#     i=i+1
# print(b)
# j=0
# c=[]
# while j<len(b)-1:
#     d=b[j]+b[j+1]
#     c.append(d)
#     j=j+1
# print(c)
# k=0
# max=0
# while k<len(c):
#     if c[k]>max:
#         max=c[k]
#     k=k+1
# print(max)
# print(max*max)

list="12345"
i=0
a=[]
while i<len(list)-1:
    s=int(list[i])+int(list[i+1])
    a.append(s)
    i=i+1
print(a)
j=0
m=0
while j<len(a):
    if a[j]>m:
        m=a[j]
    j=j+1
print(m)
print(m*m)    
    
