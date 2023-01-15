num=int(input("Enter a number to find its factorial: "))
sum=1
for i in range(1, num+1):
    sum*=i
print(f"The factorial of {num} is {sum}.")