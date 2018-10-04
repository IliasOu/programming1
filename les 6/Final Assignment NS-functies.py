def standaardprijs(afstandKM):
    prijs = float(0.80)  # prijs per kilometer
    if afstandKM <= 50:
        prijs *= afstandKM
        return "De treinrit kost {:.2f} euro." .format(prijs)
    else:
        return "Je kunt korting ontvangen!"
print(standaardprijs(49))

def ritprijs(leeftijd, weekendrit, afstandKM)
    for x in ritprijs:
