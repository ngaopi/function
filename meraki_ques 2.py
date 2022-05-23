# write a function named function_print_lines which take 2strings, and print them in 
# the following manner.
def function_print_lines(name,status):
    print("My name is",name)
    print("Iam the",status,"of Navgurukul")
function_print_lines("rishab","co-founder")

# you have to define a function named students and pass a parameter to the functio
# which takes a list of students name(dont use the list).

def my_function(*name):
    i=0
    while i<len(name):  
        print(i+1,"My name is",name[i])
        i=i+1
my_function("rishab","atta","suraj","bob")
##or

def my_function(name):
    i=0
    while i<len(name):  
        print(i+1,"My name is",name[i])
        i=i+1
my_function(["rishab","atta","suraj","bob"])

# you have to define a function named isgreater than 20 in which you have to pass
# two parameters to the function and the first parameter by default should be 20.
def my_function(name,mark=20):
    print(name,mark)
my_function("kartik mark is")
my_function("sonu mark is",40)
my_function("vishal mark is",50)
my_function("umesh mark is",67)

    