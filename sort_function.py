# using sort function sort the given list
unorder_list=[6,8,4,3,9,56,1,34,7,15]
def unorder(list):
    i=0
    while i<len(list):
        j=0
        while j<len(list)-1:
            if list[j]<list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
            j=j+1
        i=i+1
    return list
print(unorder([6,8,4,3,9,56,0,34,7,15]))
