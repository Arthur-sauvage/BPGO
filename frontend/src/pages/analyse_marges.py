""" This module contains the code for the Marges Analysis page. """

import logging
import streamlit as st
import requests
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def fetch_marges_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/marges/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_marge_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/marges/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_specific_metric(client_number, metric):
    """Fetches a specific metric for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/metric/",
        params={"numero_client": client_number, "metric": metric},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def details_marges(client_number):
    marge_data: dict = fetch_marges_client_data(client_number)

    ca = marge_data["Compte de résultat"]["Chiffre d'affaires"][1]
    croissance_ca = marge_data["Retraitement"]["Chiffre d'affaires"]["croissance"] * 100

    consommations_sur_ca = marge_data["Marges"]["Consommations"][1]

    croissance_consommation = (
        (consommations_sur_ca / marge_data["Marges"]["Consommations"][0]) - 1
    ) * 100
    consommations_sur_ca *= 100

    valeur_ajoutee = marge_data["Marges"]["Valeur ajoutée"][1]
    croissance_valeur_ajoutee = (
        (valeur_ajoutee / marge_data["Marges"]["Valeur ajoutée"][0]) - 1
    ) * 100
    valeur_ajoutee *= 100

    charges_personnels_sur_ca = marge_data["Marges"]["Charges de personnel sur CA"][1]
    croissance_charges_personnels = (
        (
            charges_personnels_sur_ca
            / marge_data["Marges"]["Charges de personnel sur CA"][0]
        )
        - 1
    ) * 100
    charges_personnels_sur_ca *= 100

    dot_amortissement = marge_data["Marges"]["Dotations aux amortissements sur CA"][1]
    croissance_dot_amortissement = (
        (
            dot_amortissement
            / marge_data["Marges"]["Dotations aux amortissements sur CA"][0]
        )
        - 1
    ) * 100
    dot_amortissement *= 100

    ebe_sur_ca = marge_data["Marges"]["EBE sur CA"][1]
    croisssance_ebe = ((ebe_sur_ca / marge_data["Marges"]["EBE sur CA"][0]) - 1) * 100
    ebe_sur_ca *= 100

    resultat_exploitation = marge_data["Marges"]["Résultat d'exploitation sur CA"][1]
    croissance_resultat_exploitation = (
        (
            resultat_exploitation
            / marge_data["Marges"]["Résultat d'exploitation sur CA"][0]
        )
        - 1
    ) * 100
    resultat_exploitation *= 100

    resultat_net = marge_data["Marges"]["Résultat net sur CA"][1]
    croissance_resultat_net = (
        (resultat_net / marge_data["Marges"]["Résultat net sur CA"][0]) - 1
    ) * 100
    resultat_net *= 100

    point_mort = marge_data["Points Morts"]["CA sur Points morts totaux"][1]
    croissance_point_mort = (
        (point_mort / marge_data["Points Morts"]["CA sur Points morts totaux"][0]) - 1
    ) * 100
    point_mort *= 100

    try:
        effectif = fetch_specific_metric(
            client_number=client_number, metric="Effectif moyen du personnel YP"
        )["metric"]
    except Exception as error:
        logging.error(f"Error fetching data: {error}")
        effectif = 7
    charges_personnel = marge_data["Compte de résultat"]["Charges de personnel"][1]

    salaire_moyen = charges_personnel / effectif

    st.title("")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric(
        "Chiffre d'Affaires",
        f"{ca:,.0f} K€",
        f"{croissance_ca:.2f}%",
    )

    col2.metric(
        "Consommation / CA",
        f"{consommations_sur_ca:,.2f} %",
        f"{croissance_consommation:.2f}%",
        delta_color="inverse",
    )

    col3.metric(
        "Valeur ajoutée / CA",
        f"{valeur_ajoutee:,.2f} %",
        f"{croissance_valeur_ajoutee:.2f}%",
    )

    col4.metric(
        "Charges de personnel / CA",
        f"{charges_personnels_sur_ca:,.2f} %",
        f"{croissance_charges_personnels:.2f}%",
        delta_color="inverse",
    )

    col5.metric(
        "EBE / CA",
        f"{ebe_sur_ca:,.2f} %",
        f"{croisssance_ebe:.2f}%",
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Dotations aux amortissements / CA",
        f"{dot_amortissement:,.2f} %",
        f"{croissance_dot_amortissement:.2f}%",
        delta_color="inverse",
    )

    col2.metric(
        "Résultat d'exploitation / CA",
        f"{resultat_exploitation:,.2f} %",
        f"{croissance_resultat_exploitation:.2f}%",
    )

    col3.metric(
        "Résultat net / CA",
        f"{resultat_net:,.2f} %",
        f"{croissance_resultat_net:.2f}%",
    )

    col4.metric(
        "CA / Point mort",
        f"{point_mort:,.2f} %",
        f"{croissance_point_mort:.2f}%",
    )

    col5.metric(
        "Salaire moyen",
        f"{salaire_moyen:,.2f} K€",
    )
    st.divider()


def display_marges_analysis(client_number):
    st.subheader("Compte de Résultat")

    analysis_data: dict = fetch_marge_analysis(client_number)

    buttons_keys = {
        "edit": "edit_marges",
        "validate": "validate_marges",
        "save": "save_marges"
    }

    modes_keys = {
        "edit": "edit_mode_marges",
        "validated": "validated_marges"
    }

    text_key = "text_marges"

    display_analysis(analysis_data["Synthèse"], buttons_keys, modes_keys, text_key)

    with st.expander("En savoir plus"):
        details_marges(client_number)

        st.write(analysis_data["Chiffre d'affaire"])
        st.write(analysis_data["Valeur ajoutée"])
        st.write(analysis_data["Charges de Personnel"])
        st.write(analysis_data["Point mort"])
        st.write(analysis_data["Resultat d'exploitation"])
        st.write(analysis_data["Résultat Net"])
