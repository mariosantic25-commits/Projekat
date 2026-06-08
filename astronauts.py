# Modul za upravljanje astronautima - Orbital Command
# Sadrži podatke o astronautima i logiku dodjele zadataka
# Svaki astronaut ima specijalnost koja odgovara tipu zadatka
# Autor: [Mario]

from colorama import init, Fore, Style
init(autoreset=True)


# ===============================================================
# Podaci o astronautima
# ===============================================================

ASTRONAUTI = {
    1: {
        "ime"         : "Kozlov",
        "uloga"       : "Inženjer",
        "specijalnost": "KRITIČNO",
        "tip"         : 1,
        "boja"        : Fore.RED,
        "emoji"       : "[INZ]",
        "zadaci"      : [],  # Lista dodijeljenih zadataka
    },
    2: {
        "ime"         : "Chen",
        "uloga"       : "Znanstvenik",
        "specijalnost": "NAUČNO",
        "tip"         : 2,
        "boja"        : Fore.YELLOW,
        "emoji"       : "[NAU]",
        "zadaci"      : [],
    },
    3: {
        "ime"         : "Muller",
        "uloga"       : "Medicinar",
        "specijalnost": "RUTINSKO",
        "tip"         : 3,
        "boja"        : Fore.GREEN,
        "emoji"       : "[MED]",
        "zadaci"      : [],
    },
}


# ===============================================================
# Funkcije za dodjelu zadataka
# ===============================================================

def reset_astronauta():
    """
    Funkcija za resetovanje liste zadataka svakog astronauta.
    Poziva se prije svake nove simulacije.
    """
    for astronaut in ASTRONAUTI.values():
        astronaut["zadaci"] = []


def dodijeli_zadatak(zadatak):
    """
    Funkcija za dodjelu zadatka odgovarajućem astronautu.
    Dodjela se vrši prema tipu zadatka i specijalnosti astronauta.

    Parametri:
        zadatak - rječnik sa podacima o zadatku

    Vraća:
        Rječnik sa podacima o astronautu kojemu je dodijeljen zadatak
    """

    # Pronađi astronauta čiji tip odgovara tipu zadatka
    tip = zadatak.get("tip", 3)
    astronaut = ASTRONAUTI.get(tip, ASTRONAUTI[3])

    # Dodaj zadatak u listu astronautovih zadataka
    astronaut["zadaci"].append(zadatak)

    return astronaut


def ispisi_dodjelu(zadatak, astronaut):
    """
    Funkcija za ispis informacije o dodjeli zadatka astronautu.

    Parametri:
        zadatak   - rječnik sa podacima o zadatku
        astronaut - rječnik sa podacima o astronautu
    """

    boja = astronaut["boja"]

    print(boja +
          f"  {astronaut['emoji']} {astronaut['ime']:<8} "
          + Fore.WHITE +
          f"← {zadatak['naziv'][:30]}")


def ispisi_statistiku_astronauta():
    """
    Funkcija za ispis statistike svakog astronauta nakon simulacije.
    Prikazuje broj zadataka, ukupno burst time i prosječno waiting time.
    """

    print(Fore.CYAN + "\n  === STATISTIKA ASTRONAUTA ===\n")
    print(Fore.WHITE + "  " + "=" * 65)
    print(Fore.CYAN  +
          f"  {'Astronaut':<12}"
          f"{'Uloga':<15}"
          f"{'Zadataka':>10}"
          f"{'Ukupno BT':>12}"
          f"{'Prosj. WT':>12}")
    print(Fore.WHITE + "  " + "=" * 65)

    for astronaut in ASTRONAUTI.values():
        zadaci = astronaut["zadaci"]

        # Ako astronaut nema zadataka preskoči
        if not zadaci:
            print(astronaut["boja"] +
                  f"  {astronaut['ime']:<12}"
                  f"{astronaut['uloga']:<15}"
                  + Fore.WHITE +
                  f"{'0':>10}"
                  f"{'0':>12}"
                  f"{'N/A':>12}")
            continue

        # Računanje statistike
        ukupno_bt = sum(z["burst_time"] for z in zadaci)
        ukupno_wt = sum(z.get("waiting_time", 0) for z in zadaci)
        prosj_wt  = round(ukupno_wt / len(zadaci), 2)

        print(astronaut["boja"] +
              f"  {astronaut['ime']:<12}"
              f"{astronaut['uloga']:<15}"
              + Fore.WHITE +
              f"{len(zadaci):>10}"
              f"{ukupno_bt:>12}"
              f"{prosj_wt:>12}")

    print(Fore.WHITE + "  " + "=" * 65)