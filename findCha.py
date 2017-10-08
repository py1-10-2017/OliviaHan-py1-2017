# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = []

for i in range (0,len(word_list)):
    for j in range (0,len(word_list[i])):
        if word_list[i].find(char) != -1:
            new_list = new_list + [word_list[i]]
            break
print new_list
