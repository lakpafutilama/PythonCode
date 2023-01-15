import datetime


def displayHeader():
    print(f"""
__________________________________________________________________________________________
                Sunway Int'l Electricity Billing System")
                      Maitidevi, Kathmandu")
                                                     Date:,{datetime.date.today()}
__________________*_________________*_________________*_________________*_________________""")


def inputInformation():
    custno = int(input("Enter no. of customer : "))
    allCustomerList=[]
    for i in range(custno):
        name = input(f"Enter the owner's name [Customer {i+1}]: ")
        address = input(f"Enter the owner's address [Customer {i+1}]: ")
        unit = int(input(f"Enter the total unit consume [Customer {i+1}]: "))
        individualList=[name, address, unit]
        allCustomerList.append(individualList)
    return custno, allCustomerList


def calculateUnit(unit):
    discount = 0
    if (unit <= 20):
        charge = unit*4
    elif (20 < unit <= 50):
        charge = (unit-20)*7.5+20*4
    elif (50 < unit <= 150):
        charge = (unit-50)*9.5+30*7.5+20*4
        discount = (unit-50)*9.5*0.05
    elif (150 < unit <= 250):
        charge = (unit-150)*11.5+100*9.5+30*7.5+20*4
        discount = (unit-150)*11.5*0.1+100*9.5*0.05
    else:
        charge = (unit-250)*13.5+100*11.5+100*9.5+30*7.5+20*4
        discount = (unit-250)*13.5*0.15+100*11.5*0.1+100*9.5*0.05
    totalCharge = charge-discount
    return charge, discount, totalCharge


def displayInformation(name, address, unit, charge, discount, totalCharge):
    print(f"""
    Customer name : {name} \t\t Customer Address : {address}
    Consume unit : {unit} units
    Total Amount to pay = Rs.{charge} \t Total discount amount : Rs.{discount}
    After discount amount = Rs.{totalCharge}
    Customer {name}, address {address} where consumed unit {unit} units has to pay amount Rs.{charge}
    and After discount amount Rs.{discount}, you got total discounted amount Rs.{totalCharge}
    """)

# call 
customerNo, allCustomerData = inputInformation()
allDataList=[]
for i in range(customerNo):
    singleList=allCustomerData[i]
    charge, discount, totalCharge = calculateUnit(singleList[2])
    singleList+=[charge, discount, totalCharge]
    allDataList.append(singleList)

for i in range(customerNo):
    individualList=allDataList[i] 
    displayHeader()
    displayInformation(individualList[0], individualList[1], individualList[2], individualList[3], individualList[4], individualList[5])