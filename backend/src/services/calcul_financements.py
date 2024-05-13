""" Calcul the financements ratios """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def calcul_financements(numero_client: int):
    if numero_client == 10:
        data_input_financement = {
            "Capitaux Propres": 555.885,
            "Endettement net": 204.812,
            "EBE": [85.0, 80.0],
            "Résultat d'exploitation": 44.089,
            "Frais financiers": [1.0, 3.116],
            "Actif Economique": -266.698,
            "Actif immobilisé net": [165.0, 152.0],
            "Besoins en fonds de roulement": [-474.0, -419.0],
            "Dotations aux amortissements": [40.0, 36.0],
            "Impots sur les sociétés": [11.0, 9.0],
            "Dividendes": [0.0, 50.0],
            "disponibilité": [1056.185, 1029.624],
        }

        ratio_endettement = (
            data_input_financement["Endettement net"]
            / data_input_financement["Capitaux Propres"]
        )

        dettes_sur_ebe = (
            data_input_financement["Endettement net"] / data_input_financement["EBE"][1]
        )

        res_exploit_sur_frais_financiers = (
            data_input_financement["Résultat d'exploitation"]
            / data_input_financement["Frais financiers"][1]
        )

        caf = (
            data_input_financement["EBE"][1]
            - data_input_financement["Frais financiers"][1]
            - data_input_financement["Impots sur les sociétés"][1]
        )

        caf_0 = (
            data_input_financement["EBE"][0]
            - data_input_financement["Frais financiers"][0]
            - data_input_financement["Impots sur les sociétés"][0]
        )

        var_caf = caf - caf_0

        var_bfr = (
            data_input_financement["Besoins en fonds de roulement"][1]
            - data_input_financement["Besoins en fonds de roulement"][0]
        )
        flux_treso_exploitation = caf - var_bfr

        flux_investissements = (
            data_input_financement["Actif immobilisé net"][1]
            - data_input_financement["Actif immobilisé net"][0]
            + data_input_financement["Dotations aux amortissements"][1]
        )

        desendettement_net = flux_treso_exploitation - flux_investissements

        data_financement = {
            "ratio_endettement": ratio_endettement,
            "dettes_sur_ebe": dettes_sur_ebe,
            "res_exploit_sur_frais_financiers": res_exploit_sur_frais_financiers,
            "caf": caf,
            "var_caf": var_caf,
            "var_bfr": var_bfr,
            "flux_treso_exploitation": flux_treso_exploitation,
            "flux_investissements": flux_investissements,
            "desendettement_net": desendettement_net,
        }

    return {
        "data_input_financement": data_input_financement,
        "data_financement": data_financement,
    }
