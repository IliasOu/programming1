lengte = int(input("Wat is jouw lengte in centimeters: "))
def lang_genoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de attractie"
    else:
        return "Je bent helaas niet lang genoeg voor de attractie"
print(lang_genoeg(lengte))