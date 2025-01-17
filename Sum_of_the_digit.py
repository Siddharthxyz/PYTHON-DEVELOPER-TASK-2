n = int(input("enter a number"))
string_n = str(n) # converting the digit into string
sum = 0
for i in string_n:
    sum = sum + int(i)

print(f"number is {n} sum of the digit is {sum}")