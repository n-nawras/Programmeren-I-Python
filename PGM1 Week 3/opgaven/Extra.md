# Opdracht 1
Schrijf de functie trap(x) die een getal accepteert en een omgekeerde # trap tekent (print). Maak gebruik van recursie en niet van lussen.

```
In : trap(3)
Out:
###
##
#

In: trap(5)
Out:
#####
####
###
##
#
```
##### Tip 
        Bedenk dat je strings kan vermenigvuldigen!
        3 * "#" == "###"

_Code:_
```
def trap(x):

    if x == 0:
        return
    
    print(x * "#")
    trap(x-1)
    
trap(3)
print()
trap(5)
```
# Opdracht 2
a. Schrijf de functie lines(x, space) die twee #-lijnen tekent van x regels hoog en space geeft aan hoeveel spaties tussen de lijnen liggen.

```
In : lines(3, 3)
Out:
#   #
#   #
#   #

In: lines(2, 5)
Out:
#     #
#     #
```

_Code:_
```
def lines (num1, num2):
    
    space = " " * num2
    tek = "#" 
    
    for i in range(num1):
        print(tek + space + tek)
    
lines(3, 3)
print()
lines(2, 5)

```

b. Schrijf een functie print_square(x) die een getal accepteert en een # vierkant van grootte x print. Maak gebruik van de functie lines.
```
In : print_square(3)
Out:
###
# #
###

In: print_square(5)
Out:
#####
#   #
#   #
#   #
#####
```

_Code:_