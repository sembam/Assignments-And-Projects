def bereken_driehoek(hoogte, breedte):
    hoogte = float(input('geef een hoogte op:  ? '))
    breedte = float(input('geef een breedte op:  ? '))
    resultaat = breedte * (hoogte * 0.5)
    print(f'de oppervlakte van de driehoek is {resultaat}')
bereken_driehoek(hoogte=0, breedte=0)