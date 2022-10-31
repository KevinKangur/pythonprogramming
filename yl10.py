nimi = input("Sisestage oma nimi: ")

print("Tere,", nimi + "!")

koht = input("Sisestage oma elukoht: ")

if koht.lower() == "saaremaa":
    print("Ikka üks kena saarlane!")

vanus = int(input("Sisestage oma vanus: "))

if vanus < 18:
    print("Kasutaja on liiga noor.")
elif vanus == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Kasutaja võib autot juhtida.")