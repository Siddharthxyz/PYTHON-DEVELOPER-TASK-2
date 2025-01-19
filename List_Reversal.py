
def reverse_list(numbers):
    return numbers[::-1]
numbers = list(map(int,input("enter a sequence of numbers by space").split()))
rev = reverse_list(numbers)
print(f"original {numbers}")
print("reversed",rev)