def readFile(filename):
    try:
        with open(filename, encoding='utf-8')as file:
            data = file.read()
    except FileExistsError as error:
        return 'Soubor nebyl nalezen'
    except Exception as error:
        return 'Problém při otevírání souboru'
    finally:
        file.close()
    return data
print(readFile("python.txt"))