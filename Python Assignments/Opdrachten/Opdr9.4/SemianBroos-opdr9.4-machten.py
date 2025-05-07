import random


def macht(grondtal, macht):
    '''
    doet tot de macht op een random getal tussen de 1 en de 10
    '''
    # gebruik random cijfer tussen de 1 en tien voor beide te genereren.
    grondtal = random.randint(1, 10)
    macht = random.randint(1, 10)
    resultaat = grondtal ** macht
    print (f'{grondtal} tot de macht {macht} is {resultaat}')
    


macht(grondtal=0, macht=0)
macht(grondtal=0, macht=0)