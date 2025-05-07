print("getallen = '12, 3, 7, 25, 771, 45, 6, 98, 55, 546'")

getallen = [12, 3, 7, 25, 771, 45, 6, 98, 55, 546]

for getal in getallen:

    isEven = getallen % 2 == 0

    if isEven == True:
        print(f'Getal {getallen} is even')
    else:
        print(f'Getal {getallen} is oneven')