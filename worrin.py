# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F
# name=["sam ","harris"]
# i=0
# b=[]
# while i<len(name):
#     j=0
#     while j<len(name[i]):
#         c=name[i][j]==name[i][0]
#         e=name[i][0].upper()
#         b.append(e)
#         d=".".join(b)
#         break
#         j=j+1
#     i=i+1
# print("Sam Harris=>",d)

# def function(name):
#     i=0
#     b=[]
#     while i<len(name):
#         j=0
#         while j<len(name[i]):
#             c=name[i][j]==name[i][0]
#             e=name[i][0].upper()
#             b.append(e)
#             d=".".join(b)
#             break
#             j=j+1
#         i=i+1
#     print("Sam Harris=>",d)
# function(["sam ","harris"])
    

# def my(a):
#     i=0
#     b=[]
#     while i<len(a):
#         # if a[i].isupper():
#         if a[i]<="Z":
#             b.append(a[i])
#             # b.append(i)
#         i=i+1
#     return b
# print(my("HaRrIs"))

list=([(1,9),(5,3),(4,6),(9,12),(4,10)])
i=0
b=[]
while i<len(list):
    j=1
    while j<len(list[i]):
        d=list[i][0]+list[i][1]
        b.append(d)
        j=j+1
    i=i+1
print (b)

    