# Opgave 1
Voor deze opdracht is het jouw taak om een verzameling regels te ontwerpen om Picobot een lege vierkante ruimte volledig te laten verkennen.
Vergeet niet dat jouw oplossing moet werken voor elke mogelijke startpositie van Picobot!

    Antwoord:
        0 x*** -> N 0
        0 N*** -> X 1

        1 *x** -> E 1
        1 *E** -> W 2
        2 **x* -> W 2
        2 **W* -> S 1


# Opgave 2
Heb je Picobot de lege kamer kunnen laten verkennen? Dan is het nu tijd voor andere omgevingen, waaronder een doolhof!
   
    Antwoord:
        0 **x* -> W 3
        0 **W* -> x 1

        1 ***x -> S 0
        1 ***S -> x 2

        2 *x** -> E 1
        2 *E** -> x 3

        3 x*** -> N 2
        3 N*** -> x 0



# Opgave 3
Ontwerp een verzameling regels om Picobot een ruimte in de vorm van een ruit te laten verkennen (er zijn geen beperkingen aan het aantal regels).

    Antwoord:
        0 ***x -> s 0 
        0 *exs -> w 0 
        0 *xws -> e 0
        0 xews -> n 7 

        1 *x** -> e 1 
        1 xe** -> n 3 
        1 NEx* -> w 5 

        2 **x* -> w 2 
        2 x*w* -> n 4
        2 NxW* -> e 6 

        3 *x** -> e 2
        4 **x* -> w 1
        5 x*** -> n 2
        6 x*** -> n 1 
        7 **x* -> w 8 
        8 *x** -> e 1 

# Opgave 4
Ontwerp een verzameling regels om Picobot een ruimte in de vorm van een grot te laten verkennen (er zijn geen beperkingen aan het aantal regels).

    Antwoord:
        0 x*** -> N 0
        0 N*** -> X 1

        1 *x** -> E 1
        1 *E** -> W 2
        2 **x* 
