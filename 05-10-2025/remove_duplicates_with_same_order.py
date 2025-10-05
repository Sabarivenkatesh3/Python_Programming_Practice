numbers  = list(map(int,input("enter the numbers: ").split()))


without_duplicates = []
for i in numbers:
   
    if i in without_duplicates:
        continue
    else:
        without_duplicates.append(i)

print(without_duplicates)