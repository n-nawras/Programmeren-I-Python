def over_hundred(L):
    
    """
    Controleert of de som van de getallen in de lijst L groter is dan 100.
    Als de som van getallen gorter dan 100 returens True anders False.
    """
    
    result = 0
    for i in L:
        result += i 
        
        if result > 100:
            return True
            
    return False

L = [12,13,7] 
print(over_hundred(L))
