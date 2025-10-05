num = list(map(int, input("enter the numbers: ").split()))

first_largest = 0
second_largest = 0

for i in num:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i

print(second_largest)

### another method
"""num.sort()
print("largest: ",num[-1])
print("second_largest: ",num[-2])"""