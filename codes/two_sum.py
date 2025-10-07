number = list(map(int,(input("enter the numbers: ")).split(",")))

target = int(input("Enter the target: "))

output = []

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] + number[j] == target:
            output+=i,j
            print(output)
        break

