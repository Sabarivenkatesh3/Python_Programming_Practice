numbers = list(map(int, input("enter the numbers:").split()))
print(numbers)

checked = set()


for i in numbers:
    if i not in checked:
        count = 0
        for j in numbers:
            if j == i:
                count += 1
                
        print(f"the number {i} occurs for {count} times")
        checked.add(i)
