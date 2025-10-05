word1 = input()
word2 = input()

if sorted(word1)==sorted(word2):
    print("anagram")
else:
    print("not anagram")