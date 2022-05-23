# list="@12,aZ45'BC!df^*"
# i=0
# count=0
# count1=0
# count2=0
# count3=0
# while i<len(list):
#     if list[i].isupper():
#         count=count+1
#     elif list[i].islower():
#         count1+=1
#     elif list[i].isnumeric():
#         count2+=1
#     else:
#         count3+=1
#     i=i+1
# print([count,count1,count2,count3])

def func(list):
    i=0
    count=0
    count1=0
    count2=0
    count3=0
    while i<len(list):
        if list[i].isupper():
            count=count+1
        elif list[i].islower():
            count1+=1
        elif list[i].isnumeric():
            count2+=1
        else:
            count3+=1
        i=i+1
    b=[count,count1,count2,count3]
    return b
print(func("@12,aZ45'BC!df^*"))