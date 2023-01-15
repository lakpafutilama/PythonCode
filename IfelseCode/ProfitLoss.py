cp=int(input("Enter the cost price in Rupees: "))
sp=int(input("Enter the selling price in Rupees: "))
if(sp==cp):
    print("There is neither profit nor loss.")
elif(sp>cp):
    print(f"The profit is Rs.{sp-cp}")
else:
    print(f"The loss is Rs.{cp-sp}")