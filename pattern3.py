n=int(input("Enter a number: "))
for i in range(1,n+1):  # loop for rows
    for j in range(1, i + 1):  # loop for columns
        print(j, end="")
    print()  # move to the next line after each row