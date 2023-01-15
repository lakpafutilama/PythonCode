year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
day=int(input("Enter the day: "))
if(1800<=year<=9999 and 1<=month<=12):
    if(0<day<=31 and month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        flag=True
    elif(0<day<=30 and month==4 or month==6 or month==9 or month==11):
        flag=True
    elif(0<day<=28 and month==2):
        flag=True
    elif(day==29 and month==2 and year%4==0 and year%100!=0 or year%400==0):
            flag=True
    else:
        flag=False
else:
    flag=False  
if(flag==True):
    print(f"{month}/{day}/{year} is valid and correct.")
else:        
    print(f"{month}/{day}/{year} is not valid and incorrect.")