""" Module to display the completeness analysis of the data. """

import streamlit as st
import requests
import pyperclip
import pandas as pd
import os
from src.utils.edit_validate import toggle_edit_mode, validate_text


def fetch_generation_mails(client_number):
    """Fetches the analysis for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/mails/demandes",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


@st.experimental_dialog("Mail à envoyer")
def handle_generation_click():
    mail: dict = fetch_generation_mails(10)
    subject = mail["Subject"]
    body = mail["Body"]
    mail_text = f"{subject}\n\n{body}"
    st.write(mail_text)

    if st.button("Copier"):
        pyperclip.copy(mail_text)
        st.rerun()


def display_completeness_analysis(data_completeness):
    """Display the completeness analysis of the data."""
    # Calculate completeness score
    total_elements = len(data_completeness)
    missing_elements = sum(1 for value in data_completeness.values() if value is None)
    completeness_score = (1 - missing_elements / total_elements) * 100

    good = "✅"
    wrong = "❌"

    # Create a list to store modified completeness status
    modified_completeness = []

    if "added_documents" not in st.session_state:
        st.session_state["added_documents"] = {}

    data_completeness.update(st.session_state["added_documents"])
    for k, v in data_completeness.items():
        if v is None:
            data_completeness[k] = wrong
        else:
            data_completeness[k] = good

    if completeness_score > 75:
        comment = "Les données sont largement complètes, l'analyse financière est considérée comme fiable"
    elif completeness_score > 50:
        comment = "Des données importantes manquent, ce qui pourrait affecter la précision de l'analyse"
    else:
        comment = "Beaucoup d'informations essentielles sont manquantes, l'analyse n'est pas fiable"

    with st.expander("", True):
        # st.info(comment)
        st.title("")
        cols = st.columns(2)
        cols[0].markdown("Date de la dernière actualisation : **12/03/2024**")
        cols[0].dataframe(
            pd.DataFrame(data_completeness.items(), columns=["Document", "Présent ?"]),
            hide_index=True,
        )


        cols[1].title("")
        with cols[1].form("my-form", clear_on_submit=True):
            new_doc = st.file_uploader("Ajouter un document")
            submitted = st.form_submit_button("Valider")

        if submitted and new_doc is not None:
            st.session_state["added_documents"][os.path.splitext(new_doc.name)[0]] = os.path.splitext(new_doc.name)[0]
            st.rerun()

        cols[1].title("")
        if cols[1].button("Générer un mail de demande"):
            handle_generation_click()

    st.title("")
    if st.button("Passer à l'analyse financière"):
        st.session_state["validated_completude"] = True