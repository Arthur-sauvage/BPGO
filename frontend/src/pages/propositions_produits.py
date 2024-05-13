import logging
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


PRODUITS = """
Affacturage :
- Flash Factures : Solution de financement à la Facture 100% digitale.

Changement de Devises :
- Change Dynamique sur TPE : Solution de change de devises.

Développement durable :
- Prêt Mobilité Verte : Prêt pour l'achat de véhicules propres et/ou les bornes de rechargement.
- Prêt Rénovation Energétique : Prêt d'équipement MLT permettant de financer des travaux de rénovation énergétique.
"""




def display_propositions_produits(data_analysis):
    if "produits" not in st.session_state:
        st.session_state.produits = {
                    "Ventes Fuel :": [["Financement pour la mise en conformité avec les réglementations environnementales.", "Prêt Mobilité Verte : Prêt pour l'achat de véhicules propres et/ou les bornes de rechargement."]],
                    "Financement des investissements :": [["Financement spécifique pour renouveler l'outil industriel usé et maintenir la compétitivité.", "Prêt Relais Equipement Pro : Solution de crédit à court terme pour financer un projet Professionnel."], ["Besoin de financement à long terme pour de nouvelles immobilisations pour soutenir l'expansion.", "CREDIT BAIL MOBILIER : Opération de location d’un bien mobilier à usage professionnel"]],
                    "Optimisation de la Trésorerie :": [["Proposition de solutions pour rémunérer la Trésorerie excédentaire.", "Livret Optiplus Tréso : Destiné à rémunérer la trésorerie professionnelle excédentaire des professionnels."]],
                    "Planification successorale et de retraite pour les propriétaires d'entreprises :": [["Service de planification de la succession pour assurer une transition en douceur de la direction de l'entreprise.", "Garanties de Passif : Engagement par signature de la Banque, dans le cadre d’une cession d’entreprise"]],
                    }


    if "validated_produits" not in st.session_state:
        st.session_state.validated_produits = {}


    for titre in st.session_state.validated_besoins.keys():
        with st.expander(f"**{titre.replace(':', '').strip()}**", True):
            if titre in st.session_state.validated_produits.keys():
                for besoin, produit in st.session_state.validated_produits[titre]:
                    if f"- {besoin}" in st.session_state.validated_besoins[titre]:
                        my_cols = st.columns(2)
                        my_cols[0].success(besoin.replace("-", " "))
                        my_cols[1].success(produit)
            if titre in st.session_state.produits.keys():
                for besoin, produit in st.session_state.produits[titre]:
                    if f"- {besoin}" in st.session_state.validated_besoins[titre]:
                        my_cols = st.columns((3, 3, 1))
                        my_cols[0].success(besoin.replace("-", " "))
                        my_cols[1].info(produit)
                        if my_cols[2].button("🛒", key=f"add_{titre}_{produit}"):
                            if titre not in st.session_state.validated_produits:
                                st.session_state.validated_produits[titre] = [[besoin, produit]]
                            else:
                                st.session_state.validated_produits[titre].append([besoin, produit])
                            st.session_state.produits[titre].remove([besoin, produit])
                            st.rerun()
            else:
                st.write(st.session_state.produits.keys())



    if st.button("Etape suivante", key="next_step_produits"):
        st.session_state["validated_products"] = True
        st.success("Produits validés avec succès")
        st.rerun()