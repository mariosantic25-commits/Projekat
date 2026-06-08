# Modul za uporednu analizu algoritama - Orbital Command
# Pokreće sva tri algoritma na istim zadacima i poredi rezultate
# Autor: [Mario]

from colorama import init, Fore, Style
init(autoreset=True)

from utils import prikupi_zadatke, izracunaj_prosjeke
from sjf import sjf_algoritam
from srtf import srtf_algoritam
from priority import priority_algoritam
import copy


def pokreni_analizu():
    """
    Funkcija za uporednu analizu sva tri algoritma.
    Koristi iste zadatke za sve algoritme i poredi rezultate.
    """

    print(Fore.CYAN + "\n  ╔══════════════════════════════════╗")
    print(Fore.CYAN + "  ║   UPOREDNA ANALIZA ALGORITAMA    ║")
    print(Fore.CYAN + "  ║   SJF vs SRTF vs PRIORITY        ║")
    print(Fore.CYAN + "  ╚══════════════════════════════════╝")

    print(Fore.WHITE + "\n  Unesite zadatke jednom —")
    print(Fore.WHITE +   "  svi algoritmi će koristiti iste!\n")

    # Prikupi zadatke jednom za sve algoritme
    zadaci = prikupi_zadatke()

    # Pokretanje svakog algoritma na kopiji zadataka
    print(Fore.YELLOW + "\n  Pokretanje SJF algoritma...")
    rezultati_sjf, _      = sjf_algoritam(copy.deepcopy(zadaci))

    print(Fore.YELLOW + "\n  Pokretanje SRTF algoritma...")
    rezultati_srtf, _     = srtf_algoritam(copy.deepcopy(zadaci))

    print(Fore.YELLOW + "\n  Pokretanje Priority algoritma...")
    rezultati_priority, _ = priority_algoritam(copy.deepcopy(zadaci))

    # Računanje prosjeka za svaki algoritam
    sjf_cekanje,      sjf_tat      = izracunaj_prosjeke(rezultati_sjf)
    srtf_cekanje,     srtf_tat     = izracunaj_prosjeke(rezultati_srtf)
    priority_cekanje, priority_tat = izracunaj_prosjeke(rezultati_priority)

    # Prikaz uporedne tabele
    ispisi_uporednu_tabelu(
        sjf_cekanje,      sjf_tat,
        srtf_cekanje,     srtf_tat,
        priority_cekanje, priority_tat
    )

    # Prikaz pobjednika
    ispisi_pobjednika(
        sjf_cekanje,      sjf_tat,
        srtf_cekanje,     srtf_tat,
        priority_cekanje, priority_tat
    )

    input(Fore.CYAN + "\n  Pritisnite Enter za nastavak...")


def ispisi_uporednu_tabelu(
        sjf_cekanje,      sjf_tat,
        srtf_cekanje,     srtf_tat,
        priority_cekanje, priority_tat):
    """
    Funkcija za ispis tabele sa rezultatima sva tri algoritma.

    Parametri:
        sjf_cekanje      - prosječno waiting time SJF
        sjf_tat          - prosječni TAT SJF
        srtf_cekanje     - prosječno waiting time SRTF
        srtf_tat         - prosječni TAT SRTF
        priority_cekanje - prosječno waiting time Priority
        priority_tat     - prosječni TAT Priority
    """

    print(Fore.CYAN + "\n  === REZULTATI UPOREDNE ANALIZE ===\n")

    # Zaglavlje tabele
    print(Fore.WHITE + "  " + "=" * 55)
    print(Fore.CYAN  +
          f"  {'Algoritam':<20}"
          f"{'Prosj. WT':>15}"
          f"{'Prosj. TAT':>15}")
    print(Fore.WHITE + "  " + "=" * 55)

    # Redovi tabele — svaki algoritam u svojoj boji
    print(Fore.YELLOW +
          f"  {'SJF (Non-Preemptive)':<20}"
          f"{sjf_cekanje:>15}"
          f"{sjf_tat:>15}")

    print(Fore.CYAN +
          f"  {'SRTF (Preemptive)':<20}"
          f"{srtf_cekanje:>15}"
          f"{srtf_tat:>15}")

    print(Fore.MAGENTA +
          f"  {'Priority Scheduling':<20}"
          f"{priority_cekanje:>15}"
          f"{priority_tat:>15}")

    print(Fore.WHITE + "  " + "=" * 55)
    print(Fore.WHITE + "\n  WT=Waiting Time  TAT=Turnaround Time  (u minutama)")


def ispisi_pobjednika(
        sjf_cekanje,      sjf_tat,
        srtf_cekanje,     srtf_tat,
        priority_cekanje, priority_tat):
    """
    Funkcija koja određuje i ispisuje koji algoritam je bio najefikasniji
    na osnovu prosječnog waiting time i turnaround time.

    Parametri:
        Prosječni WT i TAT za svaki algoritam
    """

    # Rječnik rezultata za lakšu obradu
    rezultati = {
        "SJF"     : (sjf_cekanje,      sjf_tat),
        "SRTF"    : (srtf_cekanje,     srtf_tat),
        "Priority": (priority_cekanje, priority_tat),
    }

    # Pronađi pobjednika po waiting time
    pobjednik_wt  = min(rezultati, key=lambda k: rezultati[k][0])

    # Pronađi pobjednika po turnaround time
    pobjednik_tat = min(rezultati, key=lambda k: rezultati[k][1])

    print(Fore.CYAN + "\n  === ZAKLJUČAK ANALIZE ===\n")
    print(Fore.YELLOW + "  " + "-" * 45)

    print(Fore.WHITE  + "  Najmanji Waiting Time    : "
          + Fore.GREEN + f"{pobjednik_wt} "
          + Fore.WHITE + f"({rezultati[pobjednik_wt][0]} min)")

    print(Fore.WHITE  + "  Najmanji Turnaround Time : "
          + Fore.GREEN + f"{pobjednik_tat} "
          + Fore.WHITE + f"({rezultati[pobjednik_tat][1]} min)")

    print(Fore.YELLOW + "  " + "-" * 45)

    # Generalni pobjednik — manji zbroj WT + TAT
    pobjednik_generalni = min(
        rezultati,
        key=lambda k: rezultati[k][0] + rezultati[k][1]
    )

    print(Fore.GREEN + f"\n  ★ Najefikasniji algoritam: "
          + Fore.WHITE + f"{pobjednik_generalni}")
    print(Fore.WHITE +
          f"  WT: {rezultati[pobjednik_generalni][0]} min  |  "
          f"TAT: {rezultati[pobjednik_generalni][1]} min")