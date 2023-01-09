import random

while True:

    valik = input('Vali kas kivi, paber või käärid: ').lower()

    kpk = ['kivi', 'paber', 'käärid']
    valikrandom = random.choice(kpk)

    print(f"Sina valisid {valik}, arvuti valis {valikrandom}.")

    if valik == valikrandom:
        print(f"Mõlemad valisid {valik}. Viik!")
    elif valik == "kivi":
        if valikrandom == "käärid":
            print("Kivi võidab kääre! Sa võitsid!")
        else:
            print("Paber võidab kivi! Sa kaotasid.")
    elif valik == "paber":
        if valikrandom == "kivi":
            print("Paber võidab kivi! Sa võitsid!")
        else:
            print("Käärid võidab paberit! Sa kaotasid.")
    elif valik == "käärid":
        if valikrandom == "paber":
            print("Käärid võidab paberit! Sa võitsid!")
        else:
            print("Kivi võidab kääre! Sa kaotasid.")

    mängiuuesti = input("Mängi uuesti? (jah/ei): ")
    if mängiuuesti.lower() != "jah":
        break