n = int(input())


for row in range(1, n + 1):
    for i in range(1, n - row + 1):
        print(" ", end=" ")
    for col in range(1, row * 2):
        print("*", end=" ")
    print()

print()


for row in range(1, n+1):
    for i in range(1, n - row + 1):
        print(" ", end=" ")
    for col in range(1, row * 2):
        print(col, end=" ")
    print()

print()


for row in range(1, n+1):
    for i in range(1, n - row + 1):
        print(" ", end=" ")
    for col in range(1, row * 2):
        print(n - row + 1, end=" ")
    print()

print()

for row in range(1, n+1):
    for i in range(1, n - row + 1):
        print(" ", end=" ")
    for col in range(1, row * 2):
        print(n - col + 1, end=" ")
    print()
