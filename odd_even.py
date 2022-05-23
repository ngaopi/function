def my(list):
    i=0
    even=0
    while i<len(list):
        if list[i]%2==0:
            print(list[i])
        i=i+1
    return even
my([2,4,7,8,9,5])
