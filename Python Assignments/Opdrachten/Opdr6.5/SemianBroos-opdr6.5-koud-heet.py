print ('geef de temperatuur in °C \n')
temp = float(input('? '))

if temp < 0:
    print ('het is koud')
elif temp < 10 and temp > 0:
    print ('het is fris')
elif temp < 17 and temp > 11:
    print ('het is koel')
elif temp < 24 and temp > 18:
    print ('het is lekker weer')
elif temp < 31 and temp > 25:
    print ('het is warm')
elif temp < 40 and temp > 32:
    print ('het is erg warm')
elif temp > 40:
    print ('het is heet')