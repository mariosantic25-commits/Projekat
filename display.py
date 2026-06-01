# Modul za vizualni prikaz rezultata - Orbital Command
# Sadrži funkcije za ispis tabele, Gantt charta i prosjeka
# Autor: [Mario]

from colorama import init, Fore, Style
init(autoreset=True)

def ispisi_tabelu(zadaci):
    """
    Funkcija za ispis rezultata raspoređivanja u obliku tabele.
    Nazivi koji su predugački se skraćuju da ne pomjeraju kolone.

    Parametri:
        zadaci - lista zadataka sa izračunatim vrijednostima
    """

    boje = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
    }

    tipovi = {
        1: "KRITIČNO",
        2: "NAUČNO  ",
        3: "RUTINSKO",
    }

    print(Fore.CYAN + "\n  === REZULTATI RASPOREĐIVANJA ===\n")

    # Fiksne širine kolona
    w_id    = 4
    w_naziv = 25  # Naziv se skraćuje na 25 znakova
    w_tip   = 11
    w_num   = 6

    # Zaglavlje
    print(Fore.WHITE + "  " + "=" * 76)
    print(Fore.CYAN  +
          f"  {'#':<{w_id}}"
          f"{'Naziv zadatka':<{w_naziv}}"
          f"{'Tip':<{w_tip}}"
          f"{'AT':>{w_num}}"
          f"{'BT':>{w_num}}"
          f"{'CT':>{w_num}}"
          f"{'TAT':>{w_num}}"
          f"{'WT':>{w_num}}")
    print(Fore.WHITE + "  " + "=" * 76)

    # Redovi tabele
    for z in zadaci:
        boja = boje.get(z["tip"], Fore.WHITE)
        tip  = tipovi.get(z["tip"], "NEPOZNAT")

        # Skrati naziv na max 24 znaka da ne pomjera kolone
        naziv = z['naziv'][:24] if len(z['naziv']) > 24 else z['naziv']

        print(boja +
              f"  {str(z['id']):<{w_id}}"
              f"{naziv:<{w_naziv}}"
              f"{tip:<{w_tip}}"
              f"{z['arrival_time']:>{w_num}}"
              f"{z['burst_time']:>{w_num}}"
              f"{z['completion_time']:>{w_num}}"
              f"{z['turnaround_time']:>{w_num}}"
              f"{z['waiting_time']:>{w_num}}")

    print(Fore.WHITE + "  " + "=" * 76)

    print(Fore.WHITE  + "\n  Legenda: "
          + Fore.RED    + "■ KRITIČNO  "
          + Fore.YELLOW + "■ NAUČNO  "
          + Fore.GREEN  + "■ RUTINSKO")

    print(Fore.WHITE + "\n  AT=Arrival Time  BT=Burst Time  "
                       "CT=Completion Time  TAT=Turnaround Time  WT=Waiting Time")


def ispisi_gantt(gantt_lista):
    """
    Funkcija za ispis Gantt charta u terminalu.
    Prikazuje blokove sa vremenom start → kraj pored svakog reda.

    Parametri:
        gantt_lista - lista tuplova (naziv_zadatka, start, kraj)
    """

    print(Fore.CYAN + "\n  === GANTT CHART ===\n")

    boje_gantt = [
        Fore.RED, Fore.YELLOW, Fore.GREEN,
        Fore.CYAN, Fore.MAGENTA, Fore.WHITE
    ]

    ukupno_vrijeme = gantt_lista[-1][2] if gantt_lista else 0
    SKALA = 1

    for index, (naziv, start, kraj) in enumerate(gantt_lista):
        boja     = boje_gantt[index % len(boje_gantt)]
        trajanje = kraj - start

        razmak = " " * (start * SKALA)
        blok   = "█" * (trajanje * SKALA)

        kratki_naziv = naziv[:14] if len(naziv) > 14 else naziv

        # Blok + vrijeme s desne strane
        print(boja +
              f"  {kratki_naziv:<15}|{razmak}{blok} {start} → {kraj} min")

    # Jednostavna tekstualna osa na dnu
    print(Fore.WHITE + "\n  Ukupno trajanje misije: "
          + Fore.CYAN + f"{ukupno_vrijeme} min")

def ispisi_prosjeke(prosjecno_cekanje, prosjecni_tat):
    """
    Funkcija za ispis prosječnih vrijednosti na kraju analize.

    Parametri:
        prosjecno_cekanje - prosječno waiting time
        prosjecni_tat     - prosječni turnaround time
    """

    print(Fore.YELLOW + "\n  " + "=" * 45)
    print(Fore.WHITE  + "  STATISTIKA MISIJE:")
    print(Fore.YELLOW + "  " + "=" * 45)
    print(Fore.GREEN  + "  >> Prosjecno vrijeme cekanja : "
          + Fore.WHITE + f"{prosjecno_cekanje} min")
    print(Fore.GREEN  + "  >> Prosjecni Turnaround Time : "
          + Fore.WHITE + f"{prosjecni_tat} min")
    print(Fore.YELLOW + "  " + "=" * 45)

    input(Fore.CYAN + "\n  Pritisnite Enter za nastavak...")