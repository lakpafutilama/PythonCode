n=int(input("Enter the number to check number of digit present in it: "))
count=0
number=n
while(n>0):
    n=n//10
    count+=1
print(f"There are {count} dgits in number {number}")