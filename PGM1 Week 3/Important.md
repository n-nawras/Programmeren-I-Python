# Functies
#### Structuur versus procedure
$$f(x) = 2x + 3$$

```
    def f(x):
        return 2 * x + 3
```

# Imports
Random is wat een module wordt genoemd, soms wordt hier ook het woord library of functiebibliotheek voor gebruikt. Met het importeren van een module krijg te toegang tot alle functies die in deze module staan.

#### Optie 1:

```
    import random

    random.choice(list(range(0, 10)))
    random.randint(0,9)
    random.uniform(0,9)
```
In deze optie wordt de hele module toegevoegd. Om de functies te gebruiken die in deze module staan, noteren we eerst uit welke module ze komen en dan volgt de functie naam. Zo ontstaan er geen problemen als er meerdere modules worden geïmporteerd en er functie namen overeenkomen.



#### Optie 2:

```
    from random import choice
    from random import randint
    from random import uniform

    choice(list(range(0, 10)))
    randint(0,9)
    uniform(0,9)
```
from random import choice importeert een hele specifieke functie uit de module en niet de gehele module. Scheelt in de grootte van het programma. Is vooral handig om te gebruiken als je maar een enkele functie uit de module wilt gebruiken.


#### Optie 3:

```
    from random import *

    choice(list(range(0, 10)))
    randint(0,9)
    uniform(0,9)
```
from random import * importeert alle functies uit de module. Het is belangrijk om te weten welke functies dit zijn om te voorkomen dat er twee dezelfde functies in het programma staan. Bijvoorbeeld van een andere module of in je eigen code.

# Handige modules

math
- cos()
- sin()
- tan()
- sqrt()
- pi

random
- choice()
- randint()
- uniform()

time
- time()
- ctime()
- sleep()


# Ingebouwde functies
#### range
range geeft een iterator met integers terug. Het maakt niet uit als je niet precies weet wat een iterator is, het belangrijkst is dat je ziet dat list de iterator omzet naar een lijst met integers:
```
    In [1]: list(range(0, 100))
    Out[1]: [0, 1, 2, ..., 99]
```
Let op dat range, zoals bij vrijwel alles in Python, tot het eindpunt telt (en niet tot en met)!


#### sum
sum telt een lijst van getallen op, en range maakt een lijst met integers (of eigenlijk een iterator met integers, maar daar kan sum ook mee overweg):
```
    In [2]: sum(range(3, 11))
    Out[2]: 52
```
Een omslachtige manier om 40 + 2 uit te rekenen:

```
    In [3]: sum([40, 2])
    Out[3]: 42
```