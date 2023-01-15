def Staff_Info():
    Staff_No = int(
        input("Please enter the number of staff you wanted to provide data: "))
    all_data = []
    for i in range(1, Staff_No+1):
        Staff_Name = input(f"Enter Staff Name [{i}]: ")
        Staff_Address = input(f"Enter Address [{i}]: ")
        Staff_PanNo = int(input(f"Enter Pan No [{i}]: "))
        Staff_Status = input(f"Enter ‘Y’ for Married and ‘N’ for Unmarried Status [{i}]: ")[0]
        Fiscal_Year = input(f"Enter FY [{i}]: ")
        Monthly_Income = int(
        input(f"Enter Staff per month income [Rs.][{i}]: "))
        data_list = [Staff_Name, Staff_Address, Staff_PanNo, Staff_Status, Fiscal_Year, Monthly_Income]
        all_data.append(data_list)
    return Staff_No, all_data


def Calculate_Tax_Of_Staff(Staff_Status, Monthly_Income):
    flag=True
    if (Staff_Status == 'Y' or Staff_Status == 'y'):
        flag==True
    elif (Staff_Status == 'N' or Staff_Status == 'n'):
        flag=False
    else:
        print("Enter y or n")
        Staff_Status=input(f"Enter ‘Y’ for Married and ‘N’ for Unmarried Status [{i}]: ")[0]
        Calculate_Tax_Of_Staff(Staff_Status, Monthly_Income)
        
    if (flag==True):
        Tax_Rate, Tax_Amount = Calculate_Tax_Of_Staff_Married(Monthly_Income)
    else:
        Tax_Rate, Tax_Amount = Calculate_Tax_Of_Staff_Unmarried(Monthly_Income)
        
    return Tax_Rate, Tax_Amount


def Calculate_Tax_Of_Staff_Married(Monthly_Income):
    Annual_Income = Monthly_Income*12
    if (Annual_Income <= 400000):
        Tax_Rate = 1
        Tax_Amount = 0.01*Annual_Income
    elif (400000 < Annual_Income <= 500000):
        Tax_Rate = 10
        Tax_Amount = 0.1*(Annual_Income-400000)+0.01*400000
    elif (500000 < Annual_Income <= 700000):
        Tax_Rate = 20
        Tax_Amount = 0.2*(Annual_Income-500000)+0.1*100000+0.01*400000
    elif (700000 < Annual_Income <= 1300000):
        Tax_Rate = 30
        Tax_Amount = 0.3*(Annual_Income-700000)+0.2 * \
            200000+0.1*100000+0.01*400000
    else:
        Tax_Rate = 36
        Tax_Amount = 0.36*(Annual_Income-1300000)+0.3 * \
            600000+0.2*200000+0.1*100000+0.01*400000
    return Tax_Rate, Tax_Amount


def Calculate_Tax_Of_Staff_Unmarried(Monthly_Income):
    Annual_Income = Monthly_Income*12
    if (Annual_Income <= 450000):
        Tax_Rate = 1
        Tax_Amount = 0.01*Annual_Income
    elif (450000 < Annual_Income <= 550000):
        Tax_Rate = 10
        Tax_Amount = 0.1*(Annual_Income-450000)+0.1*100000+0.01*450000
    elif (550000 < Annual_Income <= 750000):
        Tax_Rate = 20
        Tax_Amount = 0.2*(Annual_Income-550000)+0.1*100000+0.01*450000
    elif (750000 < Annual_Income <= 130000):
        Tax_Rate = 30
        Tax_Amount = 0.3*(Annual_Income-750000)+0.2 * \
            200000+0.1*100000+0.01*450000
    else:
        Tax_Rate = 36
        Tax_Amount = 0.36*(Annual_Income-1300000)+0.3 * \
            550000+0.2*200000+0.1*100000+0.01*450000
    return Tax_Rate, Tax_Amount


def Display_Static_Info():
    heading = """    
            Sunway  College  Account  Department
                MaitiDevi, Kathmandu
                    Welcome to
            Salary & Tax Calculate System (STCS)
    """
    return heading


def Display_Staff_Info(List):
    Staff_Name = List[0]
    Staff_Address = List[1]
    Staff_PanNo = List[2]
    Staff_Status = List[3]
    Fiscal_Year = List[4]
    Monthly_Income = List[5]
    Tax_Rate = List[6]
    Tax_Amount = List[7]
    Deducted_Income=Monthly_Income-(Tax_Amount/12)
    print(f"""
    Staff Name: {Staff_Name} \t\t Address: {Staff_Address}
    PAN No: {Staff_PanNo}  \t FY: {Fiscal_Year} \t Married Status= {Staff_Status}
    Monthly Income= {Monthly_Income} \t Monthly Income After Tax Deduction= {Deducted_Income}

    Staff {Staff_Name} with PAN {Staff_PanNo} fall under {Tax_Rate}%  Tax salb.
    {Staff_Name} (PAN {Staff_PanNo}) to pay tax to government is = Rs.{Tax_Amount} per year
______________________________________________________________________________________
    """)


def fileWriting(Staff_No, heading, newAllData):
    fileName = "TaxOutput.txt"
    for i in range(Staff_No):
        List = newAllData[i]
        Staff_Name = List[0]
        Staff_Address = List[1]
        Staff_PanNo = List[2]
        Staff_Status = List[3]
        Fiscal_Year = List[4]
        Monthly_Income = List[5]
        Tax_Rate = List[6]
        Tax_Amount = List[7]
        Deducted_Income=Monthly_Income-(Tax_Amount/12)
        f = open(fileName, "a")
        f.write(f"Staff: {i+1}")
        f.write(heading)
        f.write(f"""
        Staff Name: {Staff_Name} \t\t Address: {Staff_Address}
        PAN No: {Staff_PanNo}  \t FY: {Fiscal_Year} \t Married Status= {Staff_Status}
        Monthly Income= {Monthly_Income} \t Monthly Income After Tax Deduction= {Deducted_Income}

        Staff {Staff_Name} with PAN {Staff_PanNo} fall under {Tax_Rate}%  Tax salb.
        {Staff_Name} (PAN {Staff_PanNo}) to pay tax to government is = Rs.{Tax_Amount} per year
    
        """)
    f.close()


Staff_No, all_dataList = Staff_Info()
newAllData = []
for i in range(Staff_No):
    ListElementAdd = all_dataList[i]
    Staff_Status = ListElementAdd[3]
    Monthly_Income = ListElementAdd[5]
    Tax_Rate, Tax_Amount = Calculate_Tax_Of_Staff(Staff_Status, Monthly_Income)
    ListElementAdd.append(Tax_Rate)
    ListElementAdd.append(Tax_Amount)
    newAllData.append(ListElementAdd)

heading = Display_Static_Info()
print("Output")
for i in range(Staff_No):
    singleList = newAllData[i]
    print(heading)
    Display_Staff_Info(singleList)

fileWriting(Staff_No, heading, newAllData)