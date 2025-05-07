import random

def Naam(voornaam, achternaam):
    '''
    Laat de ingevoerde voor en achternaam zien.
    '''

    getal = random.randint(1, 5)

    if getal == 1:
        groet = 'Hoi'
    elif getal == 2:
        groet = 'Hallo'
    elif getal == 3:
        groet = 'goede avond'
    elif getal == 4:
        groet = 'goede morgen'
    elif getal == 5:
        groet = 'Hoe gaat het?'


    print('geef uw voornaam')
    voornaam = input('? ')
    print('geef uw achternaam')
    achternaam = input('? ')

    print(f"{groet} {voornaam + " " + achternaam}")

Naam(voornaam='', achternaam='')
