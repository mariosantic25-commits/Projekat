# Modul za vizualni prikaz rezultata - Orbital Command
# Sadrži funkcije za ispis tabele, Gantt charta i prosjeka
# Autor: [Mario Šantić]

from colorama import init, Fore, Style
init(autoreset=True)


def ispisi_tabelu(zadaci):
    """
    Funkcija za ispis rezultata raspoređivanja u obliku tabele.
    Svaki zadatak se ispisuje u boji prema svom tipu.

    Parametri:
        zadaci - lista zadataka sa izračunatim vrijednostima
    """

    # Mapa boja prema tipu zadatka
    boje = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
    }

    # Mapa naziva tipa zadatka
    tipovi = {
        1: "KRITIČNO",
        2: "NAUČNO  ",
        3: "RUTINSKO",
    }

    print(Fore.CYAN + "\n  === REZULTATI RASPOREĐIVANJA ===\n")

    # Ispis zaglavlja tabele
    print(Fore.WHITE + "  " + "=" * 85)
    print(Fore.CYAN  + f"  {'#':<4} {'Naziv zadatka':<28} {'Tip':<10} "
                       f"{'AT':>4} {'BT':>4} {'CT':>5} {'TAT':>5} {'WT':>5}")
    print(Fore.WHITE + "  " + "=" * 85)

    # Ispis svakog zadatka u odgovarajućoj boji
    for z in zadaci:
        boja  = boje.get(z["tip"], Fore.WHITE)
        tip   = tipovi.get(z["tip"], "NEPOZNAT")

        print(boja + f"  {z['id']:<4} {z['naziv']:<28} {tip:<10} "
                     f"{z['arrival_time']:>4} {z['burst_time']:>4} "
                     f"{z['completion_time']:>5} {z['turnaround_time']:>5} "
                     f"{z['waiting_time']:>5}")

    print(Fore.WHITE + "  " + "=" * 85)

    # Legenda
    print(Fore.WHITE  + "\n  Legenda: "
          + Fore.RED    + "■ KRITIČNO  "
          + Fore.YELLOW + "■ NAUČNO  "
          + Fore.GREEN  + "■ RUTINSKO")

    # Objašnjenje kolona
    print(Fore.WHITE + "\n  AT=Arrival Time  BT=Burst Time  "
                       "CT=Completion Time  TAT=Turnaround Time  WT=Waiting Time")


def ispisi_gantt(gantt_lista):
    """
    Funkcija za ispis Gantt charta u terminalu.
    Prikazuje vremenski raspored izvršavanja zadataka.

    Parametri:
        gantt_lista - lista tuplova (naziv_zadatka, start, kraj)
    """

    print(Fore.CYAN + "\n  === GANTT CHART ===\n")

    # Boje za Gantt blokove
    boje_gantt = [
        Fore.RED, Fore.YELLOW, Fore.GREEN,
        Fore.CYAN, Fore.MAGENTA, Fore.WHITE
    ]

    # Ispis svakog bloka u Gantt chartu
    for index, (naziv, start, kraj) in enumerate(gantt_lista):
        boja     = boje_gantt[index % len(boje_gantt)]
        trajanje = kraj - start

        # Svaka minuta = jedan znak "█"
        blok = "█" * trajanje

        # Skrati naziv ako je predugačak
        kratki_naziv = naziv[:15] if len(naziv) > 15 else naziv

        print(boja + f"  {kratki_naziv:<16} |{blok}| "
              + Fore.WHITE + f"{start} → {kraj} min")

    # Ispis vremenske ose
    if gantt_lista:
        ukupno_vrijeme = gantt_lista[-1][2]
        print(Fore.WHITE + "\n  Vrijeme (min):")
        print(Fore.WHITE + "  " + "".join(
            str(i).ljust(5) for i in range(0, ukupno_vrijeme + 1, 5)
        ))


def ispisi_prosjeke(prosjecno_cekanje, prosjecni_tat):
    """
    Funkcija za ispis prosječnih vrijednosti na kraju analize.

    Parametri:
        prosjecno_cekanje - prosječno waiting time
        prosjecni_tat     - prosječni turnaround time
    """

    print(Fore.YELLOW + "\n  " + "=" * 45)
    print(Fore.WHITE  + "  📊 STATISTIKA MISIJE:")
    print(Fore.YELLOW + "  " + "=" * 45)
    print(Fore.GREEN  + f"  ► Prosječno vrijeme čekanja : "
          + Fore.WHITE + f"{prosjecno_cekanje} min")
    print(Fore.GREEN  + f"  ► Prosječni Turnaround Time : "
          + Fore.WHITE + f"{prosjecni_tat} min")
    print(Fore.YELLOW + "  " + "=" * 45)

    input(Fore.CYAN + "\n  Pritisnite Enter za nastavak...")