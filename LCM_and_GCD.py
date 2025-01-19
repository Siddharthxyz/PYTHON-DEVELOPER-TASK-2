import math
num1 = int(input("enter a number 1."))
num2 = int(input("enter a number 2."))

GCD = math.gcd(num1,num2)
LCM = math.lcm(num1,num2)

print(f"GDC of two number {num1} and {num2} is {GCD}")
print(f"LCM of two number {num1} and {num2} is {LCM}")