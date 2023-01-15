import datetime


def displayHeader():
    print(f"""
_____________________________________________________________________________
        WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
                MAITIDEVI, KATHMANDU
                                        Date :{datetime.date.today()}
_____________________________________________________________________________        
    """)


def takeInformation():
    name = input("Enter your name : ")
    inputString = input("Enter any character to check : ")
    return name, inputString


def checkInput(inputString):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(0, len(inputString)):
        if ('A' <= inputString[i] <= 'Z'):
            a += 1
        elif ('a' <= inputString[i] <= 'z'):
            b += 1
        elif ('0' <= inputString[i] <= '9'):
            c += 1
        else:
            d += 1
    return a, b, d, c


def displayOutput(name, inputString, upperCase, lowerCase, specialCharacter, numericData):
    print(f"""
    Dear {name}, the string '{inputString}' you entered consist of :
    Number of UpperCase           = {upperCase}
    Number of LowerCase           = {lowerCase}
    Number of Special Character   = {specialCharacter}
    Number of Numeric Data        = {numericData}
    
    \t\t Thank you for the visit
    """)

displayHeader()
name, inputString = takeInformation()
upperCase, lowerCase, specialCharacter, numericData = checkInput(inputString)
print()
print("Output of System")
displayHeader()
displayOutput(name, inputString, upperCase, lowerCase, specialCharacter, numericData)