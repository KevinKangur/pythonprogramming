name = input("Sisestage oma nimi: ")

print("Tere,", name + "!")

home = input("Sisestage oma elukoht: ")

if home.lower() == "saaremaa":
    print("Ikka üks kena saarlane!")

age = int(input("Sisestage oma vanus: "))

if age < 18:
    print("Kasutaja on liiga noor.")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Kasutaja võib autot juhtida.")