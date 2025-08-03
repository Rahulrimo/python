num=int(input("enter a  positive number: "))
if num %15 == 0:
    print("The number is divisible by 15")
else:
 if num %3 == 0 or num %5 == 0:
       print("The number is  not divisible by 15 but divisible by 3 or 5")
 else:
    print(" number is neither divisible by 3 nor 5")