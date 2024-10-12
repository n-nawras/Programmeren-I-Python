
gegeven_getallen = 0
opgeteld_getallen = 0

while True:
    
    inp = int(input("Geef positief getal: "))
    
    if inp < 0: #Check if the input more then 0.
        break
    
    opgeteld_getallen += inp
    gegeven_getallen += 1 
    

print(f"Getallen gegeven: {gegeven_getallen}")
print(f"Getallen opgeteld: {opgeteld_getallen}")