numbers = list(map(int,(input("enter the number: ")).split(",")))

print("Numbers before removing duplicates: ",numbers)

duplicate = list(set(numbers))
print("Numbers after removing duplicates: duplicate: ",duplicate)

