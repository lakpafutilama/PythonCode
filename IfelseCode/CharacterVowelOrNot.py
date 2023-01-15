character = input("Enter a character: ")
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if character in vowels:
    flag = True
else:
    flag = False
if(flag==True):
    print(character," is vowel.")
else:
    print(character," is consonant.")