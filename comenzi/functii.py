"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json
from datetime import datetime
from pprint import pprint
from marketplace.baza_de_date.functii import citeste_datele_din_baza_de_date,scrie_datele_in_baza_de_date
from pytz import country_timezones, timezone


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """
    produs, cantitate = "", ""
    while len(produs) < 1:
        produs = input("Produs : ")
        cantitate = input("Cantitate : ")

    detalii_comanda = {produs:cantitate}
    id_comanda = genereaza_id_comanda(detalii_comanda)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    produsele_noastre = citeste_datele_din_baza_de_date()
    produsele_noastre["comenzi"][id_comanda] = {
         "id_comanda": id_comanda,
        "detalii_comanda": detalii_comanda,
        "data_inregistrare": data_inregistrare.isoformat()
    }

    scrie_datele_in_baza_de_date(produsele_noastre)


def modifica_comanda():
    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    comenzile_noastre = citeste_datele_din_baza_de_date()
    identificator = input("Introduceți identificatorul comenzii care se modifica: ")
    if identificator in comenzile_noastre["comenzi"]:
        mesaj = input("Alegeti actiunea\n'a' - adaugare produs; \n'm ' - modificare cantitate; \n's'-sterge produs, \n'e'-exit \nActiunea: ")
        if mesaj == "e":
            print("Exit")
        elif mesaj == "a":
            produs = input("Produs : ")
            cantitate = input("Cantitate : ")
            comenzile_noastre["comenzi"][identificator]["detalii_comanda"][produs] = cantitate
        elif mesaj == "m":
            produs = input("Produs : ")
            cantitate = input("Cantitate : ")
            if produs in comenzile_noastre["comenzi"][identificator]["detalii_comanda"]:
              comenzile_noastre["comenzi"][identificator]["detalii_comanda"][produs] = cantitate
            else:
              print("Acest produs nu apartine acestui identificator")
        elif mesaj == "s":
            comenzile_noastre["comenzi"].pop(identificator)
        else:
            print("Actiune invalida")
    else:
        print("Nu exista nici o comanda cu acest identificator")

    scrie_datele_in_baza_de_date(comenzile_noastre)














def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    produsele_noastre = citeste_datele_din_baza_de_date()
    comenzi = produsele_noastre["comenzi"]
    if comenzi:
        pprint(comenzi)
    else:
        print("Nu exista produse")

def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """
    produs_de_sters = input("Introduceți identificatorul comenzii de sters: \n")
    produsele_noastre = citeste_datele_din_baza_de_date()
    produsele_noastre["comenzi"].pop(produs_de_sters)
    scrie_datele_in_baza_de_date(produsele_noastre)
