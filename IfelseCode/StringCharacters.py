# Uppercase, Lowercase, Special Character, or Digit
string = input("Enter anything: ")
count1 = count2 = count3 = count4 = 0
for ch in string:
    if ('a' <= ch <= 'z'):
        count1 += 1
    elif ('A' <= ch <= 'Z'):
        count2 += 1
    elif ('0' <= ch <= '9'):
        count3 += 1
    else:
        count4 += 1
print(f"""
In string '{string}', there are {count1+count2+count3+count4} character.
Among them, there are {count1+count2} alphabets.
Number of Uppercase character={count2}
Number of Lowercase character={count1}
Number of Special character={count4}
Number of digits ={count3}
""")
