def vraag_naam():
    print('wat is uw naam?')
    naam = input('? ')
    print(f'Hallo {naam} \n ')
    vraag_naam()
vraag_naam()