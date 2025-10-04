def mutate_string(string, position, character):
    altered_string = list(string)
    altered_string[position] = character
    return ''.join(altered_string)  
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)