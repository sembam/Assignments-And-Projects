import random

rnd_getal = random.randint(1, 10)

getal = int(input("Raad een getal tussen de 1 en de 10 \n ? "))


while getal!= rnd_getal:

    random.radint(1, 10)

    if getal > rnd_getal: 
        print("Het getal is te hoog")
    elif getal < rnd_getal:
        print("Het getal is te laag")
    else:
        print("Voer een geldig getal in")
    
    getal = int(input("? "))
    
print("je hebt gewonnen!")