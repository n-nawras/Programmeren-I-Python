
# Syntax van functies
Leerdoel: het lezen van functies
## Opdracht 1
```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function(4) + function(6)
    print(x)


def function(x):
    l = list(range(x))
    return sum(l)

main()
```
a. Wat doet de functie function? 1- Creëert een lijst 2- Berekenen van de som
b. Wat is de ouput van dit programma? 21


## Opdracht 2
```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function("lol")
    y = function("xo")
    print(x + y)

def function(x):
    s = x[::-1] + x
    return s

main()
```
a. Wat doet de functie function? maakt een nieuwe string door de originele string om te keren en deze aan de originele string toe te voegen.

b. Wat is de ouput van dit programma? lolloloxxo


## Opdracht 3
```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    l = function1(5)
    x = function2(l)
    print(x)

def function1(x):
    l = list(range(x))
    return l[::-1]

def function2(l):
    x = sum(l)
    y = len(l)
    return x / y

main()
```
a. Wat doet de functie function1? genereert een lijst van 0 tot x-1 en retourneert deze in omgekeerde volgorde.

b. Wat doet de functie function2?  berekent en retourneert het gemiddelde van de getallen in de lijst.

c. Wat is de output van dit programma? 2.0