# Glavni modul aplikacije Orbital Command
# Autor: Mario Šantić
# Datum: 6/5/2026
# Opis: Simulacija raspoređivanja zadataka na ISS svemirskoj stanici
#       korištenjem CPU scheduling algoritama

# Uvoz potrebnih biblioteka
import os
import sys
# Uvoz pomocnih funkcija iz utils modula
from utils import prikupi_zadatke
# Uvoz SJF modula
from sjf import pokreni_sjf
# Uvoz Priority Scheduling modula
from priority import pokreni_priority
# Uvoz SRTF modula
from srtf import pokreni_srtf
# Uvoz modula za uporednu analizu
from analiza import pokreni_analizu

# Provjera i instalacija colorama biblioteke
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Instaliranje colorama biblioteke...")
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    init(autoreset=True)


def ispisi_ascii_art():
    """
    Funkcija za ispis ASCII art svemirske stanice pri pokretanju programa.
    Koristi colorama za bojanje teksta u terminalu.
    """
    print(Fore.CYAN + """
    *    .  *       .         *    .       *
  .    *        .       *  .       .    *    .
  
         ___________
        |           |
    ====|  ORBITAL  |====[ ]====[ ]====
        |  COMMAND  |
        |___________|
        
  .    *        .       *  .       .    *    .
    *    .  *       .         *    .       *
    """)

    print(Fore.YELLOW + "=" * 50)
    print(Fore.WHITE + "   Dobrodošli u Orbital Command v1.0")
    print(Fore.WHITE + "   ISS Kontrolni Centar - Houston, TX")
    print(Fore.YELLOW + "=" * 50)
    print()


def ispisi_meni():
    """
    Funkcija za ispis glavnog menija aplikacije.
    Prikazuje dostupne algoritme raspoređivanja.
    """
    print(Fore.GREEN + "\n  Odaberite algoritam raspoređivanja:")
    print(Fore.YELLOW + "  " + "-" * 45)
    print(Fore.WHITE  + "  [1] " + Fore.CYAN + "SJF - Rutinski zadaci (Non-Preemptive)")
    print(Fore.WHITE  + "  [2] " + Fore.CYAN + "SRTF - Hitni zadaci (Preemptive)")
    print(Fore.WHITE  + "  [3] " + Fore.CYAN + "Priority Scheduling - Misijski prioriteti")
    print(Fore.WHITE  + "  [4] " + Fore.CYAN + "Uporedna analiza svih algoritama")
    print(Fore.WHITE  + "  [5] " + Fore.RED  + "Izlaz iz sistema")
    print(Fore.YELLOW + "  " + "-" * 45)


def main():
    """
    Glavna funkcija programa.
    Kontroliše tok aplikacije i poziva odgovarajuće algoritme.
    """
    # Čišćenje terminala pri pokretanju
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ispis ASCII arta i dobrodošlice
    ispisi_ascii_art()

    # Glavna petlja programa
    while True:

        # Ispis menija
        ispisi_meni()

        # Unos korisnika
        print(Fore.GREEN + "\n  >> Vaš odabir: ", end="")
        odabir = input().strip()

        # Obrada odabira
        if odabir == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            ispisi_ascii_art()
            pokreni_sjf()

        elif odabir == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            ispisi_ascii_art()
            pokreni_srtf()

        elif odabir == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            ispisi_ascii_art()
            pokreni_priority()

        elif odabir == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            ispisi_ascii_art()
            pokreni_analizu()

        elif odabir == "5":
            # Izlaz iz aplikacije
            os.system('cls' if os.name == 'nt' else 'clear')
            ispisi_ascii_art()
            print(Fore.RED + "  Gasim sistem... Zbogom, Houston!")
            print(Fore.CYAN + "  *signal prekinut*\n")
            sys.exit(0)

        else:
            # Pogrešan unos
            print(Fore.RED + "\n  ⚠ Pogrešan odabir! Unesite broj između 1 i 5.")


# Pokretanje programa
if __name__ == "__main__":
    main()