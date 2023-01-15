import math

a=int(input("Enter the value of a from the equation "))
b=int(input("Enter the value of b from the equation "))
c=int(input("Enter the value of c from the equation "))
determinant=math.pow(b, 2)-(4*a*c)
print(determinant)
if(determinant==0):
    x=(-b)/(2*a)
    print("It has one roots which is",x)
elif(determinant>0):
    d=math.sqrt(determinant)
    x=(-b+d)/(2*a)
    y=(-b-d)/(2*a)
    print("It has two roots which are",x ,y)
else:
    print("It has no roots.")