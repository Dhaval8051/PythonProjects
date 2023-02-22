mark=int(input("enter the marks:"))
if mark<=100 and mark>=0:
    if mark<=100 and mark>=90:
         print("Grade A")
    elif mark<=89 and mark>=80:
         print("Grade B")
    elif mark<=79 and mark>=60:
         print("Grade c")
    else:
         print("Grade F")