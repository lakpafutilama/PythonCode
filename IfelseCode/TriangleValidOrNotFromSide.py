side1=int(input("Enter the length of side 1 in cm "))
side2=int(input("Enter the length of side 2 in cm "))
side3=int(input("Enter the length of side 3 in cm "))
if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")