from comenzi.functii import listeaza_toate_comenzile, adauga_o_comanda, sterge_o_comanda, modifica_comanda
from produse.functii import adauga_un_produs, listeaza_toate_produsele, sterge_produs
from utilizatori.functii import listeaza_toti_utilizatorii, adauga_un_utilizator, sterge_un_utilizator

if __name__ == '__main__':
    def mesaj_de_iesire():
        print("O zi frumoasa in continuare")

    maparea_comenzilor_la_functii = {
        "adauga_utilizator": adauga_un_utilizator,
        "listeaza_utilizatori": listeaza_toti_utilizatorii,
        "sterge_utilizator": sterge_un_utilizator,
        "adauga_comanda": adauga_o_comanda,
        "listeaza_comenzi": listeaza_toate_comenzile,
        "sterge_comanda": sterge_o_comanda,
        "modifica_comanda": modifica_comanda,
        "adauga_produs": adauga_un_produs,
        "sterge_produs": sterge_produs,
        "listeaza_produse": listeaza_toate_produsele,
        "exit": mesaj_de_iesire
    }
    actiune = None
    while actiune != "exit":
        actiune = input("Introdu o comanda:\n")
        functia_de_executie = maparea_comenzilor_la_functii.get(actiune)
        if functia_de_executie is None:
            print("Actiune Invalida")
            print(f"Actiuni Valide: {','.join(maparea_comenzilor_la_functii.keys())}")
        else:
            functia_de_executie()
