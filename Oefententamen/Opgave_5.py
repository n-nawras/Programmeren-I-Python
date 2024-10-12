def number_stairs(size):
    """
    De functie ontvanget integer size en een ladder uitprint van nummers. 
    """
    
    for i in range(1, size + 1):
        for j in range(0, i):
            print(j + 1, end="")
        print()
    
number_stairs(5)
print()
number_stairs(3)