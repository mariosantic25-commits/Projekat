# 🚀 Orbital Command - ISS Task Scheduler

## Opis projekta
Simulacija raspoređivanja zadataka astronauta na Međunarodnoj
svemirskoj stanici (ISS) korištenjem CPU scheduling algoritama.
Projekt je realizovan kao analogija CPU raspoređivanja procesa
gdje svaki zadatak astronauta predstavlja jedan proces.

## Scenariji

### 1. SJF - Shortest Job First (Non-Preemptive)
Zadatak sa najkraćim burst time-om se izvršava prvi.
Jednom započet zadatak ne može biti prekinut.
Primjer: Rutinski zadaci se raspoređuju po trajanju.

### 2. SRTF - Shortest Remaining Time First (Preemptive)
Ako novi zadatak ima kraće preostalo vrijeme od trenutnog,
trenutni se prekida i novi preuzima izvršavanje.
Primjer: Hitni zadaci mogu prekinuti rutinske.

### 3. Priority Scheduling
Zadaci se raspoređuju prema tipu/prioritetu:
- 🔴 KRITIČNO (prioritet 1) - Popravci i hitne situacije
- 🟡 NAUČNO   (prioritet 2) - Eksperimenti i istraživanje
- 🟢 RUTINSKO (prioritet 3) - Čišćenje i svakodnevne aktivnosti

### 4. Uporedna analiza
Automatski pokreće sva tri algoritma na istim zadacima
i prikazuje koji je bio najefikasniji.

## Posada ISS-a
| Astronaut | Specijalnost | Tip zadataka |
|-----------|-------------|--------------|
| 👨‍🔧 Kozlov | Inženjering | KRITIČNO |
| 👩‍🔬 Chen   | Nauka       | NAUČNO   |
| 👨‍⚕️ Müller | Medicina    | RUTINSKO |

## Pokretanje
```bash
py main.py
```

## Tehnologije
- Python 3.x
- Colorama (boje u terminalu)

## Autor
[Mario Šantić] — [Politehnički fakultet - Softversko inžinjerstvo]