def som_gem(lijst, som_getal, gem_getal):
    som_getal = 0
    gem_getal = 0
    aantal = len(lijst)
    for getal in lijst:
        som_getal += getal
    for getal in lijst:
        gem_getal += getal / aantal
    
    
    print(f'lijst: {lijst}')
    print(f'som: {som_getal}')
    print(f'gem: {gem_getal}')
    print('')
som_gem(lijst=[1, 2, 3], som_getal=0, gem_getal=0)
som_gem(lijst=[7, 66, 94, 73, 12, 9, 33, 21], som_getal=0, gem_getal=0)
som_gem(lijst=[3, -79, 34, 47, 19, 8,], som_getal=0, gem_getal=0)