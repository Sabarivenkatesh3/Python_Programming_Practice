word = input("enter the word: ")
print(word)

reverse_word = word[::-1]

if word == reverse_word:
    print("palindrome")
else:
    print("not palindrome")