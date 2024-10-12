# Toekenning van de opbrengst per gewas in kilogram
opbrengst_tomaten = 150  # kilogram
opbrengst_paprikas = 120  # kilogram
opbrengst_komkommers = 80  # kilogram

# Berekening van de totale opbrengst in kilogram
totale_opbrengst = opbrengst_tomaten + opbrengst_paprikas + opbrengst_komkommers

# Prijzen per kilogram voor elk gewas
prijs_tomaat_per_kg = 3.24  # euro per kilogram
prijs_paprika_per_kg = 2.87  # euro per kilogram
prijs_komkommer_per_kg = 1.48  # euro per kilogram

# Berekening van de totale omzet

totale_omzet = (opbrengst_tomaten * prijs_tomaat_per_kg) + \
                (opbrengst_paprikas * prijs_paprika_per_kg) + \
                (opbrengst_komkommers * prijs_komkommer_per_kg)

# Rond de totale omzet af op twee decimalen
totale_omzet = round(totale_omzet, 2)

# Resultaten afdrukken
print("Totale opbrengst in kilogram:", totale_opbrengst)
print("Totale omzet in euro:", totale_omzet)


