num = int(input("enter a number "))\

if num <= 0:
    print("wrong input")
else:
    def prime_no(num):
        for i in (2,num):
            if num % i == 0:
                return False
            return  True
result = prime_no(num)
print(result)
