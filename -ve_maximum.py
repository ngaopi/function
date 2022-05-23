
def max(list):
    i=0
    max=0
    a=list[i]
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
        j=0
        while j<len(list):
            if max>list[j] and list[j]>a:
                a=list[j]
            j=j+1
        print(a)
        break
max([-1,-2,-3,-4,-5])
