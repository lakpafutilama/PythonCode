num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
list1=[]
list2=[]
for i in range(1, 11):
    list1.append(i*num1)
    list2.append(i*num2)
cm=set(list1).intersection(list2)
list=list(cm)
print(f"The LCM of {num1} and {num2} is {list[0]}")