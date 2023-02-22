mark=int(input("enter the marks:"))

if mark>=90:
    print("Grade A")
elif mark >=80 and mark<=89:
    print("Grade B")
elif mark>=60 and mark <= 79:
    print("Grade C")
else:
    print("Failed,Please re-attempt")