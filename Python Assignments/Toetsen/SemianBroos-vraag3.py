import random

def mk_array(cnt, rnd_min, rnd_max):
    '''
    Maakt een lijst van nummers tussen de 1 en 1000 met een minimum en maximum.
    '''
    cnt= random.randint(1, 20)
    rnd_min = 100
    rnd_max = 1000
    begin = 0

    while begin < cnt:
        print(f"{begin}: {random.randint(rnd_min, rnd_max)}")
        begin += 1

        return rnd_max, rnd_min, cnt
    
mk_array(cnt=0, rnd_min=0, rnd_max=0)
