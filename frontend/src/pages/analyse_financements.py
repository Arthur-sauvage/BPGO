""" This module contains the functions to analyse the financements of a company.  """

import logging
import streamlit as st
import requests
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def fetch_financements_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/financements/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_financements_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/financements/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def details_financements(client_number):
    financement_data: dict = fetch_financements_client_data(client_number)

    actif_economique = financement_data["data_input_financement"]["Actif Economique"]

    disponibilites = financement_data["data_input_financement"]["disponibilité"]
    var_disponibilite = disponibilites[1] - disponibilites[0]

    bfr = financement_data["data_input_financement"]["Besoins en fonds de roulement"]
    var_bfr = financement_data["data_financement"]["var_bfr"]

    ratios_endettement = financement_data["data_financement"]["ratio_endettement"]

    dettes_sur_ebe = financement_data["data_financement"]["dettes_sur_ebe"]
    res_exploit_sur_frais_financiers = financement_data["data_financement"][
        "res_exploit_sur_frais_financiers"
    ]
    caf = financement_data["data_financement"]["caf"]
    var_caf = financement_data["data_financement"]["var_caf"]
    flux_treso_exploitation = financement_data["data_financement"][
        "flux_treso_exploitation"
    ]
    desendettement_net = financement_data["data_financement"]["desendettement_net"]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Actif Economique", f"{actif_economique:,.2f} K€")

    col2.metric(
        "Disponibilités", f"{disponibilites[1]:,.2f} K€", f"{var_disponibilite:,.2f} K€"
    )

    col3.metric("Ratio d'endettement", f"{ratios_endettement:.2f}")

    col4.metric("Dette / EBE", f"{dettes_sur_ebe:.2f}")

    col5.metric(
        "Résultat d'exploitation / Frais financiers",
        f"{res_exploit_sur_frais_financiers:.2f}",
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Capacité d'Autofinancement (CAF)", f"{caf:,.2f} K€", f"{var_caf:,.2f} K€"
    )

    col2.metric(
        "Besoin en fonds de roulement (BFR)",
        f"{bfr[1]:,.2f} K€",
        f"{var_bfr:,.2f} K€",
        delta_color="inverse",
    )

    col3.metric(
        "Flux de trésorerie d'exploitation", f"{flux_treso_exploitation:,.2f} K€"
    )

    col4.metric("Désendettement net", f"{desendettement_net:,.2f} K€")

    st.divider()


def display_financements_analysis(client_number):
    """Display the Financements analysis of a company."""
    st.subheader("Analyse des Financements")

    analysis_data: dict = fetch_financements_analysis(client_number)

    buttons_keys = {
        "edit": "edit_financement",
        "validate": "validate_financement",
        "save": "save_financement",
    }

    modes_keys = {"edit": "edit_mode_financement", "validated": "validated_financement"}

    text_key = "text_financement"

    display_analysis(analysis_data["Synthèse"], buttons_keys, modes_keys, text_key)

    with st.expander("En savoir plus"):
        details_financements(client_number)

        st.write(
            analysis_data["Analyse des flux de trésorerie et du désendettement net"]
        )
        st.write(analysis_data["Structure du Financement"])
        st.write(analysis_data["Analyse de l'actif économique et des disponibilités"])
