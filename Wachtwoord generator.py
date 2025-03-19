#programma is gemaakt voor wachtwoorden te genereren.
'''
Opslaan List in txt file



'''
import random
import string
import time

#random cijfers

letter = string.ascii_lowercase
hoofdletters = string.ascii_uppercase
cijfers = string.digits
speciale_tekens = string.punctuation
Wachtwoorden = []

while True:

    def opslaan_txt_file(naam_bestand):
        with open(f"{naam_bestand}.txt", "w") as output:
            output.write(str(Wachtwoorden))

    def randomgeneratie(): #Input user
        hoeveelcijfers = int(input("Hoeveel cijfers moet uw wachtwoord hebben?: "))
        print()
        hoeveelletters = int(input("Hoeveel letters moet uw wachtwoord hebben?: "))
        print()
        hoeveelhoofdletters = int(input("Hoeveel hoofdletters moet uw wachtwoord hebben?: "))
        print()
        hoeveelheid_speciale_tekens = int(input("Hoeveel speciale tekens moet uw wachtwoord hebben?: "))

        global hoeveelheid_teken
        hoeveelheid_teken = hoeveelcijfers + hoeveelletters + hoeveelhoofdletters + hoeveelheid_speciale_tekens

        kiesletter = random.choices(letter, k=int(hoeveelletters))
        kieshoofdletter =random.choices(hoofdletters, k=int(hoeveelhoofdletters))
        kiescijfer = random.choices(cijfers, k=int(hoeveelcijfers))
        kiesspeciale_teken = random.choices(speciale_tekens, k=int(hoeveelheid_speciale_tekens))

        allecijfersletter = kiesspeciale_teken + kiescijfer + kiesletter + kieshoofdletter
        gr = list(allecijfersletter)
        random.shuffle(gr)

        st = ''.join(gr)

        if str.lower(input("Wilt u dit wachtwoord opslaan?")) == "y":
            global Wachtwoorden
            Wachtwoorden.append(st)
        print(Wachtwoorden)


    def wachtwoordverwijderen(): #verwijderd een item in de list
        print(Wachtwoorden)
        keuzeverwijderen = int(input("Welk Wachtwoord wilt u verwijderen?: "))
        Wachtwoorden.pop(int(keuzeverwijderen))

    def wachtwoordtoevoegen(): #User kan custom wachtwoord toevoegen
        wwvragen = str(input("Wat is het wachtwoord wat u wilt toevoegen?: "))
        Wachtwoorden.append(wwvragen)
        print(f"Wachtwoord {wwvragen} toegevoegd")

    print('''
               1. Wachtwoord maken
               2. Lijst van wachtwoorden zien
               3. Wachtwoord verwijderen
               4. Zelf wachtwoord toevoegen
               5. Wachtwoorden opslaan in een TxT bestand

               6. Programma stoppen
           ''') # print lijst met keuze wat de user kan doen
    kiezeninput = int(input("Wat wilt u doen?: "))

    if kiezeninput == 1:
        randomgeneratie()
    elif kiezeninput == 2:
        print(Wachtwoorden)
        print(f"Uw wachtwoord heeft {hoeveelheid_teken} tekens")
    elif kiezeninput == 3:
        wachtwoordverwijderen()
    elif kiezeninput == 4:
        wachtwoordtoevoegen()
    elif kiezeninput == 5:
        naam_bestand = str(input("Naam van het bestand?: "))
        opslaan_txt_file(naam_bestand)
    elif kiezeninput == 6:
        print("Programma wordt gestopt over 0.5 seconden")
        time.sleep(0.5)
        print("STOP PROGRAMMA")
        break
