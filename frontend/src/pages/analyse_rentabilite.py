""" This module contains the functions to display the profitability analysis of a company.  """

import logging
import streamlit as st
import requests
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def fetch_rentabilite_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/rentabilite/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_rentabilite_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/rentabilite/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def details_rentabilite(client_number):
    """Display details on the rentabilite analysis."""

    rentabilite_data: dict = fetch_rentabilite_client_data(client_number)

    disponibilite = rentabilite_data["data_input_rentabilite"]["disponibilité"]

    var_disponibilite = rentabilite_data["data_rentabilite"]["var_disponibilite"]

    actif_economique = rentabilite_data["data_input_rentabilite"]["Actif Economique"]
    resultat_exploitation_apre_impot_sur_ca = (
        rentabilite_data["data_rentabilite"]["resultat_exploitation_apre_impot_sur_ca"]
        * 100
    )
    var_resultat_exploitation_apre_impot_sur_ca = (
        rentabilite_data["data_rentabilite"][
            "var_resultat_exploitation_apre_impot_sur_ca"
        ]
        * 100
    )

    ca_sur_actif_economique = (
        rentabilite_data["data_rentabilite"]["ca_sur_actif_economique"] * 100
    )
    rentabilite_economique = (
        rentabilite_data["data_rentabilite"]["rentabilite_economique"] * 100
    )

    cout_dettes = rentabilite_data["data_rentabilite"]["cout_dettes"] * 100
    var_cout_dettes = rentabilite_data["data_rentabilite"]["var_cout_dettes"] * 100
    levier_financier = rentabilite_data["data_rentabilite"]["levier_financier"] * 100
    var_levier_financier = (
        rentabilite_data["data_rentabilite"]["var_levier_financier"] * 100
    )

    rentabilite_capitaux_propres = (
        rentabilite_data["data_rentabilite"]["rentabilite_capitaux_propres"] * 100
    )
    var_rentabilite_capitaux_propres = (
        rentabilite_data["data_rentabilite"]["var_rentabilite_capitaux_propres"] * 100
    )

    part_rentabilite_capitaux_propres_levier = (
        rentabilite_data["data_rentabilite"]["part_rentabilite_capitaux_propres_levier"]
        * 100
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Disponibilite (Trésorerie)",
        f"{disponibilite[1]:,.2f} K€",
        f"{var_disponibilite:,.2f} K€",
    )

    col2.metric("Actif Economique", f"{actif_economique:,.2f} K€")

    col3.metric(
        "Résultat exploitation après impôt sur CA",
        f"{resultat_exploitation_apre_impot_sur_ca:.2f} %",
        f"{var_resultat_exploitation_apre_impot_sur_ca:.2f} %",
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Coût des dettes",
        f"{cout_dettes:.2f} %",
        f"{var_cout_dettes:.2f} %",
        delta_color="inverse",
    )

    col2.metric(
        "Levier financier",
        f"{levier_financier:.2f} %",
        f"{var_levier_financier:.2f} %",
        delta_color="inverse",
    )

    col3.metric(
        "Rentabilité capitaux propres",
        f"{rentabilite_capitaux_propres:.2f} %",
        f"{var_rentabilite_capitaux_propres:.2f} %",
    )


def display_rentabilite_analysis(client_number):
    """Display the Rentabilite analysis of a company."""
    st.subheader("Synthèse des indicateurs de rentabilité")

    analysis_data: dict = fetch_rentabilite_analysis(client_number)

    buttons_keys = {
        "edit": "edit_rentabilite",
        "validate": "validate_rentabilite",
        "save": "save_rentabilite",
    }

    modes_keys = {"edit": "edit_mode_rentabilite", "validated": "validated_rentabilite"}

    text_key = "text_rentabilite"

    display_analysis(analysis_data["Synthèse"], buttons_keys, modes_keys, text_key)

    with st.expander("En savoir plus"):
        details_rentabilite(client_number)

        st.write(analysis_data["Résultat d'exploitation après impôt et Rentabilité économique"])
        st.write(analysis_data["Coût de la dette et levier financier"])
        st.write(analysis_data["Rentabilité des capitaux propres"])
        st.write(analysis_data["Risques de l'entreprise"])
