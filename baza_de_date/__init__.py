import os
from pathlib import Path


def calea_catre_baza_de_date():
    calea_catre_fisierul_de_baze_de_date = Path(
        os.path.dirname(os.path.abspath(__file__)),
        "marketplace.json"
    )
    return calea_catre_fisierul_de_baze_de_date
