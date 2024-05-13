""" This module contains the functions to analyse the BFR of a company.  """

import logging
import streamlit as st
import requests
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def fetch_bfr_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/bfr/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_bfr_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/bfr/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def details_bfr(client_number):
    investment_data: dict = fetch_bfr_client_data(client_number)

    rotation_credit_client = investment_data["bfr_ratios"]["rotation_credit_client"]
    rotation_credit_fournisseur = investment_data["bfr_ratios"][
        "rotation_credit_fournisseur"
    ]
    rotation_stock = investment_data["bfr_ratios"]["rotation_stock"]
    rotation_bfr = investment_data["bfr_ratios"]["rotation_bfr"]
    rotation_var_bfr = investment_data["bfr_ratios"]["rotation_var_bfr"]

    disponibilites = investment_data["data_actif_circulant"]["Disponibilités"]

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric(
        "Rotation crédit client (en j de CA)", f"{rotation_credit_client:,.0f} j"
    )

    col2.metric(
        "Rotation crédit fournisseur (en j d'achats)",
        f"{rotation_credit_fournisseur:,.0f} j",
    )

    col3.metric("Rotation stock (en j de CA)", f"{rotation_stock:,.0f} j")

    col4.metric(
        "Rotation BFR (en j de CA)",
        f"{rotation_bfr:,.0f} j",
        f"{rotation_var_bfr:.2f} j",
        delta_color="inverse",
    )

    col5.metric("Disponibilités", f"{disponibilites:,.2f} K€")

    st.divider()


def display_bfr_analysis(client_number):
    """Display the BFR analysis of a company."""
    st.subheader("Analyse du Besoin en Fonds de Roulement")

    analysis_data: dict = fetch_bfr_analysis(client_number)

    buttons_keys = {
        "edit": "edit_bfr",
        "validate": "validate_bfr",
        "save": "save_bfr",
    }

    modes_keys = {"edit": "edit_mode_bfr", "validated": "validated_bfr"}

    text_key = "text_bfr"

    display_analysis(
        analysis_data["Synthèse et points d'attentions"],
        buttons_keys,
        modes_keys,
        text_key,
    )

    with st.expander("En savoir plus"):
        details_bfr(client_number)

        st.write(analysis_data["Analyse du Besoin en Fonds de Roulement (BFR)"])
