# Van decimaal naar binair en verder!
Dit probleem gaat over het omzetten van getallen naar en van grondtal 10 (decimaal, wat de meeste mensen gebruiken) en van en naar grondtal 2 (binair, waar vrijwel alle computers mee werken).

Aan het einde van de opdracht zal je dit uitbreiden naar ternair, oftewel grondtal 3, waar minder computers en mensen, maar veel meer buitenaardse wezens mee werken!

## Functie 1: is_odd(n)
Schrijf een Python functie is_odd(n) die als argument een integer n accepteert, en True teruggeeft als n oneven is en False als n even is. Zorg ervoor dat je deze (boolean) waarden teruggeeft, niet strings! De even- of onevenheid van een getal noemen we zijn pariteit.

Je moet de %-operator (de “modulo”-operator) gebruiken. Onthoud dat in Python n % d de rest na deling van n door d teruggeeft (als n >= 0). Hier zijn twee voorbeelden van het gebruik van is_odd:

```
In [1]: is_odd(42)
Out[1]: False

In [2]: is_odd(43)
Out[2]: True
```

Hier zijn een paar tests:

```
assert is_odd(42) == False
assert is_odd(43) == True
```

Als je liever kortere versies hebt van deze tests dan kan je de volgende gebruiken:

```
assert not is_odd(42)
assert is_odd(43)
```

_Code:_
```

```

## Functie 2: num_to_binary(n)
In dit onderdeel ga je getallen bit voor bit,van rechts naar links van decimaal naar binair omzetten, wat misschien “even” raar zal klinken…!

Kort samengevat, je gaat een functie num_to_binary(n) schrijven die als volgt werkt:
```
In [1]: num_to_binary(0)
Out[1]: ''

In [2]: num_to_binary(1)
Out[2]: '1'

In [3]: num_to_binary(4)
Out[3]: '100'

In [4]: num_to_binary(10)
Out[4]: '1010'

In [5]: num_to_binary(42)
Out[5]: '101010'

In [6]: num_to_binary(100)
Out[6]: '1100100'
```

_Code:_
```

```

## Functie 3: binary_to_num(s)

Nu ga je het meer uitdagende probleem aanpakken om van grondtal 2 naar grondtal 10 te gaan, opnieuw van rechts naar links. We stellen een waarde met grondtal 2 voor als een reeks van 0’en en 1’en (bits).

Kort samengevat, je gaat een functie binary_to_num(s) schrijven die als volgt werkt:
```
In [1]: binary_to_num("100")
Out[1]: 4

In [2]: binary_to_num("1011")
Out[1]: 11

In [3]: binary_to_num("00001011")
Out[1]: 11

In [4]: binary_to_num("")
Out[1]: 0

In [5]: binary_to_num("0")
Out[1]: 0

In [6]: binary_to_num("1100100")
Out[1]: 100

In [7]: binary_to_num("101010")
Out[1]: 42
```

_Code:_
```

```

## Functie 4: increment(s)

In het kort, schrijft increment(S), die een binaire string s met 0’en en 1’en accepteert en het volgende getal in grondtal 2 teruggeeft.

Merk op dat increment('11111111') in de voorbeelden hier beneden weer uitkomt op een string met alleen maar nullen. Dit kan een speciaal geval zijn (if).

Maak gebruik van de functies die je eerder hebt geschreven!

Hier zie je een aantal voorbeelden:
```
In [1]: increment("00000000")
Out[1]: '00000001'

In [2]: increment("00000001")
Out[2]: '00000010'

In [3]: increment("00000111")
Out[3]: '00001000'

In [4]: increment("11111111")
Out[4]: '00000000'
```

_Code:_
```

```

# Functie 5: count(s, n)
Gebruik de functie increment om de functie count(s, n) te schrijven, die een binaire string van 8 tekens accepteert als argument en vervolgens n keer doortelt vanaf s, terwijl hij wordt afgedrukt.

Hier zie je een aantal voorbeelden:
```
In [1]: count("00000000", 4)
00000000
00000001
00000010
00000011
00000100

In [2]: count("11111110", 5)
11111110
11111111
00000000
00000001
00000010
00000011
```

_Code:_
```

```

# Functie 7: ternary_to_num(s)
Scrijf de functie ternary_to_num(s), die een integer representatie teruggeeft van de waarde van het argument s (net als binary_to_num).

Hier zie je een aantal voorbeelden:
```
In [3]: ternary_to_num("1120")
Out[3]: 42

In [4]: ternary_to_num("12211010")
Out[4]: 4242
```

_Code:_
```

```