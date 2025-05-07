def BMR():

    try:
        leeftijd = float(input('Wat is uw leeftijd in jaren? '))
        gewicht = float(input('Wat is uw gewicht in kg? '))
        lengte = float(input('Wat is uw lengte in cm? '))
        geslacht = input('Wat is uw geslacht (m/v)? ').lower()
        factor = float(input('Hoeveel minuten wandelt u per dag? '))
    except ValueError:
        print("Ongeldige invoer. Zorg ervoor dat u numerieke waarden invoert waar gevraagd.")
        return

    
    if geslacht == 'm':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * lengte) - (5.677 * leeftijd)
    elif geslacht == 'v':
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * lengte) - (4.33 * leeftijd)
    else:
        print("Ongeldig geslacht. Voer 'm' of 'v' in.")
        return

    
    wandel_calorieen = (3 * 3.5 * gewicht / 200) * (factor / 60)

    
    totale_verbranding = bmr + wandel_calorieen

    print(f'De totale verbranding per dag is {totale_verbranding:.2f} calorieën.')


BMR()
BMR()