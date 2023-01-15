basicSalary=int(input("Enter your basic salary in Rupees: "))
years=int(input("Enter years of experience: "))
grossSalary=basicSalary
if(years>=5):
    grossSalary+=0.1*basicSalary
else:
    grossSalary+=0.05*basicSalary
print("The gross salary of the employee is Rs.",grossSalary)