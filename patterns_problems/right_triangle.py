n = int(input())

for row in range(1, n+1):
    space= row
    for i in range(1,n-space+1):
        print(" ",  end= " ")
    for col in range(1,space+1):
        print("*", end= " ")
    print()

print()

for row in range(1, n+1):
    space= row
    for i in range(1,n-space+1):
        print(" ",  end= " ")
    for col in range(1,space+1):
        print(row, end= " ")
    print()

print()

for row in range(1, n+1):
    space= row
    for i in range(1,n-space+1):
        print(" ",  end= " ")
    for col in range(1,space+1):
        print(col, end= " ")
    print()

print()

for row in range(1, n+1):
    space= row
    for i in range(1,n-space+1):
        print(" ",  end= " ")
    for col in range(1,space+1):
        print(n-row+1, end= " ")
    print()

print()

for row in range(1, n+1):
    space= row
    for i in range(1,n-space+1):
        print(" ",  end= " ")
    for col in range(1,space+1):
        print(n-col+1, end= " ")
    print()
