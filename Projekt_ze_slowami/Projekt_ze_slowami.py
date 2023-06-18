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



# Sprawd�my
przykladowaKolekcja = ["Kochajmy si�, ale tak - z osobna. Grzeczno�� nie jest nauk� �atw� ani ma��. Grzeczno�� wszystkim nale�y, lecz ka�demu inna. Ju� nie puste, bo on je nape�ni� my�lami."]
przykladowyTekst = "Kochajmy si�, ale tak - z osobna. Grzeczno�� nie jest nauk� �atw� ani ma��. Grzeczno�� wszystkim nale�y, lecz ka�demu inna. Ju� nie puste, bo on je nape�ni� my�lami."

print("\n LISTA:")
print("Ilo�� s��w w �a�cuchu znak�w:", obliczanie_ilosci_slow_przykladowyTekst(przykladowyTekst))
print("Ilo�� znak�w:", obliczanie_ilosci_znakow(przykladowyTekst))
print("Ilo�� znak�w (bez spacji):", obliczanie_ilosci_znakow_bez_spacji(przykladowyTekst))
print("Ilo�� znak�w bia�ych:", obliczanie_ilosci_znakow_bialych(przykladowyTekst))

print("\n KOLEKCJA:")
print("Ilo�� s��w w kolekcji:", obliczanie_ilosci_slow_kolekcja(przykladowaKolekcja))
print("Ilo�� znak�w w kolekcji:", obliczanie_ilosci_znakow_kolekcja(przykladowaKolekcja))
print("Ilo�� znak�w (bez spacji) w kolekcji:", obliczanie_ilosci_znakow_bez_spacji_kolekcja(przykladowaKolekcja))
print("Ilo�� znak�w bia�ych w kolekcji:", obliczanie_ilosci_znakow_bialych_kolekcja(przykladowaKolekcja))

