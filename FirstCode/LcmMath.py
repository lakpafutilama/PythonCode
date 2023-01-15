import math

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
gcd=math.lcm(num1, num2)
lcm=(num1*num2)//gcd
print("The LCM of {num1} and {num2} is {lcm}.")