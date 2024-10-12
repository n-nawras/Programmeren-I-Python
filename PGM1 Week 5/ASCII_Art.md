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
def print_rect(width, height, symbol):
    
    for _ in range(height):
        print((symbol + " ") * width)

print_rect(4, 6, "%")
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
def print_triangle(width, symbol, right_side_up):
    
    if right_side_up:
        for i in range(True, width + 1):
            print(symbol * i)
    else:
        for i in range(width, False, -1):
            print(symbol * i)
            
print_triangle(3, "@", True)
print()
print_triangle(3, "@", False)

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
def print_triangle(width, symbol, right_side_up):
    if right_side_up:
        for i in range(1, width + 1):
            print(symbol * i)
    else:
        for i in range(width, 0, -1):
            print(symbol * i)



def print_bumps(num, symbol1, symbol2):
    for i in range(1, num + 1):
        print_triangle(i, symbol1, True)
        print_triangle(i, symbol2, False) 

print_bumps(4, "%", "#")

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
def print_diamond(width, symbol):
    
    for i in range(1, width + 1):
        print(" " * (width - i), end="")
        print(i * (symbol + " "))
    
    for i in range(width -1, 0, -1):
        print(" " * (width - i), end="")
        print((symbol + " ") * i)
        
print_diamond(3, "&")

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
def print_striped_diamond(width, sym1, sym2):
    
    for i in range(1, width + 1):
        print(" " * (width - i), end="")
        
        for j in range(i):
            if j % 2 == 0:
                print(sym1, end=" ")
            else:
                print(sym2, end=" ")
        print()

    for i in range(width - 1, 0, -1):
        print(" " * (width - i), end="")
        for j in range(i - 1, -1, -1):
            if j % 2 == 0:
                print(sym1, end=" ")
            else:
                print(sym2, end=" ")
        print()
        
print_striped_diamond(7, ".", "%")
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
def print_crazy_striped_diamond(width, sym1, sym2, sym1_width, sym2_width):

    for i in range(1, width + 1):
    
        print(" " * (width - i), end="")
    
        j = 1 
        while j <= i:
            if j % 3 != 0:
                if j % i != 0:
                    print((" " + sym1) * sym1_width, end=" ") 
                    j += sym1_width 
                    
                else:
                    print((" " + sym1), end=" ")
                    j += 1
            else: 
                print((" " + sym2), end=" ")
                j += 1 
        print()
    
    
    for i in range(width -1, 0, -1):
    
        print(" " * (width - i), end="")
    
        j = 1 
        while j <= i:
            if j % 3 != 0:
                if j % i != 0:
                    print((" " + sym1) * sym1_width, end=" ") 
                    j += sym1_width 
                    
                else:
                    print((" " + sym1), end=" ")
                    j += 1
            else: 
                print((" " + sym2), end=" ")
                j += 1 
        print()
        
    
        
print_crazy_striped_diamond(7, ".", "%", 2, 1)
```