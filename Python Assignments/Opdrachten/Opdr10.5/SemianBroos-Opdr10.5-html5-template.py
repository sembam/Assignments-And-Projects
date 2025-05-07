def template(key, taal, karakterset, viewport, auteur, titel, omschrijving, inhoud):
    print("\nWelkom bij html5 template !")
    print("druk op 'q' of 'Q' om het programma af te sluiten")

    def get_input(prompt):
        value = input(prompt)
        if value.lower() == 'q':
            print("Programma wordt afgesloten.")
            exit()
        return value

    print("\nwat is de taal van de pagina?")
    taal = get_input("Kies uit een van de volgende talen: nl, eng, de, be ? ")

    print("\nwat is de karakterset van de pagina ?")
    print("druk op enter voor de default waarde")
    karakterset = get_input("? ")


    print("\nwat is de viewportwaarde van de pagina ?")
    print("druk op enter voor de default waarde")
    viewport = get_input("")

    if viewport == '':
        viewport = 'width-device-width, initiaal-scale-1'
    else:
        viewport = viewport

    auteur = get_input("\nwie is de auteur van de pagina ? ")

    titel = get_input("\nwat is de titel van de pagina ? ")

    omschrijving = get_input("\nwat is de omschrijving van de pagina ? ")
    



    print("\ngeef hier de inhoud van de pagina ?")
    print("druk op enter voor de default waarde")
    inhoud = get_input("? ")

    if inhoud == '':
        inhoud = (f'dit is de homepagina van <{auteur} >')
    else:
        inhoud

    print(f"""
    ##################################################################
    Html pagina

         <!DOCTYPE html>
         <html lang='{taal}'>
            <head>
                <title>{titel}</title>
                <meta charset='{karakterset}'>
                <meta viewport="{viewport}">
                <meta name="description" content="{omschrijving}">
                <meta name="author" content="{auteur}">
            </head>
            <body>

                <h3>Welkom!</h3>
                <p>{inhoud}</p>

            </body>
        </html>
    ##################################################################


    
    
    
    
    
    """)
    


template(key='', taal='', karakterset='', viewport='', auteur='', titel='', omschrijving='', inhoud='')

