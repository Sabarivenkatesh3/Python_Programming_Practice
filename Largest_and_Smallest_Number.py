numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("The numbers are:", numbers)

smallest_number = numbers[0]
largest_number = numbers[0]

for i in numbers:
    if i > largest_number:
        largest_number = i
    if i < smallest_number:
        smallest_number = i

print("Largest number:", largest_number)
print("Smallest number:", smallest_number)
