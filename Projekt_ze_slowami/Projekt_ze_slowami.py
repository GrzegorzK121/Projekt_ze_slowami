def obliczanie_ilosci_slow_kolekcja(kolekcja):
    ilosc_slow = 0
    for element in kolekcja:
        if isinstance(element, str):
            ilosc_slow += len(element.split())
    return ilosc_slow

def obliczanie_ilosci_slow_przykladowyTekst(tekst):
    return len(tekst.split())

def obliczanie_ilosci_znakow(tekst):
    return len(tekst)

def obliczanie_ilosci_znakow_bez_spacji(tekst):
    return len(tekst.replace(" ", ""))

def obliczanie_ilosci_znakow_bialych(tekst):
    ilosc_bialych_znakow = 0
    for znak in tekst:
        if znak.isspace():
            ilosc_bialych_znakow += 1
    return ilosc_bialych_znakow
def obliczanie_ilosci_znakow_kolekcja(kolekcja):
    ilosc_znakow = 0
    for element in kolekcja:
        if isinstance(element, str):
            ilosc_znakow += len(element)
    return ilosc_znakow

def obliczanie_ilosci_znakow_bez_spacji_kolekcja(kolekcja):
    ilosc_znakow_bez_spacji = 0
    for element in kolekcja:
        if isinstance(element, str):
            ilosc_znakow_bez_spacji += len(element.replace(" ", ""))
    return ilosc_znakow_bez_spacji

def obliczanie_ilosci_znakow_bialych_kolekcja(kolekcja):
    ilosc_znakow_bialych = 0
    for element in kolekcja:
        if isinstance(element, str): 
            for znak in element:
                if znak.isspace():
                    ilosc_znakow_bialych += 1
    return ilosc_znakow_bialych



# SprawdŸmy
przykladowaKolekcja = ["Kochajmy siê, ale tak - z osobna. Grzecznoœæ nie jest nauk¹ ³atw¹ ani ma³¹. Grzecznoœæ wszystkim nale¿y, lecz ka¿demu inna. Ju¿ nie puste, bo on je nape³ni³ myœlami."]
przykladowyTekst = "Kochajmy siê, ale tak - z osobna. Grzecznoœæ nie jest nauk¹ ³atw¹ ani ma³¹. Grzecznoœæ wszystkim nale¿y, lecz ka¿demu inna. Ju¿ nie puste, bo on je nape³ni³ myœlami."

print("\n LISTA:")
print("Iloœæ s³ów w ³añcuchu znaków:", obliczanie_ilosci_slow_przykladowyTekst(przykladowyTekst))
print("Iloœæ znaków:", obliczanie_ilosci_znakow(przykladowyTekst))
print("Iloœæ znaków (bez spacji):", obliczanie_ilosci_znakow_bez_spacji(przykladowyTekst))
print("Iloœæ znaków bia³ych:", obliczanie_ilosci_znakow_bialych(przykladowyTekst))

print("\n KOLEKCJA:")
print("Iloœæ s³ów w kolekcji:", obliczanie_ilosci_slow_kolekcja(przykladowaKolekcja))
print("Iloœæ znaków w kolekcji:", obliczanie_ilosci_znakow_kolekcja(przykladowaKolekcja))
print("Iloœæ znaków (bez spacji) w kolekcji:", obliczanie_ilosci_znakow_bez_spacji_kolekcja(przykladowaKolekcja))
print("Iloœæ znaków bia³ych w kolekcji:", obliczanie_ilosci_znakow_bialych_kolekcja(przykladowaKolekcja))

