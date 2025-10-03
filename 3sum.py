numbers = list(map(int,(input("enter the number: ")).split(",")))


output = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i]+numbers[j]+numbers[k]==0:
                triplet = tuple(sorted([numbers[i], numbers[j], numbers[k]]))
                output.add(triplet)
                

print([list(t) for t in output])