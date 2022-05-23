def num(a):
    i=0
    while i<len(a):
        if a[i]!=1:
            return False
        i=i+1
    return True
print(num([1,1,1]))