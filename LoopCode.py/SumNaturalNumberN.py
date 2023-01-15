n=int(input("Enter the number upto where you want to add natural numbres: "))
sum=0
for i in range(n+1):
    sum+=i
print(f"The sum of natural numbers from 1 to {n} is {sum}.")