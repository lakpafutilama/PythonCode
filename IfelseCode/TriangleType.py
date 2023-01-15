side1=int(input("Enter the length of side 1 in cm "))
side2=int(input("Enter the length of side 2 in cm "))
side3=int(input("Enter the length of side 3 in cm "))
if(side1==side2==side3):
    print("The triangle is equilateral triangle.")
elif(side1==side2 or side2==side3 or side1==side3):
    print("The triangle is isosceles triangle.")
else:
    print("The triangle is scalene triangle.")