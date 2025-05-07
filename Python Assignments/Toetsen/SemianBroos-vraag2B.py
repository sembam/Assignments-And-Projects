def Naam(voornaam, achternaam):
    '''
    Laat de ingevoerde voor en achternaam zien.
    '''

    print('geef uw voornaam')
    voornaam = input('? ')
    print('geef uw achternaam')
    achternaam = input('? ')

    print(f"Hallo, {voornaam + " " + achternaam}")

Naam(voornaam='', achternaam='')
