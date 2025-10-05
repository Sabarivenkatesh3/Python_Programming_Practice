numbers = list(map(int, input("enter the numbers: ").split()))

output = []


for i in range(len(numbers)):
    if numbers[i]%3 == 0 and numbers[i]%5==0:
        output.append(numbers[i])

print(output)

