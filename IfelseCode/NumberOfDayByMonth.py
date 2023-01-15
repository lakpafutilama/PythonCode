year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
if (1 <= month <= 12):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print("There are 31 days in month",month)
    elif(month==4 or month==6 or month==9 or month==11):
        print("There are 30 days in month",month)
    elif(month==2):
        if(year%4==0 and year%100!=0 or year%400==0):
            print("There are 29 days in month",month)
        else:
            print("There are 28 days in month",month)
    else:
        print(month," is invalid month.")
else:        
    print(year," is invalid year.")