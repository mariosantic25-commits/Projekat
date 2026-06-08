# Modul za SRTF (Shortest Remaining Time First) algoritam - Orbital Command
# Scenarij: Hitni zadaci mogu prekinuti trenutni zadatak
# Simulacija se odvija minuta po minuta
# Autor: [Mario]

from colorama import init, Fore, Style
init(autoreset=True)

from utils import prikupi_zadatke, izracunaj_prosjeke
from display import ispisi_tabelu, ispisi_gantt, ispisi_prosjeke
from astronauts import reset_astronauta, dodijeli_zadatak, ispisi_statistiku_astronauta


def srtf_algoritam(zadaci):
    """
    Implementacija SRTF (Shortest Remaining Time First) algoritma.
    Svake minute provjerava da li novi zadatak ima kraće preostalo vrijeme.
    Ako ima, trenutni zadatak se prekida i novi preuzima CPU.

    Parametri:
        zadaci - lista zadataka sa arrival_time i burst_time

    Vraća:
        Listu završenih zadataka sa izračunatim vrijednostima i Gantt listu
    """

    # Inicijalizacija preostalog vremena za svaki zadatak
    for z in zadaci:
        z["preostalo"]       = z["burst_time"]
        z["completion_time"] = 0
        z["waiting_time"]    = 0
        z["turnaround_time"] = 0

    zavrseni         = []
    gantt            = []
    trenutno_vrijeme = 0
    trenutni_zadatak = None
    gantt_start      = 0

    # Ukupno vrijeme simulacije = suma svih burst timeova + max arrival time
    max_vrijeme = sum(z["burst_time"] for z in zadaci) + max(z["arrival_time"] for z in zadaci)

    print(Fore.CYAN + "\n  Simulacija SRTF algoritma u toku...")

    # Simulacija minuta po minuta
    while len(zavrseni) < len(zadaci):

        # Filtriraj zadatke koji su stigli i nisu završeni
        dostupni = [
            z for z in zadaci
            if z["arrival_time"] <= trenutno_vrijeme
            and z not in zavrseni
            and z["preostalo"] > 0
        ]

        if not dostupni:
            # Nema dostupnih zadataka, pomjeri vrijeme
            trenutno_vrijeme += 1
            continue

        # Odabir zadatka sa najkraćim preostanim vremenom
        kandidat = min(dostupni, key=lambda z: z["preostalo"])

        # Provjera da li trebamo prekinuti trenutni zadatak (preemption)
        if trenutni_zadatak != kandidat:

            # Spremi Gantt blok za prethodni zadatak ako postoji
            if trenutni_zadatak is not None and gantt_start < trenutno_vrijeme:
                gantt.append((
                    trenutni_zadatak["naziv"],
                    gantt_start,
                    trenutno_vrijeme,
                    trenutni_zadatak["tip"]
                ))

                # Ispis preemption poruke
                if trenutni_zadatak not in zavrseni:
                    print(Fore.YELLOW +
                          f"  ⚡ Preemption na {trenutno_vrijeme} min! "
                          + Fore.WHITE +
                          f"{trenutni_zadatak['naziv'][:20]} prekinut, "
                          f"preostalo: {trenutni_zadatak['preostalo']} min")

            # Postavi novog trenutnog
            trenutni_zadatak = kandidat
            gantt_start      = trenutno_vrijeme

        # Izvrši jedan minut trenutnog zadatka
        trenutni_zadatak["preostalo"] -= 1
        trenutno_vrijeme += 1

        # Provjeri da li je zadatak završen
        if trenutni_zadatak["preostalo"] == 0:

            # Spremi završni Gantt blok
            gantt.append((
                trenutni_zadatak["naziv"],
                gantt_start,
                trenutno_vrijeme,
                trenutni_zadatak["tip"]
            ))

            # Izračunaj vrijednosti
            trenutni_zadatak["completion_time"]  = trenutno_vrijeme
            trenutni_zadatak["turnaround_time"]  = (
                trenutno_vrijeme - trenutni_zadatak["arrival_time"]
            )
            trenutni_zadatak["waiting_time"]     = (
                trenutni_zadatak["turnaround_time"] - trenutni_zadatak["burst_time"]
            )

            zavrseni.append(trenutni_zadatak)

            print(Fore.GREEN +
                  f"  ✓ [{gantt_start}-{trenutno_vrijeme} min] "
                  + Fore.WHITE +
                  f"{trenutni_zadatak['naziv']} završen!")

            trenutni_zadatak = None

        # Zaštita od beskonačne petlje
        if trenutno_vrijeme > max_vrijeme + 10:
            break

    return zavrseni, gantt


def spoji_gantt_blokove(gantt):
    """
    Funkcija koja spaja uzastopne Gantt blokove istog zadatka.
    Smanjuje broj redova u Gantt chartu za bolji prikaz.

    Parametri:
        gantt - originalna Gantt lista sa svim blokovima

    Vraća:
        Spojenu Gantt listu
    """

    if not gantt:
        return gantt

    spojena = [gantt[0]]

    for trenutni in gantt[1:]:
        prethodni = spojena[-1]

        # Ako je isti zadatak i nastavlja se odmah — spoji
        if (trenutni[0] == prethodni[0] and
                trenutni[1] == prethodni[2] and
                trenutni[3] == prethodni[3]):
            spojena[-1] = (prethodni[0], prethodni[1], trenutni[2], prethodni[3])
        else:
            spojena.append(trenutni)

    return spojena


def pokreni_srtf():
    """
    Glavna funkcija SRTF modula.
    Prikuplja zadatke, pokreće algoritam i prikazuje rezultate.
    """

    print(Fore.CYAN + "\n  ╔══════════════════════════════════╗")
    print(Fore.CYAN + "  ║   SRTF - SHORTEST REMAINING      ║")
    print(Fore.CYAN + "  ║   TIME FIRST - Hitni zadaci ISS  ║")
    print(Fore.CYAN + "  ╚══════════════════════════════════╝")

    print(Fore.WHITE + "\n  Napomena: Kritični zadaci mogu")
    print(Fore.WHITE +   "  prekinuti trenutni zadatak ako")
    print(Fore.WHITE +   "  imaju kraće preostalo vrijeme!\n")

    # Prikupljanje zadataka
    zadaci = prikupi_zadatke()

    # Pokretanje algoritma
    rezultati, gantt = srtf_algoritam(zadaci)

    # Spajanje uzastopnih blokova istog zadatka u Gantt chartu
    gantt_spojen = spoji_gantt_blokove(gantt)

    # Prikaz rezultata
    ispisi_tabelu(rezultati)
    ispisi_gantt(gantt_spojen)

    # Računanje i prikaz prosjeka
    prosjecno_cekanje, prosjecni_tat = izracunaj_prosjeke(rezultati)
    ispisi_prosjeke(prosjecno_cekanje, prosjecni_tat)

    # Dodjela zadataka astronautima i ispis statistike
    reset_astronauta()
    for z in rezultati:
        dodijeli_zadatak(z)
    ispisi_statistiku_astronauta()