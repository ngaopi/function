list="navgurukul is residential program"
a=[]
s=""
for i in list:
    if i==" ":
        a.append(s)
        s=""
    else:
        s=s+i
if s:
    a.append(s)
print(a)
  