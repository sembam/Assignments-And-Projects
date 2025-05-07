import random

#ik wil meer met comments gaan werken dus dat doe ik vortaan

#maakt een variabel voor een random getal
rnd_getal = random.randint(1, 10)

#input
print ('--- Gok spelletje ---')
print ('geef een getal \n')
getal = int(input('? '))


if getal < rnd_getal:
    print (f'jammer, getal {getal} is te laag. \n het juiste getal was {rnd_getal}')
elif getal > rnd_getal:
    print (f'jammer, getal {getal} is te laag. \n het juiste getal was {rnd_getal}')
elif getal == rnd_getal:
    print(f'gefeliciteerd! getal {getal} is goed!')

