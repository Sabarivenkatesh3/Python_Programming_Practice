def sum(*args):
    total = 0
    for n in args:
        total += n
    return total


print(sum(50,10,150))