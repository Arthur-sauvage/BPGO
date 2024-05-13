""" Main Streamlit app for the financial dashboard. """

import logging
import streamlit as st
from src.pages.client_selection import display_client_selection, display_change_client
from src.pages.connaissances_client import display_completeness_analysis
from src.pages.financial_analysis import display_financial_analysis
from src.pages.identification_besoins import display_identification_besoins
from src.pages.propositions_produits import display_propositions_produits
from src.pages.notes_questions import display_notes_questions
from src.pages.dashboard import display_dashboard
from src.pages.simulations import display_simulation
from src.utils.documents import documents_Equinox
from src.utils.load_kpis import load_kpis
from src.components.kpi import KPI
from src.components.table_of_content import ToC

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

st.set_page_config(layout="wide")


def initialize_session_state():
    """Initialize session state variables."""
    if "selected_client_id" not in st.session_state:
        st.session_state["selected_client_id"] = None
        logging.info("Selected client not found in session state.")

    if "client_data" not in st.session_state:
        st.session_state["client_data"] = None
    if "validated_completude" not in st.session_state:
        st.session_state["validated_completude"] = False
    if "validated_synthesis" not in st.session_state:
        st.session_state["validated_synthesis"] = False
    if "validated_section_besoins" not in st.session_state:
        st.session_state["validated_section_besoins"] = False
    if "validated_products" not in st.session_state:
        st.session_state["validated_products"] = False
    if "validated_notes" not in st.session_state:
        st.session_state["validated_notes"] = False


def update_client():
    """Function to refresh client data."""
    st.session_state["client_data"] = "New data"


def test():
    st.info(st.session_state["selected_client_id"])


def process_completude(toc, data_elements):
    st.title("")
    toc.title("Actualisation de la Connaissance Client")

    display_completeness_analysis(data_elements)


def process_financial_analysis(toc, numero_client):
    if st.session_state["validated_completude"]:
        st.title("")
        toc.title("Analyse Financière")

        display_financial_analysis(numero_client)


def process_identification_besoins(toc):
    if st.session_state["validated_synthesis"]:
        st.title("")
        toc.title("Identification des Besoins")
        display_identification_besoins("")


def process_propositions_produits(toc):
    if st.session_state["validated_section_besoins"]:
        st.title("")
        toc.title("Propositions de Produits BPGO")
        display_propositions_produits("")


def process_simulation(toc):
    if st.session_state["validated_products"]:
        st.title("")
        toc.title("Simulation (Work in Progress)")
        display_simulation()


def process_notes_questions(toc):
    if st.session_state["validated_products"]:
        st.title("")
        toc.title("Points à Eclaircir & Questions")
        display_notes_questions("")


def process_dashboard(toc, numero_client, all_kpis):
    if st.session_state["validated_notes"]:
        st.title("")
        toc.title("Récapitulatif")
        display_dashboard(numero_client, all_kpis)


def main():
    """Main Streamlit app for the financial dashboard."""

    cols = st.columns(5)
    cols[1].image("frontend/src/assets/BANQUE_POPULAIRE_GO_LOGO.png")
    cols[3].columns(2)[1].image("frontend/src/assets/logo_niji.png")

    centered_text = """
    <div style="text-align: center;">
        <h1 style="color:#299ADC">Appui Pro x Niji</h1>
    </div>
    """
    st.markdown(centered_text, unsafe_allow_html=True)

    st.markdown(
        """<div style="text-align: center;"><h7 style="color:black">Prototype pour démo du 15/05/24</h7></div>""",
        unsafe_allow_html=True,
    )

    initialize_session_state()

    if st.session_state["selected_client_id"] is None:
        display_client_selection()

    else:
        logging.info("Selected client is in the session_state.")

        all_kpis: dict[str, KPI] = load_kpis(st.session_state["selected_client_id"])

        # Load or generate data
        data_elements = documents_Equinox()

        toc = ToC(numero_client=st.session_state["selected_client_id"])

        process_completude(toc, data_elements)

        process_financial_analysis(toc, st.session_state["selected_client_id"])

        process_identification_besoins(toc)

        process_propositions_produits(toc)

        # st.title("")
        # toc.title("Simulation (Work in Progress)")
        # display_simulation()

        process_notes_questions(toc)

        process_dashboard(toc, st.session_state["selected_client_id"], all_kpis)

        toc.generate()

        st.sidebar.divider()

        display_change_client()


if __name__ == "__main__":
    main()
