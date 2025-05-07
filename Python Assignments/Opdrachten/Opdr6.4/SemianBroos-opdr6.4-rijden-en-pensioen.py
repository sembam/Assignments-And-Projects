print ('Geef uw leeftijd \n')
leeftijd = int(input('? '))

print (f'uw leeftijd is {leeftijd} \n')

if leeftijd > 0 and leeftijd < 18:
    print('Je mag nog niet autorijden!')
elif leeftijd > 68:
    print ('U mag met pensioen!')
elif leeftijd > 18 and leeftijd < 86:
    print ('U mag autorijden maar nog niet met pensioen!')
elif leeftijd < 0 and leeftijd > 120:
    print ('Geef een geldige leeftijd op!')