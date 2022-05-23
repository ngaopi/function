# Question 6

# Define a function that checks the speed of drivers. This function will take a parameter named speed, and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3. If points are more than 12, print “License suspended”

# Input:-

# 85
# 135

# Output :-

# 3
# “License suspended”

def driver_license(speed):
    if speed<70:
        print("70")
    elif speed>70:
        i=71
        j=0
        while i<=speed:
            if i%5==0:
                j=j+1
            i=i+1
        if j>12:
            print("license suspended")
        else:
            print(j)
driver_license(85)
driver_license(135)
            
            
            
            
# list=["abc def"] 
# i=0
# b=[]
# while i<len(list):
#     c=list[i].replace(" ","")
#     b.append(c)
#     i=i+1
# print(b)


    
     
    