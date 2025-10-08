n = int(input())

for row in range(1, n+1):
    for col in range(1,row+1):
        print("*", end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(1,row+1):
        print(col, end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(1,row+1):
        print(row, end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(n, n-row, -1):
        print(col, end=" ")
    print()

print()

for row in range(1, n+1):
    num = n - row + 1
    for col in range(1, row+1):
        print(num, end=" ")
    print()
