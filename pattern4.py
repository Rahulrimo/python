n=int(input("enter a no: "))

for i in range(n): #loop for rows
    for j in range(i+1): #loop for columns
        print(chr(65+j), end="") 
    print()
    