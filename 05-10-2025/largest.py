num = list(map(int, input("enter the numbers: ").split()))
print(num)

largest = 0

for i in num:
    if i>largest:
        largest = i
    
print(largest)