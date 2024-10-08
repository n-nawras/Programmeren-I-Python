# Opdracht 1
#### 1a
Een klusjesman, Handige Harry, rekent startkosten/voorrijkosten van €60 en een uurtarief van €40. Schrijf een programma dat de volgende stappen doet:

- Vraagt de gebruiker om input, dit omzet tot een integer en het resultaat opslaat in een variabele genaamd uren.

- Een berekening uitvoert om uit te rekenen hoeveel geld Harry krijgt en het resultaat opslaat in een variabele genaamd rekening.

- Print het resultaat.

_Code:_
```
uren = int(input("Hoeveel uren heeft Harry gewerkt? "))

startkosten = 60 
uurtarief = 40
rekening = startkosten + (uren * uurtarief)

print(f"De totale rekening voor Harry is: €{rekening}")

```

#### 1b
Harry heeft een aanbieding lopen: als de klant meer dan €400 moet betalen, dan krijgt de klant 10% korting. Pas het programma bij a zo aan dat ook de korting wordt meeberekend, als de klant daar recht op heeft.

_Code:_
```
uren = int(input("Hoeveel uren heeft Harry gewerkt? "))

startkosten = 60 
uurtarief = 40

rekening = startkosten + (uren * uurtarief)

if (rekening > 400):
    korting = rekening * 0.10  # 10% korting
    rekening -= korting
    print(f"De rekening was boven €400. Je krijgt 10% korting van €{korting}")

print(f"De totale rekening voor Harry is: €{rekening}")
```

# Opdracht 2
Tentamencijfers worden vaak berekend aan de hand van een formule:

    punten / max_punten * 9 + 1 = cijfer

Schrijf een programma dat de gebruiker 2 keer om input vraagt; namelijk hoeveel punten er zijn gehaald voor de toets en hoeveel punten er maximaal te behalen zijn. Vervolgens berekent het programma het cijfer en print dat uit.

_Code:_

```
gPunten = input("Hoeveel punten er zijn gehaald voor de toets: ")
maxPunten = input("Hoeveel punten er macimaal te behalen: ")

cijfer = int(gPunten) / int(maxPunten) * 9 + 1

print(f"Cijfer is: {cijfer}")
```

# Opdracht 3
#### 3a
Schrijf een programma dat de gebruiker 2 keer om input vraagt; namelijk wat de temperatuur is en of dat in Fahrenheit is of in Celsius. Als het in Fahrenheit is, rekent het programma uit wat dat in Celsius is en andersom. De formule om van Celsius naar Fahrenheit te komen is:

$$(\text{Celsius} \times \frac{9}{5}) + 32 = \text{Fahrenheit}$$

_Code:_
```
temperatuur = float(input("Wat de temperatuur is:"))
f_or_c = input("Is dat in Fahrenheit of in Celsius?")

f_to_c = (temperatuur - 32) * 5/9
c_to_f = (temperatuur * 9/5) + 32

if f_or_c == 'Fahrenheit':
    print(f"{temperatuur} graden Faherenheit is gelijke aan {f_to_c:.2f} graden Celsius")
elif f_or_c == 'Celsius':
    print(f"{temperatuur} graden Celsius is gelijke aan {c_to_f:.2f} graden Faherenheit")
else:
    print('Ongeldige invoer. Voer aub Fahrenheit of Celsius.')
```
#### 3b
Naast Fahrenheit en Celsius is er ook graden Kelvin. De formule voor de omzetting van graden Celsius naar Kelvin is als volgt:
        $$Celsius + 273.15 = Kelvin$$
Pas het programma bij a zodanig aan dat:

- Als de gebruiker aangeeft dat de temperatuur in Kelvin is, het programma de temperatuur in Celsius en in Fahrenheit uitprint.
- Als het Celsius is, dan print het programma Kelvin en Fahrenheit uit.
- Als het Fahrenheit is, dan print het programma Celsius en Kelvin uit.

_Voorbeeld output:_

        Temperatuur?: 20
        Schaal?: Celsius
        Fahrenheit = 68
        Kelvin = 293.15

        Temperatuur?: 20
        Schaal?: Fahrenheit
        Celsius = -6.67
        Kelvin = 266.48

_Code:_

```
temperatuur = float(input("Wat is de temperatuur?: "))
eenheid = input("Is dat in Fahrenheit, Celsius of Kelvin? ").strip().capitalize()

if eenheid == 'Fahrenheit':
    celsius = (temperatuur - 32) * 5 / 9
    kelvin = celsius + 273.15
    print(f"Temperatuur?: {temperatuur}")
    print(f"Schaal?: {eenheid}")
    print(f"Celsius = {celsius:.2f}")
    print(f"Kelvin = {kelvin:.2f}")

elif eenheid == 'Celsius':
    fahrenheit = (temperatuur * 9 / 5) + 32
    kelvin = temperatuur + 273.15
    print(f"Temperatuur?: {temperatuur}")
    print(f"Schaal?: {eenheid}")
    print(f"Fahrenheit = {fahrenheit:.2f}")
    print(f"Kelvin = {kelvin:.2f}")

elif eenheid == 'Kelvin':
    celsius = temperatuur - 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperatuur?: {temperatuur}")
    print(f"Schaal?: {eenheid}")
    print(f"Celsius = {celsius:.2f}")
    print(f"Fahrenheit = {fahrenheit:.2f}")

else:
    print('Ongeldige invoer. Voer alstublieft Fahrenheit, Celsius of Kelvin in.')

```

