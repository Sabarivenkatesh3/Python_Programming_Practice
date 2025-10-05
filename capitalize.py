words = list(map(str,input("Enter the sentence: ").split()))
print(words)

capitalize = ""

for i in range(0,len(words)):
    words[i][0] = words[i][0].upper()
    
        

print(words)
