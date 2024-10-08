"""
Steen, papier en schaar
    - Een gebruiker uitnodigt het spel steen, papier en schaar te spelen
    - De gebruiker uit minstens drie opties laat kiezen
        - dit hoeft niet steen, papier of schaar te zijn, je mag andere wapens kiezen!
        - maar jouw programma moet wel steeds anders reageren op basis van de drie mogelijke opties die de gebruiker kan invoeren (althans, minimaal drie opties)
    - Het spel eerlijk speelt
        - maar je mag het spel ook zo maken dat de speler altijd wint (of verliest)
    - De keuze van de speler afdrukt (print)
        - je mag aannemen dat de gebruiker de keuze foutloos typt, dus altijd één van de mogelijke opties
    - Afdrukt welke keuze het zelf heeft gemaakt uit de mogelijke opties (eerlijk of niet)
    - Afdrukt wie het spel heeft gewonnen (of een gelijkspel, of een andere uitkomst)
"""

import random

def rps():

    user = input('Kies een wapen (steen, papier of schaar):')
    comp = random.choice(['steen', 'papier', 'schaar'])

    print("De gebruiker koos:", user)
    print("De computer koos:", comp)

    while True:        
        if user == comp:
            print('Het is gelijkspel')
            break
        if user == 'steen' and comp == 'papier':
            print('Je verliest, helaas!')
            break
        elif comp == 'schaar':
            print('Je hebt gewonnen!')
            break
        if user == 'papier' and comp == 'schaar':
            print('Je verliest, helaas!')
            break
        elif comp == 'steen':
            print('Je hebt gewonnen!')
            break
        if user == 'schaar' and comp == 'steen':
            print('Je verliest, helaas!')
            break
        elif comp == 'papier':
            print('Je hebt gewonnen!')
            break
        else:
            print('Onjuiste keuze, probeer het nog eens.')

# Start het spel
rps()