oldpassword = str(input("Voer uw oude wachtwoord in: "))
newpassword = str(input("Voer uw nieuwe wachtwoord in: "))
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        return "True"
    else:
        return "False"
print(new_password(oldpassword, newpassword))