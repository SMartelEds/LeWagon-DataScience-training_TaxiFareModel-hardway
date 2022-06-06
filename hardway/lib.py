from time import sleep

def try_me():
    input("Veuillez indiquer l'âge de votre grand-mère: ")
    input("Merci de renseigner le nombre de lettres de votre prénom: ")
    input("Nombre de lettres de votre nom de famille: ")
    sleep(2)
    print("Processing...")
    sleep(3)
    print("Processing...")
    sleep(2)
    print("\nT'as vraiment du temps à perdre, toi !\n\n*42*\n")

try_me()
