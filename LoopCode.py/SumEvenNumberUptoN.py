n=int(input("Enter the number up to which you have to sum: "))
sum=0
for i in range(n+1):
    if(i%2==0):
        sum+=i
print(f"The sum of all even natural numbers upto {n} is {sum}")