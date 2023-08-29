import random
import pickle

spillkort = []

for i in range(7, 15):
    spillkort.append(f'\u2665 {i}')
    spillkort.append(f'\u2663 {i}')
    spillkort.append(f'\u2666 {i}')
    spillkort.append(f'\u2660 {i}')


def stokk(kort):
    random.shuffle(kort)
    kort = [kort[x:x + 4] for x in range(0, len(kort), 4)] 
    return kort


def fjernkort(b1, b2):
    global bunker
    bokstaver = ("ABCDEFGH")
    konverter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    if b1 != b2:
        bunker[konverter[b1]].pop(0)
        bunker[konverter[b2]].pop(0)
    else:
        print("prøv igjen")

def tap(kort):
    kopi = []
    for item in kort:
        try:
            kopi.append(int(item[0][2:]))
        except:
            continue

    kopi_2 = set(kopi)
    if len(kopi) == len(kopi_2):
        return True

def lagre(kort):
    pickle.dump(kort, open("wish.p", "wb"))

def vinn(kort):
    if spillkort == 0:
        print("Du vant!")
    
def lastned():
    global bunker
    try:
        bunker = pickle.load(open("wish.p", "rb"))
        spill(bunker)
    except FileNotFoundError:
        print("Finner ingen lagret data")

def spill(kort):
    bokstaver = list("ABCDEFGH")
    while True:
        if vinn(kort):
            print("Du vant!")
            break
        elif tap(kort):
            print("Du tapte...")
            break
        else:
            for index, bunke in enumerate(kort):
                if len(bunke) > 0:
                    print(f'{bokstaver[index]}: {bunke[0]} {" "* (len(bunke[0])%2)}{"? "* len(bunke[1:])}')
                else:
                    print(f"{bokstaver[index]}:")

            print('\n"lagre" for å lagre file')
            print('"tilbake" for å gå tilbake til meny')
            bruker = input("Velg kort du vil fjerne (eks: AF):").upper()
            if bruker == "LAGRE": lagre(kort)
            elif bruker == "TILBAKE": meny()
            else:
                if len(bruker) == 2:
                    b1 = bruker[0]
                    b2 = bruker[1]
                    fjernkort(b1, b2)
                else: spill(kort)

bunker = stokk(spillkort)

def meny():
    global bunker
    import sys
    valg = """
---------------
1 - Nytt spill
2 - Hent lagret spill
---------------
"""
    print(valg)
    bruker_valg = input("Valg:")
    if bruker_valg == "1":
        bunker = stokk(spillkort)
        spill(bunker)
    elif bruker_valg == "2":
        lastned()
    else:
        print("Prøv igjen")

    meny()


meny() 
        










