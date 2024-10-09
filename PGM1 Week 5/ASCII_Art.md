# Opgave 1
Schrijf een functie print_rect die drie argumenten width, height en symbol accepteert, en een rechthoek van width bij height met symbolen afdrukt op het scherm.

```
In [1]: print_rect(4, 6, "%")
Out:
% % % %
% % % %
% % % %
% % % %
% % % %
% % % %
```
_Code:_

```

```

# Opdracht 2
Schrijf een functie print_rect die drie argumenten width, height en symbol accepteert, en een rechthoek van width bij height met symbolen afdrSchrijf een functie print_triangle die drie argumenten width, symbol en right_side_up accepteert, en een driehoek van symbolen op het scherm afdrukt.

width is een getal die de breedte van de basis van de driehoek bepaalt en right_side_up is een boolean die bepaalt of de driehoek met de punt naar boven (True) of naar onder (False) moet worden afgedrukt.ukt op het scherm.

```
In [1]: print_triangle(3, "@", True)
Out:
@
@ @
@ @ @

In [2]: print_triangle(3, "@", False)
Out:
@ @ @
@ @
@
```
_Code:_

```

```


# Opdracht 3
Gebruik nu jouw functie print_triangle om een functie print_bumps(num, symbol1, symbol2) te schrijven die het gegeven aantal “heuvels” van twee symbolen afdrukt, waarbij elke heuvel groter is dan de volgende, zoals in het volgende voorbeeld:

```
In [1]: print_bumps(4, "%", "#")
Out:
%
#
%
% %
# #
#
%
% %
% % %
# # #
# #
#
%
% %
% % %
% % % %
# # # #
# # #
# #
#
```
_Code:_

```

```

# Opdracht 4
Voor deze en de volgende “ruit”-functies mag je string-vermenigvuldiging gebruiken, maar alleen voor strings van spaties, zoals " " * n en dergelijke. Elk zichtbaar karakter moet afzonderlijk afgedrukt worden, net zoals in de functies van de eerdere opgaven. Het is echter niet verplicht om de operator * te gebruiken voor strings van spaties.


Schrijf een functie print_diamond(width, symbol) die een ruit met symbol-en afdrukt waarvan de maximale breedte bepaald wordt door width.

```
In [1]: print_diamond(3, "&")
Out:
   &
  & &
 & & &
  & &
   &
```
_Code:_

```

```


# Opdracht 5
Schrijf nu een functie print_striped_diamond(width, sym1, sym2) die een “gestreepte ruit” van sym1 en sym2 afdrukt.

Bijvoorbeeld:
```
In [1]: print_striped_diamond(7, ".", "%")
Out:
      .
     . %
    . % .
   . % . %
  . % . % .
 . % . % . %
. % . % . % .
 % . % . % .
  . % . % .
   % . % .
    . % .
     % .
      .
```
_Code:_

```

```
# Opdracht 6
Schrijf tot slot een functie print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width) die een “gestreepte ruit” van sym1 en sym2 afdrukt waarbij de strepen verschillende breedtes kunnen hebben.

- sym1_width bepaalt de breedte van de streep gemaakt van symbool 1

- sym2_width bepaalt de breedte van de streep gemaakt van symbool 2.

```
In [1]: print_crazy_striped_diamond(7, ".", "%", 2, 1)
Out:
      .
     . .
    . . %
   . . % .
  . . % . .
 . . % . . %
. . % . . % .
 . % . . % .
  % . . % .
   . . % .
    . % .
     % .
      .
```
_Code:_

```

```