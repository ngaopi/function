# print("navgurukul")
# def say_hello():
#     print("hello")
#     print("how are you")
# say_hello()
# print("python is awesome")
# say_hello()
# print("hello....")
# say_hello

#     5 TYPES OF ARGUMENT

#    1. POSITIONAL ARGUMENT
# def my_function(a,b):
#     add=a+b
#     return add
# print(my_function(1,2)) 

#    2. DEFAULT ARGUMENT
# def my_function(a="x"):
#     print(a)
# my_function()

#    3. KEYWORD ARGUMENT
# def my_function(child3, child2, child1):
#       print("The youngest child is "+child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#     4. ARBITRARY KEYWORD ARGUMENT
# def my_function(**kid):
#       print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")

#        5. ARBITRARY ARGUMENTS
# def my_function(*kids):
#       print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")