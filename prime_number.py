def function_name():
    i=1
    while i<=30:
        count=0
        j=2
        while j<=i//2:
            if i%j==0:
                count=count+1
            j=j+1
        if count==0 and i!=1:
            print(i)
        i=i+1
function_name()
          