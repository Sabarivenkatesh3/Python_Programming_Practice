sentence = list(map(str, input().split()))
print(sentence)

max_word = ''

max_word_length = 0

for i in sentence:
    if len(i)>max_word_length:
        max_word = i
        max_word_length = len(i)

print(max_word,max_word_length)