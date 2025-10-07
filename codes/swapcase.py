

def swap(word):
    new_word = ""
    for i in word:
        if i.upper() == i:
            new_word += i.lower()
        else:
            new_word += i.upper()
    return new_word

word = input("Enter word to swap: ")

swaped_word = swap(word)
print("The swapped word is: ",swaped_word)