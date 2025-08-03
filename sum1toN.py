def sum1toN(n):
    if n == 1:
        return 1
    
    ans= n+sum1toN(n - 1)
    return ans

n = int(input("Enter n: "))
print(sum1toN(n))