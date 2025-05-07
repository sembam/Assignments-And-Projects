import random




def quiz():
    aantalfout = 0
    aantalgoed = 0
    abc = ['a', 'b', 'c']
    vragen = ['vraag 1', 'vraag 2', 'vraag 3', 'vraag 4', 'vraag 5', 'vraag 6', 'vraag 7', 'vraag 8', 'vraag 9', 'vraag 10']
    vraagaantal = int(input('-- Welkom! -- \n Hoeveel vragen wilt u oefenen? (Max 10) \n ? '))

    if vraagaantal > 10:
        print('error (niet genoeg elementen in de lijst)')
    else:
        for element in vragen[:vraagaantal]:
            print('wat is het antwoord? \n a, b of c')
            som = random.choice(abc) # random antwoord
            antwoord = input('? ').strip().lower()
            if antwoord == som:
                aantalgoed += 1
            else:
                aantalfout += 1
        
               
    procent = aantalgoed / vraagaantal * 100
    print(f'aantal goed: {aantalgoed}')
    print(f'aantal fout: {aantalfout}')
    print(f'je hebt {procent}% goed!')
    
    def opnieuw():
        opnieuw = input('wil je nog een keer deze quiz doen? y/n \n ? ')
        if opnieuw == 'y':
            quiz()
        elif opnieuw == 'n':
            print('ok, doei')
            exit()
        else:
            print('voer een geldig antwoord in')
    opnieuw()


quiz()
