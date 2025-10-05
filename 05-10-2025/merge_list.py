num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

merge = num1 + num2
merge.sort()

print(merge)