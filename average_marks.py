num= int(input("Enter the no.of students: "))

details = {}

for i in range(0,num):
    if i>=0 and i<=num:
        student_marks = input().split()
        name = student_marks[0]
        marks = list(map(float, student_marks[1:]))
        details[name] = marks  

query = input("enter the name of the student for average: ")

avg = sum(details[query]) / len(details[query])
print(f"{avg:.2f}")
