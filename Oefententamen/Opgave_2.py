if windspeed >= 252:
    print("Categorie 5")
elif 209 <= windspeed <= 251:
    print("Categorie 4")
elif 178 <= windspeed <= 208:
    print("Categorie 3")
elif 154 <= windspeed <= 177:
    print("Categorie 2")
elif 119 <= windspeed <= 153:
    print("Categorie 1")
elif 63 <= windspeed <= 118:
    print("Tropical Storm (TS)")
elif windspeed <= 62:
    print("Tropical Depression (TD)")