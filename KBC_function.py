question_list=["what is the capital of India","how many continents are there","which course is being taught in navgurukul"]
option_list=[["chandigarh","bhopal","delhi","chennai"],["four","three","eight","seven"],["software_engineering","tourism","agriculture","counselling"]]
life_line=[["chennai","delhi"],["seven","eight"],["agriculture","software_engineering"]]
life_solution=[2,1,2]
solution_list=[3,4,1]
i=0
count=0
def life(i):
    global count
    if count==0:
        k=0
        while k<len(life_line[i]):
            print(k+1,life_line[i][k])
            k=k+1
        user=int(input("enter your answer:"))
        count=count+1
        if user==life_solution[i]:
            return True
        else:
            return False
    else:
        print("you already used life_line")
        option(i)
        
def option(i):
    j=0
    while j<len(option_list[i]):
        print(j+1,option_list[i][j])
        j=j+1
    user1=("1.without lifeline","2.with lifeline")
    if user1==2:
        return life[i]
    elif user1==1:
        user2=int(input("enter your answer"))
        if user2==solution_list[i]:
            return True
        else:
            return False
        
def Question():
    i=0
    while i<len(question_list):
        print("Q",i+1,question_list[i])
        x=option(i)
        if x==True:
            print("your answer is correct")
        elif x==False:
            print("you lose the game")
            break
        i=i+1
Question()
        

    
# a=[1,2,3]
# i=0
# while i<len(a):
#     j=1
#     while j<len(a):
#         print(a[i]+a[j])
#         j=j+1
#     break
#     i=i+1