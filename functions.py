

def sumOneToN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n= int(input("Enter the n: "))   
output = sumOneToN(n)   
print("sum of all numbers till n  is ", output)
n1 = int(input("Enter  number: "))
output2 = sumOneToN(n1)
print("sum of all numbers till n1 is ", output2)