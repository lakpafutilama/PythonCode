def remove_chars(s, n):
    return string[n:]

string=input("Enter string: ")
number=int(input("Enter number of characters to be remove from first: "))
newstring=remove_chars(string, number)
print("The string after removing n characters is ",newstring)