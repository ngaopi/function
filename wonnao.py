list=[10,20,30,10,20,30]
i=0
a=[]
b=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    else:
        b.append(list[i])
    i=i+1
j=0
count=0
while j<len(b):
    if b[j]in a:
        count+=1
    j=j+1
print(count)