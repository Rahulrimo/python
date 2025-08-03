def addOne(x):
    x= x + 1
    print("inside function",x)


x = 5
addOne(x)
print("outside function", x)

def modifyList(lst):
    # lst.append(4)
    lst=[8,9,7]
    print("inside function", lst)
    
lst= [1, 2, 3]
modifyList(lst)
print("outside function", lst)