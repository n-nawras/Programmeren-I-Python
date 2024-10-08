# Functies schrijven
Leerdoel: Schrijven van simpele functies

### Opdracht 1
Schrijf de functie tpl(x) die een getal als argument accepteert en drie keer de waarde van dat argument teruggeeft.

```
In : tpl(4)
Out: 12

In: tpl("hoi")
Out: "hoihoihoi"
```

_Code:_

```
def main():
    """
    The geving elmment will be * 3 for example if the x = 3 the the output is 12. 
    It will also work with string. 
    """
    x = tpl("hoi")
    print(x)

def tpl(x):
    return x * 3

main()
```

### Opdracht 2
a. Schrijf de functie min_two(a, b) die twee getallen als argument accepteert en de kleinste waarde teruggeeft.

b. Schrijf de functie min_three(a, b, c) die drie getallen als argument accepteert en de kleinste waarde teruggeeft.


_Code:_

```
def main():
    """
    Geeft twee getallen als argument en de kleinste waarde teruggeeft.
    """
    
    getallen = minTwo(2, 3)
    print(getallen)

def minTwo(eersteG, tweedeG):
    if eersteG < tweedeG:
        return eersteG
    else:
        return tweedeG
main()
```

### Opdracht 3
Schrijf de functie absolute(x,y) die twee getallen accepteert en de afstand berekent tussen de twee getallen.

```
In : absolute(3, 10)
Out: 7

In: absolute(-3, 10)
Out: 13
```

_Code:_

```
def main():
    """
    de functie accepteert twee getallen en de afstand berekent tussen de twee getallen.
    """

    x = absolute(-3, 10)
    print(x)

def absolute(getal1, getal2):

    x = list(range(getal1, getal2))
    aantall = len(x)
   
    return(aantall)

main()
```

# Syntax van recursie
Leerdoel: Begrijpen wat er gebeurt als een functie zichzelf aanroept

### Opdracht 1

```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function(10)


def function(x):
    print(x)
    if x == 0:
        return
    function(x-1)

main()
```

_a. Wat doet de functie function?_ print de waarde van x en roept zichzelf recursief aan totdat x gelijk is aan 0.

_b. Wat is de output van dit programma?_ De output van main() met function(10): 10 tot 1, elke waarde op een nieuwe regel.

### Opdracht 2

```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function(10, 2)

def function(x, y):
    print(x)
    if x == 0:
        return
    function(x-y, y)

main()
```

_a. Wat doet de functie function?_ De functie function: print de waarde van x en roept zichzelf recursief aan met een vermindering van x met y totdat x gelijk is aan 0.

_b. Wat is de output van dit programma?_ De output van main() met function(10, 2): 10, 8, 6, 4, 2, 0, elk op een nieuwe regel.

_c. Wat is de output als function(10, 2) wordt vervangen met function(5,0)?_ Bij aanroep van function(5, 0): veroorzaakt een RecursionError door een oneindige recursieve aanroep.


### Opdracht 3

```
def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen.
    """
    x = function(10, 6)


def function(x, y):
    print(x)
    if x >= 20:
        return
    function(x+y, y)

main()
```

_a. Wat doet de functie function?_ De functie function: print de waarde van x en roept zichzelf recursief aan met x + y totdat x groter dan of gelijk aan 20 is.

_b. Wat is de output van dit programma?_ De output van het programma: 10, 16, 22, elk op een nieuwe regel.
