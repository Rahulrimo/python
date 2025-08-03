eng_marks= int(input("Enter your English marks: "))
math_marks= int(input("Enter your Math marks: "))
if eng_marks > 80 and math_marks > 80:
    print("A grade")
elif eng_marks > 80 or math_marks > 80:
    print("B grade")
else:
    print("C grade")