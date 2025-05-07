print('''
############################################################
Welkom bij rekenen !
Voer twee hele getallen in.
''')


#Opgeving van het getal en het uitprinten
Getal1 = input('Geef een eerste getal ? ')
Getal2 = input('Geef een tweede getal ? ')


print('')
print('Getal1 = ' + Getal1)
print('Getal2 = ' + Getal2)
print('')

#variabelen voor de berekeningen
som = int(Getal1) + int(Getal2)
verschil = int(Getal1) - int(Getal2)
product = int(Getal1) * int(Getal2)
deling = int(Getal1) / int(Getal2)

#De output voor de antwoorden
print('De som van ' + Getal1 + ' en ' + Getal2 + ' is ' + str(som))
print('Het verschil van ' + Getal1 + ' en ' + Getal2 + ' is ' + str(verschil))
print('Het product van ' + Getal1 + ' en ' + Getal2 + ' is ' + str(product))
print('De deling van ' + Getal1 + ' en ' + Getal2 + ' is ' + str(deling))





print('''
############################################################

Tot ziens!
''')
