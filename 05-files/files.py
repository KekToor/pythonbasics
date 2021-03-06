import json, csv

def textfile_write(path, data = '', encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding)as file:
            file.write(data)
    except FileExistsError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Problém při otevírání souboru: {error}')
        return False
    finally:
        file.close()
    return True

def textfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding)as file:
            data = file.read()
    except FileExistsError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Problém při otevírání souboru: {error}'
    finally:
        file.close()
    return data

def jsonfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding)as file:
            data = json.load(file)
    except FileExistsError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Problém při otevírání souboru: {error}'
    finally:
        file.close()
    return data


def jsonfile_write(path, data = {}, encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding)as file:
            json.dump(data, file)
    except FileExistsError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Problém při otevírání souboru: {error}')
        return False
    finally:
        file.close()
    return True

def csvfile_read(path, encoding='utf-8'):
    try:
        with open(path, encoding=encoding, newline='\n')as file:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            dict_list = []
            for row in reader:
                dict_list.append(row)
    except FileExistsError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Problém při otevírání souboru 1: {error}'
    finally:
        file.close()
    return dict_list

def csvfile_write(path, data = [], encoding='utf-8'):
    try:
        with open(path, mode='w', encoding=encoding, newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
            writer.writeheader()
            for row in data:
                writer.writerow(row)


    except FileExistsError as error:
        print(f'Soubor nebyl nalezen: {error}')
        return False
    except Exception as error:
        print(f'Problém při otevírání souboru 2: {error} {type(error)}')
        return False
    finally:
        file.close()
    return True



# txt = (textfile_read("python.txt"))
# print(textfile_write('./novy.txt',txt))
# jsondata = jsonfile_read('./kniha.json')
# print(jsonfile_write('./novy.json', jsondata))

data = (csvfile_read('./kniha.csv'))
print(csvfile_write('./novy.csv', data))