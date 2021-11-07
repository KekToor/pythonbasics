def vyskytPismen (sentence):
    vyskyt = {}
    for letter in set(sentence):
        vyskyt[letter] = sentence.count(letter)
    return vyskyt
veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
vyskyty = vyskytPismen(veta)
setrizene = sorted(vyskyty.items(), key=lambda x:x[1], reverse = True)
print(setrizene)