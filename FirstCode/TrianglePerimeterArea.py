import math
side1=int(input("Enter the length of side 1 in cm "))
side2=int(input("Enter the length of side 2 in cm "))
side3=int(input("Enter the length of side 3 in cm "))
perimeter=side1+side2+side3
s=perimeter/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(f"The perimeter of triangle is {perimeter}cm and area of triangle is {area}sq cm")