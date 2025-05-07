import math

def Formule(a, b, c, xtop, ytop, dis, parabool, root1, root2):
    
    print ('Gegeven de volgende tweede graads functie:')
    print ('y = ax^2 + bx + c')
    print('')
    a = int(input('Geef a ? '))
    b = int(input('Geef b ? '))
    c = int(input('Geef c ? '))
    print("")

    xtop = -b / 2 * a
    ytop = (a * xtop) ** 2 + b * xtop + c

    dis = b ** 2 - 4 * a * c

    if dis > 0:
        nulpunt = 2
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
    elif dis == 0:
        nulpunt = 1
        root1 = -b / (2 * a)
        
    elif dis < 0:
        nulpunt = 0



    print(f'de tweede graads functie is: y = {a}x^2 + {b}x + {c}')

    parabool = ''
    if a > 0:
        parabool = 'dalparabool'
    elif a < 0:
        parabool = 'bergparabool'
    elif a == 0:
        print('a kan geen 0 zijn')
        


    print(f'de functie is een {parabool} op x,y positie ({xtop}), ({ytop})')

    print(f'de tweedegraads functie heeft {nulpunt} nulpunten')

    print(f'De x-waarden van de nulpunten zijn: ({root1})({root2})')
Formule(a=0, b=0, c=0, xtop=0, ytop=0, dis=0, parabool='', root1=0, root2=0)