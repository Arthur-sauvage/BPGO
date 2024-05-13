""" Calcul the BFR ratios"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

def calcul_bfr(numero_client: int):
    if numero_client == 10:
        data_actif_circulant = {
            "Encours Clients": 249.921,
            "Encours Fournisseurs": 315.749,
            "CA": 2656.0,
            "Achats": 1743.0,
            "stocks": 42.323,
            "bfr": -418.506,
            "variation bfr": 55.706,
            "Disponibilités": 1018.13,
        }

        rotation_credit_client = (data_actif_circulant["Encours Clients"] / data_actif_circulant["CA"]) * 365
        rotation_credit_fournisseur = (data_actif_circulant["Encours Fournisseurs"] / data_actif_circulant["Achats"]) * 365
        rotation_stock = (data_actif_circulant["stocks"] / data_actif_circulant["CA"]) * 365
        rotation_bfr = (data_actif_circulant["bfr"] / data_actif_circulant["CA"]) * 365
        rotation_var_bfr = (data_actif_circulant["variation bfr"] / data_actif_circulant["CA"]) * 365

        bfr_ratios =  {
            "rotation_credit_client": rotation_credit_client,
            "rotation_credit_fournisseur": rotation_credit_fournisseur,
            "rotation_stock": rotation_stock,
            "rotation_bfr": rotation_bfr,
            "rotation_var_bfr": rotation_var_bfr,
        }

        return {
            "data_actif_circulant": data_actif_circulant,
            "bfr_ratios": bfr_ratios,
        }