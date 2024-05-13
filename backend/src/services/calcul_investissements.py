""" Calcul the Investements ratios """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

def calcul_investsments(numero_client: int):
    if numero_client == 10:
        data_immobilisations = {
            "Immobilisations nettes": 151.808,
            "Variation immobilisations nettes": -13.0,
            "Immobilisations brutes": 668.313,
            "Dotations amortissement": 36.122,
            "Investissements": 21.49,
            "Disponibilités": 1018.13,
            "Capital": 555.885,
            "Dettes financières": 204.812,
        }

        actif_economique = data_immobilisations["Capital"] + data_immobilisations["Dettes financières"] - data_immobilisations["Disponibilités"]
        
        degre_usure = (1 - (data_immobilisations["Immobilisations nettes"] / data_immobilisations["Immobilisations brutes"])) * 100

        taux_amortissement = (data_immobilisations["Dotations amortissement"] / data_immobilisations["Immobilisations nettes"]) * 100

        investissements = {
            "actif_economique": actif_economique,
            "degre_usure": degre_usure,
            "taux_amortissement": taux_amortissement,
        }

        return {
            "data_immobilisations": data_immobilisations,
            "investissements": investissements,
        }