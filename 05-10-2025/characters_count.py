words = input("Enter a string: ")

character_count = {}  # empty dictionary

for i in words:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1

print(character_count)
