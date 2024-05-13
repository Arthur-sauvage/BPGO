import logging
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

def get_clients_data():
    # This function should interact with your data source to fetch client information
    # For demonstration, here's some dummy data:
    return [
        {"id": 2, "name": "Chez Daniel", "next_meeting": "2024-06-01"},
        {"id": 3, "name": "Pineau Rénovation", "next_meeting": "2024-05-26"},
        {"id": 4, "name": "La Maison du Pain", "next_meeting": "2024-05-19"},
        {"id": 10, "name": "DéménageFacile Express", "next_meeting": "2024-05-18"},
    ]

def preprocess_clients_data():
    clients = get_clients_data()
    # Sort the clients based on the date of the next meeting
    clients_sorted = sorted(clients, key=lambda x: x["next_meeting"])
    return clients_sorted

def display_client_selection():
    st.title("Prochains RDV clients")
    
    clients = preprocess_clients_data()
    
    # Format client information for the dropdown
    client_options = [f"{client['name']} (Prochain RDV: {client['next_meeting']})" for client in clients]
    
    # Provide a dropdown to select a client
    logging.info("Displaying client selection dropdown.")
    selected_option = st.selectbox(
        label="Sélectionnez un client",
        options=client_options,
        index=0,  # Default to the first entry (earliest meeting date)
    )
    
    selected_client_id = [client['id'] for client in clients if f"{client['name']} (Prochain RDV: {client['next_meeting']})" == selected_option][0]
    
    if st.button("Analyser"):
        logging.info("Selected client ID: %s", selected_client_id)
        st.session_state["selected_client_id"] = selected_client_id
        st.rerun()

def display_change_client():

    clients = preprocess_clients_data()
    
    # Format client information for the dropdown
    client_options = [f"{client['name']} (Prochain RDV: {client['next_meeting']})" for client in clients]
    
    # Provide a dropdown to select a client
    selected_option = st.sidebar.selectbox(
        label="Changer de client",
        options=client_options,
        index=0,  # Default to the first entry (earliest meeting date)
    )
    
    selected_client_id = [client['id'] for client in clients if f"{client['name']} (Prochain RDV: {client['next_meeting']})" == selected_option][0]
    
    if st.sidebar.columns(2)[1].button("Changer"):
        logging.info("Change selected client ID: %s", selected_client_id)
        st.session_state["selected_client_id"] = selected_client_id
        st.rerun()

