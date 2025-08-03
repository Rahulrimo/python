# def printHello():
#     print("Hello, World!")
    
# printHello()

# def add(n1=0,n2=0):
#     print("n1:", n1)
#     print("n2:", n2)
#     sum=n1+n2
#     return sum 


# # print("the sum is", add(3,2))

# print("the sum is", add(3))

# def addAllNumbers(*args):
   
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# output= addAllNumbers(1, 2, 3, 4, 5)
# print("The sum of all numbers is:", output)

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
        
        
studentInfo(name="John", age=20, grade="A", city="New York")
studentInfo(name="Alice",age=22, grade="B", city="Los Angeles")