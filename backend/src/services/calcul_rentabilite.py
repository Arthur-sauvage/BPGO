""" Calcul the rentabilite ratios """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def calcul_rentabilite(numero_client: int):
    if numero_client == 10:

        data_input_rentabilite = {
            "Chiffre d'affaires": [2463.0, 2656.0],
            "resultat_exploitation": [45.0, 44.089],
            "taux imposition": 0.20,
            "Actif Economique": -266.698,
            "Charges financieres": [1.0, 3.116],
            "Endettement net": [183.446, 204.812],
            "Capitaux Propres": [560.216, 555.885],
            "Résultat net": [32.0, 24.0],
            "Résultat exceptionnel": [0.0, -8.0],
            "disponibilité": [1056.185, 1029.624],
        }
        

        var_disponibilite = (
            data_input_rentabilite["disponibilité"][1]
            - data_input_rentabilite["disponibilité"][0]
        )

        resultat_exploitation_apre_impot_sur_ca = (
            data_input_rentabilite["resultat_exploitation"][1]
            / data_input_rentabilite["Chiffre d'affaires"][1]
        ) / (1 - data_input_rentabilite["taux imposition"])

        resultat_exploitation_apre_impot_sur_ca_0 = (
            data_input_rentabilite["resultat_exploitation"][0]
            / data_input_rentabilite["Chiffre d'affaires"][0]
        ) / (1 - data_input_rentabilite["taux imposition"])

        var_resultat_exploitation_apre_impot_sur_ca = (
            resultat_exploitation_apre_impot_sur_ca
            - resultat_exploitation_apre_impot_sur_ca_0
        )

        ca_sur_actif_economique = (
            data_input_rentabilite["Chiffre d'affaires"][1]
            / data_input_rentabilite["Actif Economique"]
        )

        rentabilite_economique = (
            resultat_exploitation_apre_impot_sur_ca * ca_sur_actif_economique
        )

        cout_dettes = (
            data_input_rentabilite["Charges financieres"][1]
            / data_input_rentabilite["Endettement net"][1]
        ) * (1 - data_input_rentabilite["taux imposition"])

        cout_dettes_0 = (
            data_input_rentabilite["Charges financieres"][0]
            / data_input_rentabilite["Endettement net"][0]
        ) * (1 - data_input_rentabilite["taux imposition"])

        var_cout_dettes = cout_dettes - cout_dettes_0

        levier_financier = (
            data_input_rentabilite["Endettement net"][1]
            / data_input_rentabilite["Capitaux Propres"][1]
        )

        levier_financier_0 = (
            data_input_rentabilite["Endettement net"][0]
            / data_input_rentabilite["Capitaux Propres"][0]
        )

        var_levier_financier = levier_financier - levier_financier_0

        rentabilite_capitaux_propres = (
            data_input_rentabilite["Résultat net"][1]
            - data_input_rentabilite["Résultat exceptionnel"][1]
        ) / data_input_rentabilite["Capitaux Propres"][1]

        rentabilite_capitaux_propres_0 = (
            data_input_rentabilite["Résultat net"][0]
            - data_input_rentabilite["Résultat exceptionnel"][0]
        ) / data_input_rentabilite["Capitaux Propres"][0]

        var_rentabilite_capitaux_propres = (
            rentabilite_capitaux_propres - rentabilite_capitaux_propres_0
        )

        part_rentabilite_capitaux_propres_levier = (
            rentabilite_capitaux_propres - rentabilite_economique
        ) / rentabilite_capitaux_propres

        data_rentabilite = {
            "var_disponibilite": var_disponibilite,
            "resultat_exploitation_apre_impot_sur_ca": resultat_exploitation_apre_impot_sur_ca,
            "var_resultat_exploitation_apre_impot_sur_ca": var_resultat_exploitation_apre_impot_sur_ca,
            "ca_sur_actif_economique": ca_sur_actif_economique,
            "rentabilite_economique": rentabilite_economique,
            "cout_dettes": cout_dettes,
            "var_cout_dettes": var_cout_dettes,
            "levier_financier": levier_financier,
            "var_levier_financier": var_levier_financier,
            "rentabilite_capitaux_propres": rentabilite_capitaux_propres,
            "var_rentabilite_capitaux_propres": var_rentabilite_capitaux_propres,
            "part_rentabilite_capitaux_propres_levier": part_rentabilite_capitaux_propres_levier,
        }

    return {
        "data_input_rentabilite": data_input_rentabilite,
        "data_rentabilite": data_rentabilite,
    }
