def armstrong_num(num):
    count = 0
    arms_num = 0

    for i in num:
        count+=1

    for i in num:
        integer = int(i)
        am= integer**count
        arms_num += am

    if int(num)==arms_num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
    
num = input("Enter any number: ")
armstrong_num(num)






    

    
