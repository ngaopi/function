# list=[1,2,[3,4],5,[6,7],8,[9,10]]     
# def my_recursion(k):
#     i=0
#     b=[]
#     sum=0  
#     while i<len(k):
#         if type(k[i])==type([]):
#             j=0
#             while j<len(k[i]):
#                 b.append(k[i][j])
#                 sum=sum+k[j]
#             j=j+1
#         else:
#             b.append(k[i])
#         i=i+1
#     print(sum)
# my_recursion([1,2,[3,4],[5,6],[7,8],10])


# list=[1,2,[3,4],[5,6],[12,3,45]]
# i=0
# b=[]
# while i<len(list):
#     if type(list[i])==type ([]):
#         j=0
#         while j<len(list[i]):
#             b.append(list[i][j]) 
#             j=j+1 
#     else:
#         b.append(list[i]) 
#     i=i+1
# print(b)