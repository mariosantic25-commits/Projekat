# Modul za Priority Scheduling algoritam - Orbital Command
# Scenarij: Zadaci se raspoređuju prema tipu/prioritetu misije
# Kritični zadaci uvijek imaju prednost nad ostalima
# Autor: Mario

from colorama import init, Fore, Style
init(autoreset=True)

from utils import prikupi_zadatke, izracunaj_prosjeke
from display import ispisi_tabelu, ispisi_gantt, ispisi_prosjeke


def priority_algoritam(zadaci):
    """
    Implementacija Priority Scheduling algoritma.
    Zadaci se raspoređuju prema prioritetu (tip zadatka).
    Prioritet 1 (KRITIČNO) je najviši, 3 (RUTINSKO) je najniži.
    Pri jednakom prioritetu, prednost ima zadatak sa manjim arrival time.

    Parametri:
        zadaci - lista zadataka sa arrival_time, burst_time i prioritet

    Vraća:
        Listu završenih zadataka sa izračunatim vrijednostima i Gantt listu
    """

    # Kopija liste sortirana po arrival time
    neobavljeni = sorted(zadaci, key=lambda z: z["arrival_time"])

    zavrseni         = []
    gantt            = []
    trenutno_vrijeme = 0

    print(Fore.CYAN + "\n  Simulacija Priority Scheduling algoritma u toku...")

    while neobavljeni:

        # Filtriraj zadatke koji su već stigli
        dostupni = [
            z for z in neobavljeni
            if z["arrival_time"] <= trenutno_vrijeme
        ]

        if not dostupni:
            # Nema dostupnih zadataka, skočimo na sljedeći arrival time
            trenutno_vrijeme = neobavljeni[0]["arrival_time"]
            continue

        # Odabir zadatka sa najvišim prioritetom (najmanji broj = viši prioritet)
        # Pri jednakom prioritetu uzima onaj koji je ranije stigao
        odabrani = min(
            dostupni,
            key=lambda z: (z["prioritet"], z["arrival_time"])
        )

        # Ukloni iz liste neobavljenih
        neobavljeni.remove(odabrani)

        # Računanje vremena
        start           = trenutno_vrijeme
        kraj            = start + odabrani["burst_time"]
        completion_time = kraj
        turnaround_time = completion_time - odabrani["arrival_time"]
        waiting_time    = turnaround_time - odabrani["burst_time"]

        # Spremi izračunate vrijednosti
        odabrani["completion_time"]  = completion_time
        odabrani["turnaround_time"]  = turnaround_time
        odabrani["waiting_time"]     = waiting_time

        # Dodaj u Gantt listu
        gantt.append((odabrani["naziv"], start, kraj, odabrani["tip"]))

        # Dodaj u završene
        zavrseni.append(odabrani)

        # Ispis napretka simulacije
        prioritet_tekst = {
            1: Fore.RED    + "KRITIČNO",
            2: Fore.YELLOW + "NAUČNO  ",
            3: Fore.GREEN  + "RUTINSKO",
        }.get(odabrani["tip"], Fore.WHITE + "NEPOZNAT")

        print(Fore.GREEN + f"  ✓ [{start}-{kraj} min] "
              + Fore.WHITE + f"{odabrani['naziv']} "
              + f"[{prioritet_tekst}" + Fore.WHITE + "]")

        trenutno_vrijeme = kraj

    return zavrseni, gantt


def pokreni_priority():
    """
    Glavna funkcija Priority Scheduling modula.
    Prikuplja zadatke, pokreće algoritam i prikazuje rezultate.
    """

    print(Fore.CYAN + "\n  ╔══════════════════════════════════╗")
    print(Fore.CYAN + "  ║   PRIORITY SCHEDULING            ║")
    print(Fore.CYAN + "  ║   Misijski prioriteti ISS        ║")
    print(Fore.CYAN + "  ╚══════════════════════════════════╝")

    # Objašnjenje prioriteta korisniku
    print(Fore.WHITE + "\n  Prioriteti zadataka:")
    print(Fore.YELLOW + "  " + "-" * 35)
    print(Fore.RED    + "  [1] KRITIČNO  — Popravci i hitne situacije")
    print(Fore.YELLOW + "  [2] NAUČNO    — Eksperimenti i istraživanje")
    print(Fore.GREEN  + "  [3] RUTINSKO  — Čišćenje i svakodnevne aktivnosti")
    print(Fore.YELLOW + "  " + "-" * 35)

    # Prikupljanje zadataka
    zadaci = prikupi_zadatke()

    # Pokretanje algoritma
    rezultati, gantt = priority_algoritam(zadaci)

    # Prikaz rezultata
    ispisi_tabelu(rezultati)
    ispisi_gantt(gantt)

    # Računanje i prikaz prosjeka
    prosjecno_cekanje, prosjecni_tat = izracunaj_prosjeke(rezultati)
    ispisi_prosjeke(prosjecno_cekanje, prosjecni_tat)