
print ("Bereken de oppervlakte en de omtrek van een cirkel\n")

antwoord = float(input("Geef de lengte van de straal van een cirkel (cm)\n"))


oppervlakte = round((antwoord * antwoord * 3.141592653589793), 1)
omtrek = round((2 * antwoord * 3.141592653589793), 1)


print (f"De straal van de cirkel is {antwoord} Cm")
print (f"De oppervlakte van de cirkel is {oppervlakte} Cm2")
print (f"De omtrek van de cirkel is {omtrek} Cm")
