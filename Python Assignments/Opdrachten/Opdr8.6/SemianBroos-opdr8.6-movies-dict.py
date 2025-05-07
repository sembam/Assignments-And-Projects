movies = [
    {
        "titel": "The Godfather",
        "jaar": 1972,
        "cijfer": 9.2,
        "regisseur": "Francis Ford Coppola"
    },
    {
        "titel": "The Shawshank Redemption",
        "jaar": 1994,
        "cijfer": 9.3,
        "regisseur": "Frank Darabont"
    },
    {
        "titel": "Schindler's List",
        "jaar": 1993,
        "cijfer": 8.9,
        "regisseur": "Steven Spielberg"
    },
    {
        "titel": "Raging Bull",
        "jaar": 1980,
        "cijfer": 8.2,
        "regisseur": "Martin Scorsese"
    },
    {
        "titel": "Casablanca",
        "jaar": 1942,
        "cijfer": 8.5,
        "regisseur": "Michael Curtiz"
    }
    
]

print ("a) alle film titels")
print("--------------------------")
for x in movies:
    print(x['titel'])

print()
print ("b) alle titels voor 1990")
print ("--------------------------")
for titels in movies:
    if titels['jaar'] < 1990:
        print (titels['titel'])

print()
print("c) alle films van Steven Spielberg")
for regisseur in movies:
    if regisseur['regisseur'] == "Steven Spielberg":
        print(regisseur)