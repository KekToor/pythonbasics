def vyskytPismen (sentence):
    vyskyt = {}
    for letter in set(sentence):
        vyskyt[letter] = sentence.count(letter)
    return vyskyt
veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
vyskyty = vyskytPismen(veta)
setrizene = sorted(vyskyty.items(), key=lambda x:x[1], reverse = True)

def textfile_write(path, data = {}, encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding)as file:
            file.write('Četnost výskytu písmen\n')
            file.write('------------------------------\n')
            file.write('[\n')
            for key, value in data:
                file.write(f"('{key}' : {value})\n")
            file.write(']\n')
    except FileExistsError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Problém při otevírání souboru: {error}')
        return False
    finally:
        file.close()
    return True

textfile_write('./frekvence.txt', setrizene)