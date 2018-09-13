cijferICOR = 6
cijferPROG = 8
cijferCSN = 7
gemiddelde = (cijferCSN + cijferPROG + cijferICOR) / 3
beloning = (cijferCSN * 30) + (cijferPROG*30) + (cijferICOR*30)
overzicht = 'Mijn cijfers' + ' ' + '(gemiddeld een' + ' ' + str(gemiddelde) + ')' + 'leveren een beloning van ' + str(beloning) + ' op!'
print(overzicht)

