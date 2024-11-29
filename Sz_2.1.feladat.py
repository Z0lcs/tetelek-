szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
a_word=0

for word in szavak:
    for letter in word:
        if letter=='a' or letter=='A':
            a_word+=1
        else:
            break
print(a_word)