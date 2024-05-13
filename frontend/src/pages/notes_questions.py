import logging
import streamlit as st
from src.utils.edit_validate import display_analysis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

NOTES = """
### Points à Eclaircir
Évaluer l'impact de la fluctuation des prix des matières premières : Noter les tendances actuelles du marché des carburants et les répercussions sur les marges du client.

Comprendre la gestion des stocks : Examiner comment le client gère les niveaux de stock pour éviter les surstocks ou ruptures, surtout lors des fluctuations de demande.

Analyse des ventes : Discuter des volumes de vente pour chaque type de carburant et des tendances observées sur les différents segments.

Infrastructure de stockage et logistique : Évaluer la capacité de stockage et les besoins logistiques du client pour s'assurer que l'infrastructure actuelle supporte efficacement les opérations.
"""

QUESTIONS = """
### Questions à Poser
Fluctuation des Prix :
- Comment gérez-vous l'impact des fluctuations des prix du carburant sur votre marge opérationnelle ?
- Avez-vous des mécanismes de couverture ou des assurances contre les fluctuations soudaines des prix du carburant ?

Gestion des Stocks :
- Quelles méthodes utilisez-vous pour optimiser vos niveaux de stock de carburants ?
- Avez-vous rencontré des défis logistiques ou de stockage qui ont affecté votre capacité à répondre à la demande du marché ?

Crédit Client et Paiements :
- Quelle est votre politique de crédit pour les acheteurs de carburants ? Offrez-vous des termes de crédit étendus ?
- Comment gérez-vous les retards de paiement et quel impact cela a-t-il sur votre trésorerie ?

Sécurité et Conformité :
- Pouvez-vous me parler des mesures de sécurité et de conformité que vous avez mises en place pour le stockage et le transport des carburants ?
- Avez-vous eu des audits ou inspections récents ? Quels en ont été les résultats ?

Investissements et Expansion :
- Envisagez-vous d'investir dans de nouvelles capacités de stockage ou dans des technologies améliorées pour l'efficacité opérationnelle ?
- Y a-t-il des projets d'expansion que vous souhaitez entreprendre qui nécessiteraient un soutien financier ?

Durabilité et Écologie :
- Avec l'augmentation de la réglementation sur l'environnement, quelles initiatives prenez-vous pour réduire l'impact écologique de vos activités ?
- Comment envisagez-vous la transition vers des sources d'énergie plus propres ou alternatives dans votre business model ?
"""


def display_notes_questions(data_analysis):
    # with st.expander("", True):
    #     st.info(NOTES)
    #     st.divider()
    #     st.info(QUESTIONS)

    buttons_keys = {
        "edit": "edit_questions",
        "validate": "validate_questions",
        "save": "save_questions",
    }

    modes_keys = {"edit": "edit_mode_questions", "validated": "validated_notes"}

    text_key = "text_questions"

    display_analysis(
        f"{NOTES}\n\n{QUESTIONS}",
        buttons_keys,
        modes_keys,
        text_key,
        name="Notes",
    )

    # if st.button("Valider les notes"):
    #     st.session_state["validated_notes"] = True
    #     st.success("Notes validés avec succès")
    #     st.rerun()
