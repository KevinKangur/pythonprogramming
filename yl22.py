import random

while True:

    user_choice = input('Vali kas kivi, paber või käärid (vali lõpeta kui tahad lõpetada mängimist): ').lower()

    choices = ['kivi', 'paber', 'käärid']
    computer_choice = random.choice(choices)

    if user_choice == "lõpeta":
        print("Tänan mängimast!")
        break

    print(f"Sina valisid {user_choice}, arvuti valis {computer_choice}.")

    if user_choice == computer_choice:
        print(f"Mõlemad valisid {user_choice}. Viik!")
    elif user_choice == "kivi" and computer_choice == "käärid":
        print("Kivi võidab kääre! Sa võitsid!")
    elif user_choice == "paber" and computer_choice == "kivi":
        print("Paber võidab kivi! Sa võitsid!")
    elif user_choice == "käärid" and computer_choice == "paber":
        print("Käärid võidab paberit! Sa võitsid!")
    else:
        print("Sa kaotasid.")