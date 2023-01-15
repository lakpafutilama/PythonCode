from datetime import date


def header():
    print(f"""
            Sunway BhatBhateni Store
              Maitidevi, Kathmandu
                                    Date: {date.today()}
____________*______________*______________*______________
    """)


def inputInfomation():
    custno = int(input("Enter no. of customer : "))
    print("_________________________________________________________")
    allList=[]
    for i in range(custno):
        custID = int(input(f"Enter the customer [Customer {i+1}] id : "))
        custName = input(f"Enter the customer [Customer {i+1}] name : ")
        custAddress = input(f"Enter the customer [Customer {i+1}] address : ")
        custPhone = input(f"Enter the customer [Customer {i+1}] Phone no : ")
        custEmail = input(f"Enter the customer [Customer {i+1}] email : ")
        item = int(input("Enter the numbers of items : "))
        itemTotalPrice = 0
        for j in range(item):
            itemQua = int(input(f"Quantity of item [{j+1}] : "))
            itemUnitPrice = int(input(f"Unit price of item [{j+1}] : "))
            itemTotalPrice += itemQua*itemUnitPrice
            print("Total Price : ", itemTotalPrice)

        singleList=[custID, custName, custAddress, custPhone, custEmail, item, itemTotalPrice]
        allList.append(singleList)
    return custno, allList


def calculation(totalPrice):
    if (totalPrice >= 10000):
        disAmount = 0.1 * totalPrice
    elif (totalPrice >= 8000):
        disAmount = 0.08 * totalPrice
    elif (totalPrice >= 5000):
        disAmount = 0.05 * totalPrice
    else:
        disAmount = 0
    discountedPrice = totalPrice-disAmount
    return disAmount, discountedPrice


def displayOutput(finalList):
    id = finalList[0]
    name = finalList[1]
    address = finalList[2]
    phone = finalList[3]
    email = finalList[4]
    itemNo = finalList[5]
    totalPrice = finalList[6]
    discount = finalList[7]
    discountedPrice = finalList[8]
    print(f"""
Customer id = {id} \t Customer Address : {address} \t Customer Phone : {phone}
Customer email : {email}
Total Price : Rs.{totalPrice} \t\t Discount Amount : Rs.{discount}
After discount Amount : Rs.{discountedPrice}

Dear {name}, your total amount to be paid for {itemNo} items is Rs.{discountedPrice} with 
discount of Rs.{discount}
    """)

  
custNumber, allDataList = inputInfomation()
finalList=[]
for i in range(custNumber):
    singleList=allDataList[i] 
    discount, discountedPrice = calculation(singleList[6])
    singleList+=[discount, discountedPrice] 
    finalList.append(singleList)    

    
for j in range(custNumber):
    breakList=finalList[j]
    header()
    displayOutput(breakList)