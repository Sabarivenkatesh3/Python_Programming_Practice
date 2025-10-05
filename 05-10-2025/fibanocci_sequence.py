num = int(input("enter the number: "))

fibanocci = [0,1]

while len(fibanocci) < num:
    fibanocci.append(fibanocci[-1] + fibanocci[-2])
print(fibanocci)