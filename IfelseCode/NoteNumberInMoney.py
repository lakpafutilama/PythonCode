amount = int(input("Enter the amount: "))
notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
count = []
for i in notes:
    if (amount >= i):
        c = amount//i
        amount = amount % i
    else:
        c = 0
    count.append(c)
print(f"""
In Rs.{amount}, there are:
1000 notes = {count[0]}
500 notes = {count[1]}
100 notes = {count[2]}
50 notes = {count[3]}
20 notes = {count[4]}
10 notes = {count[5]}
5 notes = {count[6]}
2 notes = {count[7]}
1 notes = {count[8]}
""")
