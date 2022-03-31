import json

from marketplace.baza_de_date import calea_catre_baza_de_date


def citeste_datele_din_baza_de_date():
    with open(calea_catre_baza_de_date(), "r") as baza_de_date:
        return json.load(baza_de_date)


def scrie_datele_in_baza_de_date(date):
    with open(calea_catre_baza_de_date(), "w") as baza_de_date:
        json.dump(date, baza_de_date)
