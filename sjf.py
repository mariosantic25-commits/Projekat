# Modul za SJF (Shortest Job First) Non-Preemptive algoritam
# Scenarij: Rutinski zadaci se raspoređuju po trajanju
# Zadatak sa najkraćim burst time-om ide prvi
# Autor: [Mario]

from colorama import init, Fore, Style
init(autoreset=True)

from utils import prikupi_zadatke, izracunaj_prosjeke
from display import ispisi_tabelu, ispisi_gantt, ispisi_prosjeke


def sjf_algoritam(zadaci):
    """
    Implementacija SJF Non-Preemptive algoritma.
    Zadatak koji je stigao i ima najkraći burst time se izvršava prvi.
    Jednom započet zadatak se ne može prekinuti.

    Parametri:
        zadaci - lista zadataka sa arrival_time i burst_time

    Vraća:
        Listu zadataka sa izračunatim vrijednostima i Gantt listu
    """

    # Kopija liste da ne mijenjamo originalne podatke
    neobavljeni = sorted(zadaci, key=lambda z: z["arrival_time"])

    # Lista završenih zadataka i Gantt chart podaci
    zavrseni  = []
    gantt     = []

    # Trenutno vrijeme simulacije
    trenutno_vrijeme = 0

    print(Fore.CYAN + "\n  Simulacija SJF algoritma u toku...")

    # Petlja dok ima neobavljenih zadataka
    while neobavljeni:

        # Filtriraj zadatke koji su već stigli
        dostupni = [
            z for z in neobavljeni
            if z["arrival_time"] <= trenutno_vrijeme
        ]

        if not dostupni:
            # Nema dostupnih zadataka, preskočimo na sljedeći arrival time
            trenutno_vrijeme = neobavljeni[0]["arrival_time"]
            continue

        # Odabir zadatka sa najkraćim burst time-om (SJF princip)
        odabrani = min(dostupni, key=lambda z: z["burst_time"])

        # Ukloni odabrani zadatak iz liste neobavljenih
        neobavljeni.remove(odabrani)

        # Računanje vremena
        start             = trenutno_vrijeme
        kraj              = start + odabrani["burst_time"]
        completion_time   = kraj
        turnaround_time   = completion_time - odabrani["arrival_time"]
        waiting_time      = turnaround_time - odabrani["burst_time"]

        # Dodaj izračunate vrijednosti u zadatak
        odabrani["completion_time"]  = completion_time
        odabrani["turnaround_time"]  = turnaround_time
        odabrani["waiting_time"]     = waiting_time

        # Dodaj u Gantt listu
        gantt.append((odabrani["naziv"], start, kraj))

        # Dodaj u listu završenih
        zavrseni.append(odabrani)

        # Napredak simulacije
        print(Fore.GREEN + f"  ✓ [{start}-{kraj} min] "
              + Fore.WHITE + f"{odabrani['naziv']}")

        # Pomjeri trenutno vrijeme
        trenutno_vrijeme = kraj

    return zavrseni, gantt


def pokreni_sjf():
    """
    Glavna funkcija SJF modula.
    Prikuplja zadatke, pokreće algoritam i prikazuje rezultate.
    """

    print(Fore.CYAN + "\n  ╔══════════════════════════════════╗")
    print(Fore.CYAN + "  ║   SJF - SHORTEST JOB FIRST      ║")
    print(Fore.CYAN + "  ║   Rutinsko raspoređivanje ISS    ║")
    print(Fore.CYAN + "  ╚══════════════════════════════════╝")

    # Prikupljanje zadataka od korisnika
    zadaci = prikupi_zadatke()

    # Pokretanje SJF algoritma
    rezultati, gantt = sjf_algoritam(zadaci)

    # Prikaz rezultata
    ispisi_tabelu(rezultati)
    ispisi_gantt(gantt)

    # Računanje i prikaz prosjeka
    prosjecno_cekanje, prosjecni_tat = izracunaj_prosjeke(rezultati)
    ispisi_prosjeke(prosjecno_cekanje, prosjecni_tat)