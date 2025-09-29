numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("The numbers are:",numbers)

pos_count = 0
neg_count = 0
zeros_count = 0

for i in numbers:
    if i < 0:
        neg_count += 1
    elif i > 0:
        pos_count += 1
    else:
        zeros_count +=1

print( "+ve count: ", pos_count)
print( "-ve count: ", neg_count)
print( "0 count: ", zeros_count)
