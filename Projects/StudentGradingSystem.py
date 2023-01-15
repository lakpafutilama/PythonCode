import datetime

def displayHeader():
    print(f"""
__________________________________________________________________________
             Sunway Int'l College Grading System
                      Maitidevi, Kathmandu
                                                    Date:{datetime.date.today()}
______________*______________*______________*______________*______________""")

def takeInput():
    studentNo = int(input("Enter number of students : "))
    allStudentData=[]
    for i in range(studentNo):
        StudentName = input(f"Enter name of Student [Student {i+1}]: ")
        StudentAddress = input(f"Enter student's address [Student {i+1}]: ")
        StudentFaculty = input(f"Enter the faculty of student [Student {i+1}]: ")
        StudentIntake = input(f"Enter the intake of Student {i+1}: ")
        ap, mp, dsa, be, sgc=input("Enter the marks obtained in Applied programming, Mobile Programming, Data structure and Algorithm, Basic Entrepreneurship, Small Group Communication : ").split(",")
        list=[StudentName, StudentAddress, StudentFaculty, StudentIntake, ap, mp, dsa, be, sgc]
        allStudentData.append(list)
    return studentNo, allStudentData

def calculateGrade(ap, mp, dsa, be, sgc):
    perc=(int(ap)+int(mp)+int(dsa)+int(be)+int(sgc))/5
    if(perc>90):
        grade="A+"
    elif(90>=perc>80):
        grade="A"
    elif(80>=perc>70):
        grade="B+"
    elif(70>=perc>60):
        grade="B-"
    elif(60>=perc>50):
        grade="B"
    elif(50>=perc>40):
        grade="C+"
    elif(40>=perc>30):
        grade="D"
    else:
        grade="F"
    return grade

def displayInformation(StudentName, StudentAddress, StudentFaculty, StudentIntake, grade):
    print(f"""
Student Name    : {StudentName} \t\t Student Address   : {StudentAddress}
Student Faculty : {StudentFaculty} \t\t\t\t Student Programme : BCS
Student Intake  : {StudentIntake}
______________*______________*______________*______________*______________

Student named {StudentName} has got Grade {grade}
__________________________________________________________________________""")

#call

studentNo, allStudentData = takeInput()
finalDataList=[]
for i in range(studentNo):
    singleList=allStudentData[i]
    grade=calculateGrade(singleList[4], singleList[5], singleList[6], singleList[7], singleList[8])
    singleList+=[grade]
    finalDataList.append(singleList)

for i in range(studentNo):
    singleList=finalDataList[i]
    displayHeader();
    displayInformation(singleList[0], singleList[1], singleList[2], singleList[3], singleList[9])