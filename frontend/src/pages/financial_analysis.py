import streamlit as st
import requests
from src.pages.analyse_marges import display_marges_analysis
from src.pages.analyse_bfr import display_bfr_analysis
from src.pages.analyse_investissement import display_investment_analysis
from src.pages.analyse_financements import display_financements_analysis
from src.pages.analyse_rentabilite import display_rentabilite_analysis
from src.utils.edit_validate import display_analysis


def fetch_synthesis_analysis(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/synthese/analysis",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def display_financial_analysis(numero_client: int):
    if not (
        "validated_marges" in st.session_state
        and st.session_state["validated_marges"]
        and "validated_bfr" in st.session_state
        and st.session_state["validated_bfr"]
        and "validated_investissements" in st.session_state
        and st.session_state["validated_investissements"]
        and "validated_financement" in st.session_state
        and st.session_state["validated_financement"]
        and "validated_rentabilite" in st.session_state
        and st.session_state["validated_rentabilite"]
    ):
        tab1_name = "Compte de Résultat"
        tab2_name = "BFR"
        tab3_name = "Investissements"
        tab4_name = "Structure de Financement"
        tab5_name = "Rentabilité"

        if (
            "validated_marges" in st.session_state
            and st.session_state["validated_marges"]
        ):
            tab1_name = "Compte de Résultat ✅"
        if "validated_bfr" in st.session_state and st.session_state["validated_bfr"]:
            tab2_name = "BFR ✅"
        if (
            "validated_investissements" in st.session_state
            and st.session_state["validated_investissements"]
        ):
            tab3_name = "Investissements ✅"
        if (
            "validated_financement" in st.session_state
            and st.session_state["validated_financement"]
        ):
            tab4_name = "Structure de Financement ✅"
        if (
            "validated_rentabilite" in st.session_state
            and st.session_state["validated_rentabilite"]
        ):
            tab5_name = "Rentabilité ✅"

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [tab1_name, tab2_name, tab3_name, tab4_name, tab5_name]
        )

        with tab1:
            display_marges_analysis(numero_client)

        with tab2:
            display_bfr_analysis(numero_client)

        with tab3:
            display_investment_analysis(numero_client)

        with tab4:
            display_financements_analysis(numero_client)

        with tab5:
            display_rentabilite_analysis(numero_client)

    else:
        tab1_name = "Compte de Résultat ✅"
        tab2_name = "BFR ✅"
        tab3_name = "Investissements ✅"
        tab4_name = "Structure de Financement ✅"
        tab5_name = "Rentabilité ✅"
        tab6_name = "Synthèse Financière 🔄"

        if (
            "validated_synthesis" in st.session_state
            and st.session_state["validated_synthesis"]
        ):
            tab6_name = "Synthèse Financière ✅"

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [tab1_name, tab2_name, tab3_name, tab4_name, tab5_name, tab6_name]
        )

        with tab1:
            display_marges_analysis(numero_client)

        with tab2:
            display_bfr_analysis(numero_client)

        with tab3:
            display_investment_analysis(numero_client)

        with tab4:
            display_financements_analysis(numero_client)

        with tab5:
            display_rentabilite_analysis(numero_client)

        with tab6:
            analysis_data: dict = fetch_synthesis_analysis(numero_client)

            buttons_keys = {
                "edit": "edit_synthesis",
                "validate": "validate_synthesis",
                "save": "save_synthesis",
            }

            modes_keys = {
                "edit": "edit_mode_synthesis",
                "validated": "validated_synthesis",
            }

            text_key = "text_synthesis"

            vue_ensemble = analysis_data["Vue Ensemble"]
            synthese = analysis_data["Synthèse"]

            st.session_state["financial_analysis"] = f"{vue_ensemble}\n{synthese}"

            st.subheader("Synthèse financière")
            display_analysis(
                f"{vue_ensemble}\n{synthese}",
                buttons_keys,
                modes_keys,
                text_key,
                name="Analyse",
            )
