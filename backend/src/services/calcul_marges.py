""" Calcul the marge ratios """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def calcul_marges(numero_client: int):
    if numero_client == 10:
        data_compte_de_resultat = {
            "Chiffre d'affaires": [2463.0, 2656.0],
            "Production stockée": [0.0, 0.0],
            "Produits d'exploitation": [2478.0, 2677.0],
            "Achats de marchandises et de matières premières": [1582.0, 1743.0],
            "Variation de stocks": [-15.0, -20.0],
            "Autres charges externes": [235.0, 266.0],
            "Impôts et taxes": [8.0, 8.0],
            "Charges de personnel": [569.0, 579.0],
            "Dotations aux amortissements": [40.0, 36.0],
            "Dotations aux provisions": [0.0, 0.0],
            "Charges d'exploitation": [2419.0, 2611.0],
            "Résultat d'exploitation": [60.0, 66.0],
            "Produits financiers": [0.0, 0.0],
            "Charges financières": [2.0, 3.0],
            "Résultat financier": [-1.0, -3.0],
            "Résultat exceptionnel": [0.0, -8.0],
            "Impôts sur les sociétés": [11.0, 9.0],
            "Résultat net": [47.0, 46.0],
        }

        croissance_ca: float = (
            data_compte_de_resultat["Chiffre d'affaires"][1]
            / data_compte_de_resultat["Chiffre d'affaires"][0]
        ) - 1

        consommations: list = [
            float(achats + var_stock - prod_stock)
            for achats, var_stock, prod_stock in zip(
                data_compte_de_resultat[
                    "Achats de marchandises et de matières premières"
                ],
                data_compte_de_resultat["Variation de stocks"],
                data_compte_de_resultat["Production stockée"],
            )
        ]
        croissance_consommations: float = (consommations[1] / consommations[0]) - 1

        marge_brutes: list = [
            float(ca - consommation)
            for ca, consommation in zip(
                data_compte_de_resultat["Chiffre d'affaires"], consommations
            )
        ]
        croissance_marge_brute: float = (marge_brutes[1] / marge_brutes[0]) - 1

        ebe: list = [
            float(
                marge_brute
                - autre_charge_externe
                - impot
                - charges_personnel
                - dotations_prov
            )
            for (
                marge_brute,
                autre_charge_externe,
                impot,
                charges_personnel,
                dotations_prov,
            ) in zip(
                marge_brutes,
                data_compte_de_resultat["Autres charges externes"],
                data_compte_de_resultat["Impôts et taxes"],
                data_compte_de_resultat["Charges de personnel"],
                data_compte_de_resultat["Dotations aux provisions"],
            )
        ]
        croissance_ebe: float = (ebe[1] / ebe[0]) - 1

        resultat_exploitation: list = [
            float(ebe_anne - dot_ammo)
            for ebe_anne, dot_ammo in zip(
                ebe, data_compte_de_resultat["Dotations aux amortissements"]
            )
        ]
        croissance_resultat_exploitation: float = (
            resultat_exploitation[1] / resultat_exploitation[0]
        ) - 1

        charges_financieres_nettes: list = [
            float(charge_fin - produit_fin)
            for charge_fin, produit_fin in zip(
                data_compte_de_resultat["Charges financières"],
                data_compte_de_resultat["Produits financiers"],
            )
        ]
        croissance_charges_financieres_nettes: float = (
            charges_financieres_nettes[1] / charges_financieres_nettes[0]
        ) - 1

        resultat_net: list = [
            float(
                resultat_exploitation - charge_fin_nette + resultat_exceptionnel - impot
            )
            for resultat_exploitation, charge_fin_nette, resultat_exceptionnel, impot in zip(
                resultat_exploitation,
                charges_financieres_nettes,
                data_compte_de_resultat["Résultat exceptionnel"],
                data_compte_de_resultat["Impôts sur les sociétés"],
            )
        ]
        croissance_resultat_net: float = (resultat_net[1] / resultat_net[0]) - 1

        data_retraitement = {
            "Chiffre d'affaires": {
                "valeurs": data_compte_de_resultat["Chiffre d'affaires"],
                "croissance": croissance_ca,
            },
            "Consommations": {
                "valeurs": consommations,
                "croissance": croissance_consommations,
            },
            "Marge brute": {
                "valeurs": marge_brutes,
                "croissance": croissance_marge_brute,
            },
            "EBE": {"valeurs": ebe, "croissance": croissance_ebe},
            "Résultat d'exploitation": {
                "valeurs": resultat_exploitation,
                "croissance": croissance_resultat_exploitation,
            },
            "Charges financières nettes": {
                "valeurs": charges_financieres_nettes,
                "croissance": croissance_charges_financieres_nettes,
            },
            "Résultat net": {
                "valeurs": resultat_net,
                "croissance": croissance_resultat_net,
            },
        }

        marge_consommations: list = [
            float(consommation / ca)
            for consommation, ca in zip(
                consommations, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]

        valeur_ajoutee: list = [
            float(marge_brute / ca)
            for marge_brute, ca in zip(
                marge_brutes, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]
        autres_charges_externe_sur_ca: list = [
            float(autre_charge_externe / ca)
            for autre_charge_externe, ca in zip(
                data_compte_de_resultat["Autres charges externes"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        impots_sur_ca: list = [
            float(impot / ca)
            for impot, ca in zip(
                data_compte_de_resultat["Impôts et taxes"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        charges_personnel_sur_ca: list = [
            float(charge_personnel / ca)
            for charge_personnel, ca in zip(
                data_compte_de_resultat["Charges de personnel"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        dotations_prov_sur_ca: list = [
            float(dot_prov / ca)
            for dot_prov, ca in zip(
                data_compte_de_resultat["Dotations aux provisions"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        ebe_sur_ca: list = [
            float(ebe / ca)
            for ebe, ca in zip(ebe, data_compte_de_resultat["Chiffre d'affaires"])
        ]
        dotation_ammo_sur_ca: list = [
            float(dot_ammo / ca)
            for dot_ammo, ca in zip(
                data_compte_de_resultat["Dotations aux amortissements"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        resultat_exploitation_sur_ca: list = [
            float(resultat_exploitation / ca)
            for resultat_exploitation, ca in zip(
                resultat_exploitation, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]
        charges_financieres_sur_ca: list = [
            float(charge_fin / ca)
            for charge_fin, ca in zip(
                data_compte_de_resultat["Charges financières"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        resultat_exceptionnel_sur_ca: list = [
            float(resultat_exceptionnel / ca)
            for resultat_exceptionnel, ca in zip(
                data_compte_de_resultat["Résultat exceptionnel"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        impots_societe_sur_ca: list = [
            float(impot / ca)
            for impot, ca in zip(
                data_compte_de_resultat["Impôts sur les sociétés"],
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]
        resultat_net_sur_ca: list = [
            float(resultat_net / ca)
            for resultat_net, ca in zip(
                resultat_net, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]

        marges = {
            "Consommations": marge_consommations,
            "Valeur ajoutée": valeur_ajoutee,
            "Autres charges externes sur CA": autres_charges_externe_sur_ca,
            "Impôts sur CA": impots_sur_ca,
            "Charges de personnel sur CA": charges_personnel_sur_ca,
            "Dotations aux provisions sur CA": dotations_prov_sur_ca,
            "EBE sur CA": ebe_sur_ca,
            "Dotations aux amortissements sur CA": dotation_ammo_sur_ca,
            "Résultat d'exploitation sur CA": resultat_exploitation_sur_ca,
            "Charges financières sur CA": charges_financieres_sur_ca,
            "Résultat exceptionnel sur CA": resultat_exceptionnel_sur_ca,
            "Impôts sur les sociétés sur CA": impots_societe_sur_ca,
            "Résultat net sur CA": resultat_net_sur_ca,
        }

        frais_variables: list = [
            float(consommation + (autre_charge_externe / 2))
            for consommation, autre_charge_externe in zip(
                consommations, data_compte_de_resultat["Autres charges externes"]
            )
        ]

        frais_fixes: list = [
            float(charge_personnel + dot_ammo + taxes + (autre_charge_externe / 2))
            for (charge_personnel, dot_ammo, taxes, autre_charge_externe) in zip(
                data_compte_de_resultat["Charges de personnel"],
                data_compte_de_resultat["Dotations aux amortissements"],
                data_compte_de_resultat["Impôts et taxes"],
                data_compte_de_resultat["Autres charges externes"],
            )
        ]

        logging.info("Frais %s %s", frais_variables, frais_fixes)

        points_morts_operationnel: list = [
            frais_fixes_annee / (1 - frais_variables_annee / ca)
            for frais_fixes_annee, frais_variables_annee, ca in zip(
                frais_fixes,
                frais_variables,
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]

        ca_sur_points_morts_operationnel: list = [
            ca / point_mort
            for point_mort, ca in zip(
                points_morts_operationnel, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]

        points_morts_totaux: list = [
            (frais_fixes_annee + frais_financier) / (1 - frais_variables_annee / ca)
            for (frais_fixes_annee, frais_financier, frais_variables_annee, ca) in zip(
                frais_fixes,
                charges_financieres_nettes,
                frais_variables,
                data_compte_de_resultat["Chiffre d'affaires"],
            )
        ]

        ca_sur_points_morts_totaux: list = [
            ca / point_mort
            for point_mort, ca in zip(
                points_morts_totaux, data_compte_de_resultat["Chiffre d'affaires"]
            )
        ]

        points_morts = {
            "Points morts opérationnel": points_morts_operationnel,
            "CA sur Points morts opérationnel": ca_sur_points_morts_operationnel,
            "Points morts totaux": points_morts_totaux,
            "CA sur Points morts totaux": ca_sur_points_morts_totaux,
        }

        return {
            "Compte de résultat": data_compte_de_resultat,
            "Retraitement": data_retraitement,
            "Marges": marges,
            "Points Morts": points_morts,
        }

    return None, None, None
