# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# tri_recursion(6)


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))
