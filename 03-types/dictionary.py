'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

my_games = {
    'game1': {
        'name': 'Dark Souls III',
        'release': 2016,
        'multiplatform': True,
        # Recenze pochází z těchto stránek(v tomto pořadí): PCGamer, IGN, Metacritic
        'reviews': (94, 95, 89),
        'designers': {'Junya Ishizaki', 'Yuya Kimijima', 'Shigeto Hirai', 'Hiroshi Yoshida'},
        'writer': [47, {'name': 'Hidetaka', 'surname': 'Miyazaki', 'nationality': 'Japanese'}]
    },
    'game2': {
        'name': 'Detroit: Become Human',
        'release': 2018,
        'multiplatform': True,
        'reviews': (61, 80, 78),
        'designers': {'Simon Wasselin'},
        'writer': [52, {'name': 'David', 'surname': 'Cage', 'nationality': 'French'}]
    },
    'game3': {
        'name': 'The Witcher 3: Wild Hunt',
        'release': 2015,
        'multiplatform': True,
        'reviews': (92, 93, 93),
        'designers': {'Damien Monnier', 'Michał Dobrowolski'},
        'writer': [45, {'name': 'Marcin', 'surname': 'Blacha', 'nationality': 'Polish'}]
    }
}
print(my_games)
del my_games['game3']
print('---------------------------------------------')
print(my_games)
print('---------------------------------------------')
slovnikadd = {'game4': {
        'name': 'World Of Warcraft',
        'release': 2004,
        'multiplatform': False,
        'reviews': (80, 80, 83),
        'designers': {'Jeff Kaplan', 'Rob Pardo', 'Tom Chilton'},
        'writer': [57, {'name': 'Christie', 'surname': 'Golden', 'nationality': 'American'}]
    }}
my_games.update(slovnikadd)
print(my_games)
print('---------------------------------------------')
import pandas as pd

def tabulka(slovnik = {}):
    print('Slovník my_games')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    upraveno = pd.DataFrame(slovnik).T
    print(upraveno)

tabulka(my_games)