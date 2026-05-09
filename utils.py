# Pomoćni modul aplikacije Orbital Command
# Sadrži funkcije za unos podataka, validaciju i računanje rezultata
# Autor: [Mario Šantić]

import random
from colorama import init, Fore, Style
init(autoreset=True)

# ===============================================================
# Konstante - tipovi zadataka i njihovi prioriteti
# ===============================================================

# Tipovi misija na svemirskoj stanici
TIPOVI_ZADATAKA = {
    1: ("KRITIČNO  ", Fore.RED,    "Popravak kvara na stanici"),
    2: ("NAUČNO    ", Fore.YELLOW, "Eksperiment u laboratoriji"),
    3: ("RUTINSKO  ", Fore.GREEN,  "Čišćenje i fizičke vježbe"),
}

# Primjeri stvarnih zadataka po tipu (za random generator)
PRIMJERI_ZADATAKA = {
    1: [
        "Popravak solarnog panela",
        "Kvar na sistemu za kisik",
        "Popravak komunikacijskog modula",
        "Hitna zamjena filtera zraka",
        "Kvar na sistemu za vodu",
    ],
    2: [
        "Uzorkovanje kristala u mikrogravitaciji",
        "Posmatranje Zemljine atmosfere",
        "Eksperiment sa biljkama u svemiru",
        "Testiranje novog goriva",
        "Analiza kosmičkog zračenja",
    ],
    3: [
        "Čišćenje laboratorijskog modula",
        "Dnevne fizičke vježbe",
        "Pregled i sređivanje opreme",
        "Priprema obroka za posadu",
        "Redovni zdravstveni pregled",
    ],
}


# ===============================================================
# Funkcije za unos i validaciju podataka
# ===============================================================

def unesi_cijeli_broj(poruka, min_vrijednost=0, max_vrijednost=9999):
    """
    Funkcija za siguran unos cijelog broja od korisnika.
    Ponavlja unos dok korisnik ne unese ispravan broj.
    
    Parametri:
        poruka        - tekst koji se prikazuje korisniku
        min_vrijednost - minimalna dozvoljena vrijednost
        max_vrijednost - maksimalna dozvoljena vrijednost
    
    Vraća:
        Ispravan cijeli broj unutar zadanog raspona
    """
    while True:
        try:
            print(Fore.GREEN + poruka, end="")
            vrijednost = int(input().strip())

            # Provjera da li je broj unutar dozvoljenog raspona
            if min_vrijednost <= vrijednost <= max_vrijednost:
                return vrijednost
            else:
                print(Fore.RED + f"  ⚠ Unesite broj između {min_vrijednost} i {max_vrijednost}!")

        except ValueError:
            # Korisnik je unio nešto što nije broj
            print(Fore.RED + "  ⚠ Neispravan unos! Molimo unesite broj.")


def unesi_tip_zadatka():
    """
    Funkcija za odabir tipa zadatka.
    Prikazuje dostupne tipove i vraća odabrani tip.
    
    Vraća:
        Broj koji predstavlja tip zadatka (1, 2 ili 3)
    """
    print(Fore.CYAN + "\n  Tipovi zadataka:")
    print(Fore.YELLOW + "  " + "-" * 35)

    # Ispis dostupnih tipova zadataka sa bojama
    for kljuc, (naziv, boja, opis) in TIPOVI_ZADATAKA.items():
        print(f"  {Fore.WHITE}[{kljuc}] {boja}{naziv} {Fore.WHITE}- {opis}")

    print(Fore.YELLOW + "  " + "-" * 35)

    # Unos i validacija odabira
    return unesi_cijeli_broj("  >> Odaberite tip zadatka: ", 1, 3)


