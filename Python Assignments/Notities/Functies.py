
# Een functie is een blok code die vaker uitgevoerd kan worden.

# Hier een aantal tips om effectief functies te gebruiken:


# 1. Breek de functie van de functie in meerdere delen
# zodat het niet allemaal in 1 functie zit.
# voorbeeld:

def get_user_input():
    # user input krijgen
    pass

def calculate_bmr(leeftijd, gewicht, lengte, geslacht):
    # BMR berekenen
    pass

# 2. Hierbij hoort ook niet alle input hardcoden, geef de input door met pass

# 3. Maak gewoon voor alle input een aparte functie

# 4. Maak functies goed. 
# Hierbij bedoel ik doe niet de input, berekening en uitkomst(print) allemaal in 1 functie

# 5. gebruik goede namen voor variabelen

# 6 gebruik comments en docstrings

# 7. als je herhaalde code ziet doe het in een apparte functie, bijvoorbeeld:

def calculate_bmr_for_gender(is_male, weight, height, age):
    if is_male:
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)

# 8. denk aan herbruikbaarheid, kan ik een functie hergebruiken?
# Of een deel code er van?