""" This module contains the functions to analyse the investments of a company.  """

import logging
import streamlit as st
import requests
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def fetch_investment_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/investissements/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_investment_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/investissements/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def details_investment(client_number):
    investment_data: dict = fetch_investment_client_data(client_number)

    immobilisations_nettes = investment_data["data_immobilisations"][
        "Immobilisations nettes"
    ]
    variation_immobilisations_nettes = investment_data["data_immobilisations"][
        "Variation immobilisations nettes"
    ]
    dotations_amortissement = investment_data["data_immobilisations"][
        "Dotations amortissement"
    ]
    investissements = investment_data["data_immobilisations"]["Investissements"]
    actif_economique = investment_data["investissements"]["actif_economique"]
    degre_usure = investment_data["investissements"]["degre_usure"]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Actif Economique", f"{actif_economique:,.2f} K€")

    col2.metric(
        "Immobilisations nettes",
        f"{immobilisations_nettes:,.2f} K€",
        f"{variation_immobilisations_nettes:.2f} K€",
    )

    col3.metric("Dotations amortissement", f"{dotations_amortissement:,.2f} K€")

    col4.metric("Investissements", f"{investissements:,.2f} K€")

    col5.metric("Degré d'usure", f"{degre_usure:,.2f} %")

    st.divider()


def display_investment_analysis(client_number):
    """Display the Investment analysis of a company."""
    st.subheader("Analyse des Investissements")

    analysis_data: dict = fetch_investment_analysis(client_number)

    buttons_keys = {
        "edit": "edit_investissements",
        "validate": "validate_investissements",
        "save": "save_investissements",
    }

    modes_keys = {
        "edit": "edit_mode_investissements",
        "validated": "validated_investissements",
    }

    text_key = "text_investissements"

    display_analysis(
        analysis_data["Synthèse et points d'attentions"],
        buttons_keys,
        modes_keys,
        text_key,
    )

    with st.expander("En savoir plus"):
        details_investment(client_number)

        st.write(analysis_data["Analyse de la politique d'investissements"])
