EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 300000000 #? rychlost světla ve vakuu (v m/s)
SPEED_OF_LIGHT_KMH = 1080000000 #? rychlost světla ve vakuu (v km/h)
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

DIST_MERCURY = 91700000
DIST_VENUS = 41400000
DIST_MARS = 78300000
DIST_JUPITER = 628700000
DIST_SATURN = 1279600000
DIST_URANUS = 2725400000
DIST_NEPTUNE = 4354400000


class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def gravitacnisila():
    '''
    Tato jednoduchá funkce zjišťuje gravitační sílu, kterou bude těleso přitahováno k zemi (případně k měsíci).
    '''
    print('Výpočet gravitační síly tělesa\n')
    print('----------------------------------------------\n')
    m = input('Zadejte hmotnost tělesa, jehož gravitační sílu chcete zjistit(ve formátu 1.11): ')
    v = float(EARTH_GRAVITY)*float(m)
    v2 = float(MOON_GRAVITY)*float(m)
    print('\n----------------------------------------------')
    print(f'Gravitační síla tělesa se bude rovnat {v:10.2f}N')
    print('----------------------------------------------')
    print(' Zajímavost:')
    print(f'Stejné těleso by mělo na měsíci gravitační sílu rovnou pouhým {v2:10.2f}N\n')
    print('(N = Newton (jednotka síly))\n')

def cascesty():
    '''
    Tato funkce zjišťuje, jak dlouho by trvala cesta ke každé z planet, pokud bychom vynalezli způsob, jak)
    cestovat rychlostí světla.
    '''
    print('    Výpočet času cesty na různá místa ve Vesmíru (pokud bychom cestovali rychlostí světla)')
    print('-------------------------------------------------------------------------------------------------------')
    print('Co kdybychom skrze Vesmír uměli cestovat rychlostí světla? Zjistěte, jak dlouho by trvala Vaše cesta!')
    print('Chci vědět: ')
    print('   1 - Jak dlouho by trvala cesta k planetám Sluneční soustavy?')
    print('   2 - Chci zadat vlastní vzdálenost')
    choice = input('Zvolte možnost (1 nebo 2): ')
    if int(choice)==1:
        print('-------------------------------------------------------------------------------------------------------')
        print('Chtěl bych vědět, jak dlouho by trvala cesta k: ')
        print('   1 - Merkuru'
              '   2 - Venuši'
              '   3 - Marsu'
              '   4 - Jupiteru'
              '   5 - Saturnu'
              '   6 - Uranu'
              '   7 - Neptunu')
        choice = input('Vaše volba (od 1 do 7): ')
        while switch(int(choice)):
            if case (1):
                t = (DIST_MERCURY*1000)/SPEED_OF_LIGHT
                t2 = DIST_MERCURY/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (2):
                t = (DIST_VENUS*1000)/SPEED_OF_LIGHT
                t2 = DIST_VENUS/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (3):
                t = (DIST_MARS*1000)/SPEED_OF_LIGHT
                t2 = DIST_MARS/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (4):
                t = (DIST_JUPITER*1000)/SPEED_OF_LIGHT
                t2 = DIST_JUPITER/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (5):
                t = (DIST_SATURN*1000)/SPEED_OF_LIGHT
                t2 = DIST_SATURN/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (6):
                t = (DIST_URANUS*1000)/SPEED_OF_LIGHT
                t2 = DIST_URANUS/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            if case (7):
                t = (DIST_NEPTUNE*1000)/SPEED_OF_LIGHT
                t2 = DIST_NEPTUNE/SPEED_OF_LIGHT_KMH
                print(f'Cesta by trvala {t:.2f} sekund čili {t2:.2f} hodin.')
                break
            print('Nezadal jste číslo od 1 do 7.')
            break
    elif int(choice)==2:
        print('-------------------------------------------------------------------------------------------------------')
        s = input('Zadejte vzdálenost od Země (v kilometrech): ')
        t = float(s)/float(SPEED_OF_LIGHT_KMH)
        print(f'Vaše cesta by trvala {t:.2f} hodin.')
    else:
        print('Nezadal jste 1 nebo 2, program bude ukončen.')
        sys.exit()

def letadlo():
    '''
    Funkce převádí poměr rychlosti letadla a zvuku na jednotku mach (násobek rychlosti zvuku)
    '''
    print('    Rychlost letadla v machových číslech')
    print('--------------------------------------------------------')
    v = input('Zadejte rychlost letadla, u kterého chcete zjistit machovo číslo (v m/s): ')
    mach = float(v) / float(SPEED_OF_SOUND)
    if mach < 1 and mach > 0:
        print('Rychlost letadla bohužel není nadzvuková')
    elif mach >=1:
        print(f'Rychlost letadla bude {mach:.2f} Mach')
    else:
        print('Zadejte prosím normální číslo.')