
list=[[1,2,3],[4,5],[6,2]]
i=0
d=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if i>0:
            d=d+list[i][-1]
            break
        else:
            d=d+list[i][j]
        j=j+1
    i=i+1
print(d)