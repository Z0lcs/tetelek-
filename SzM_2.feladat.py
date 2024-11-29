words=[]

while True:
    word=input('Adj meg egy szót! ')
    if word=='':
        break
    else:
        words.append(word)
        short_word=word
        long_word=word

for word in words:
    if len(word)<len(short_word):
        short_word=word

for word in words:
    if len(word)>len(long_word):
        long_word=word

print(f'Beírt szavak: {words}, legrövidebb szó: {short_word}, leghosszabb szó: {long_word}')
