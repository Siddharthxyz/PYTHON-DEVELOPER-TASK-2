# using bubble sorting
def sort(list):
    for j in range (len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

list = list(map(int,input("enter a sequence of numbers by space").split()))

print(sort(list))