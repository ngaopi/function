#  by using the reverse function print the reverse orderof the list

def num(list):
    i=0
    l=[]
    while i<len(list):
        l.append(list[-i-1])
        i=i+1
    return l 
print(num(["M","I","N","G","N","I","R"]))


