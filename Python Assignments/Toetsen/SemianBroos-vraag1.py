teken = ""

while teken == "+" or "-" or "*" or "/":
    
    print('programma berekenen')
    print('kies uit: +, -, *, /.')
    teken = input('? ')

    print('geef een (geheel) getal.')
    getal1 = int(input('? '))
    print('geef een (geheel) getal')
    getal2 = int(input('? '))

    if getal2 == "0" and teken == '/':
        print('Kan niet delen door 0')

    if teken == '+':
        antwoord = getal1 + getal2
        print(f'Het resultaat van {getal1} {teken} {getal2} is {antwoord}')
    elif teken == '-':
        antwoord = getal1 - getal2
        print(f'Het resultaat van {getal1} {teken} {getal2} is {antwoord}')
    elif teken == '*':
        antwoord = getal1 * getal2
        print(f'Het resultaat van {getal1} {teken} {getal2} is {antwoord}')
    elif teken == '/':
        antwoord = getal1 / getal2
        print(f'Het resultaat van {getal1} {teken} {getal2} is {antwoord}')
        
    

    print('typ een willekeurige toets in om door te gaan...')
    print('kies "s" om te stoppen...')
    stop = input("")

    if stop == 's' or 'S':
        break