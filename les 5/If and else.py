leeftijd = eval(input("Wat is uw leeftijd: "))
paspoort = input("Heeft u een paspoort: ")

if leeftijd > 17 and paspoort == "ja":
    print("Gefeliciteerd! U mag stemmen.")
else:
    print("Jammer genoeg mag je nog niet stemmen.")
