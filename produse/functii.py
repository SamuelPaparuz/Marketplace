"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import hashlib
import json
from datetime import datetime
from pprint import pprint
from marketplace.baza_de_date.functii import citeste_datele_din_baza_de_date,scrie_datele_in_baza_de_date
from pytz import country_timezones, timezone


def genereaza_id_produs(nume_produs, pret):
    hash_object = hashlib.md5(bytes(nume_produs + pret, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    '''
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    '''
    nume_produs , pret = "", ""
    while len(nume_produs) < 1 or len(nume_produs) > 50:
        nume_produs = input("Introduceti numele produsului de adaugat : \n")
        if len(nume_produs) < 1 or len(nume_produs) > 50:
            print("Nume invalid ! Trebuie sa ai intre 1 si 50 caractere")
    while len(pret) < 1:
        pret = input("Introduceti pretului produsului adaugat : \n")

    id_produs = genereaza_id_produs(nume_produs,pret)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    produsele_noastre = citeste_datele_din_baza_de_date()
    produsele_noastre["produse"][id_produs] = {
        "nume_produs": nume_produs,
        "pret":  pret,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(produsele_noastre)



def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    produsele_noastre = citeste_datele_din_baza_de_date()
    produse = produsele_noastre["produse"]
    if produse:
        pprint(produse)
    else:
        print("Nu aveti produse")


def sterge_produs():
    produs_de_sters = input("Ce produs vrei sa stergi ? : \n")
    produsele_noastre = citeste_datele_din_baza_de_date()
    produsele_noastre["produse"].pop(produs_de_sters)
    scrie_datele_in_baza_de_date(produsele_noastre)
