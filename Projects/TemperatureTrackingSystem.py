import calendar
from datetime import date

def initialDisplay():
    print(f"""
        Sunway Temperature Record Management System
                    Kathmandu Nepal
                     {date.today().day} {calendar.month_name[date.today().month]} {date.today().year} 
    _______________________________________________________________
    """)

def inputTemp():
    daysNo=int(input("How many days to record? "))
    print(f"Please enter {daysNo} days temperature readings")
    tempData=[]
    for i in range(1, daysNo+1):
        temperature=int(input(f"Temperature day[{i}]= "))
        tempData.append(temperature)
    return daysNo, tempData

def calculationTemperature(tempData):
    sum=0
    for i in range(len(tempData)):
        sum+=tempData[i]
    average=sum/len(tempData)
    return average

def categoryCheck(tempData):
    count1=0
    count2=0
    count3=0
    countData=[]
    categoryData=[]
    for i in range(len(tempData)):
        temperature=tempData[i]
        if(temperature>=85):
            tempCategory="Very hot"
            count1+=1
        elif(60<temperature<85):
            tempCategory="Pleasant day"
            count2+=1
        else:
            tempCategory="Very cold"
            count3+=1
        categoryData.append(tempCategory)
    countData+=[count1, count2, count3]
    return categoryData, countData

def finalDisplay(daysNo, tempData, average, categoryData, countData):
    print(f"""
    ___________________________________________________________________
    Daily Temperature Report

    ___________________________________________________________________
    """)
    for i in range(daysNo):
        print(f"\tTemperature day [{i+1}]={tempData[i]} Celsius {categoryData[i]}")

    print(f"""

    The average tep for {daysNo} days ={average} Celsius
    Number of hot days={countData[0]} day/s
    Number of pleasant days={countData[1]} day/s
    Number of cold days={countData[2]} day/s
    ___________________________________________________________________
    """)

initialDisplay()
daysNo, tempData=inputTemp()
average=calculationTemperature(tempData)
categoryData, countData=categoryCheck(tempData)
initialDisplay()
finalDisplay(daysNo, tempData, average, categoryData, countData)