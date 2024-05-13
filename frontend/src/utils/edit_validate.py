import streamlit as st
import uuid


def toggle_edit_mode(modes_keys):
    st.session_state[modes_keys["edit"]] = not st.session_state[modes_keys["edit"]]
    st.rerun()

def validate_text(modes_keys):
    st.session_state[modes_keys["validated"]] = True
    st.rerun()

def display_analysis(analysis: str, buttons_keys, modes_keys, text_key, name: str = "Analyse"):

    # Initialize session state
    if modes_keys["edit"] not in st.session_state:
        st.session_state[modes_keys["edit"]] = False
    if modes_keys["validated"] not in st.session_state:
        st.session_state[modes_keys["validated"]] = False
    if text_key not in st.session_state:
        st.session_state[text_key] = analysis

    with st.expander(name, True):
        # Display the editable text or the text_area depending on the edit_mode
        if st.session_state[modes_keys["edit"]]:
            st.session_state[text_key] = st.text_area(
                "Editez le texte:", value=st.session_state[text_key], height=150
            )
            if st.button("Enregistrer", key=buttons_keys["save"]):
                toggle_edit_mode(modes_keys)
        elif st.session_state[modes_keys["validated"]]:
            st.success(st.session_state[text_key])
        else:
            st.info(st.session_state[text_key])
            edit_button, validate_button = st.columns([1, 3])
            if edit_button.button("Modifier", key=buttons_keys["edit"]):
                toggle_edit_mode(modes_keys)
            if validate_button.button("Valider", key=buttons_keys["validate"]):
                validate_text(modes_keys)