def unesi_zadatke_rucno(broj_zadataka):
    """
    Funkcija za ručni unos podataka o zadacima od strane korisnika.
    Za svaki zadatak traži: naziv, tip, arrival time i burst time.
    
    Parametri:
        broj_zadataka - ukupan broj zadataka koji se unose
    
    Vraća:
        Listu rječnika sa podacima o zadacima
    """
    zadaci = []

    for i in range(1, broj_zadataka + 1):
        print(Fore.CYAN + f"\n  --- Zadatak {i} ---")
        print(Fore.YELLOW + "  " + "-" * 35)

        # Unos naziva zadatka
        print(Fore.GREEN + "  Naziv zadatka: ", end="")
        naziv = input().strip()

        # Ako korisnik ne unese naziv, dodjeli generički
        if not naziv:
            naziv = f"Zadatak_{i}"

        # Unos tipa zadatka
        tip = unesi_tip_zadatka()

        # Unos vremena dolaska zadatka (kada je primljen od Zemlje)
        arrival_time = unesi_cijeli_broj(
            "  Arrival Time - Kada pristiže zadatak (min): ",
            0, 999
        )

        # Unos burst time (koliko vremena treba astronautu)
        burst_time = unesi_cijeli_broj(
            "  Burst Time - Trajanje zadatka (min): ",
            1, 999
        )

        # Kreiranje rječnika sa podacima o zadatku
        zadatak = {
            "id"          : i,
            "naziv"       : naziv,
            "tip"         : tip,
            "prioritet"   : tip,        # Prioritet = tip (1=kritično, 3=rutinsko)
            "arrival_time": arrival_time,
            "burst_time"  : burst_time,
            "preostalo"   : burst_time, # Koristi se u SRTF algoritmu
        }

        zadaci.append(zadatak)

    return zadaci


def generiraj_random_zadatke(broj_zadataka):
    """
    Funkcija za automatsko generiranje random zadataka.
    Korisna za brzo testiranje algoritama bez ručnog unosa.
    
    Parametri:
        broj_zadataka - ukupan broj zadataka koji se generiraju
    
    Vraća:
        Listu rječnika sa random podacima o zadacima
    """
    zadaci = []

    print(Fore.YELLOW + "\n  Generiranje random zadataka...")

    for i in range(1, broj_zadataka + 1):

        # Random odabir tipa zadatka (1, 2 ili 3)
        tip = random.randint(1, 3)

        # Random odabir naziva iz liste primjera za taj tip
        naziv = random.choice(PRIMJERI_ZADATAKA[tip])

        # Random arrival time između 0 i 20 minuta
        arrival_time = random.randint(0, 20)

        # Random burst time između 1 i 15 minuta
        burst_time = random.randint(1, 15)

        zadatak = {
            "id"          : i,
            "naziv"       : naziv,
            "tip"         : tip,
            "prioritet"   : tip,
            "arrival_time": arrival_time,
            "burst_time"  : burst_time,
            "preostalo"   : burst_time,
        }

        zadaci.append(zadatak)
        print(Fore.GREEN + f"  ✓ Generiran: [{i}] {naziv} "
              f"(AT:{arrival_time} BT:{burst_time})")

    return zadaci


def prikupi_zadatke():
    """
    Glavna funkcija za prikupljanje zadataka.
    Nudi korisniku izbor između ručnog unosa i random generatora.
    
    Vraća:
        Listu zadataka spremnih za obradu algoritmom
    """
    print(Fore.CYAN + "\n  Način unosa zadataka:")
    print(Fore.YELLOW + "  " + "-" * 35)
    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Ručni unos podataka")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Random generator zadataka")
    print(Fore.YELLOW + "  " + "-" * 35)

    nacin = unesi_cijeli_broj("  >> Vaš odabir: ", 1, 2)

    # Unos broja zadataka (između 2 i 10)
    broj_zadataka = unesi_cijeli_broj(
        "\n  Unesite broj zadataka (2-10): ",
        2, 10
    )

    # Poziv odgovarajuće funkcije za unos
    if nacin == 1:
        return unesi_zadatke_rucno(broj_zadataka)
    else:
        return generiraj_random_zadatke(broj_zadataka)


# ===============================================================
# Funkcije za računanje rezultata
# ===============================================================

def izracunaj_prosjeke(zadaci):
    """
    Funkcija za računanje prosječnog vremena čekanja
    i prosječnog turnaround time-a.
    
    Parametri:
        zadaci - lista zadataka sa izračunatim vrijednostima
    
    Vraća:
        Tuple (prosjecno_cekanje, prosjecni_tat)
    """
    ukupno_cekanje = sum(z["waiting_time"] for z in zadaci)
    ukupno_tat     = sum(z["turnaround_time"] for z in zadaci)
    broj           = len(zadaci)

    prosjecno_cekanje = round(ukupno_cekanje / broj, 2)
    prosjecni_tat     = round(ukupno_tat / broj, 2)

    return prosjecno_cekanje, prosjecni_tat