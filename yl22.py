import random

while True:

    user_choice = input('Vali kas kivi, paber või käärid: ').lower()

    choices = ['kivi', 'paber', 'käärid']
    computer_choice = random.choice(choices)

    print(f"Sina valisid {user_choice}, arvuti valis {computer_choice}.")

    if user_choice == computer_choice:
        print(f"Mõlemad valisid {user_choice}. Viik!")
    elif user_choice == "kivi":
        if computer_choice == "käärid":
            print("Kivi võidab kääre! Sa võitsid!")
        else:
            print("Paber võidab kivi! Sa kaotasid.")
    elif user_choice == "paber":
        if computer_choice == "kivi":
            print("Paber võidab kivi! Sa võitsid!")
        else:
            print("Käärid võidab paberit! Sa kaotasid.")
    elif user_choice == "käärid":
        if computer_choice == "paber":
            print("Käärid võidab paberit! Sa võitsid!")
        else:
            print("Kivi võidab kääre! Sa kaotasid.")

    play_again = input("Mängi uuesti? (jah/ei): ")
    if play_again.lower() != "jah":
        break