marks = int(input("Enter the marks obtained: "))

while marks<=100:
    if marks >= 90:
        print("A Grade")
    elif marks >= 75:
        print("B Grade")
    elif marks >= 50:
        print("C Grade")
    else:
        print("Fail")
    break
else:
    print("please enter valid marks!!")