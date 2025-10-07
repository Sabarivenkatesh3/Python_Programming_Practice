word = input("enter a word: ")

reverse_word = []

for i in word:
    print(i)

reverse_word = word[::-1]

print("reversed word: ", reverse_word)

for j in reverse_word:
    print(j)

### to use another method
"""import sys

word = " ".join(sys.argv[1:])


reverse_word = []

for i in word:
    print(i)

reverse_word = word[::-1]

print("reversed word: ", reverse_word)

for j in reverse_word:
    print(j)
"""