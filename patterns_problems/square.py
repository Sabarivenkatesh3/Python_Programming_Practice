n = int(input())

for row in range(1, n+1):
    for col in range(1,n+1):
        print("*", end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(1,n+1):
        print(row, end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(1,n+1):
        print(col, end= " ")
    print()

print()

for row in range(1, n+1):
    for col in range(n,0,-1):
        print(col, end= " ")
    print()

print()

for row in range(n,0,-1):
    for col in range(1,n+1):
        print(row, end= " ")
    print()


    