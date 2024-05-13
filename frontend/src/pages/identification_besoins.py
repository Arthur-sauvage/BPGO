import logging
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

BESOINS = """
Financement des investissements :
- Financement spécifique pour renouveler l'outil industriel usé et maintenir la compétitivité.
- Besoin de financement à long terme pour de nouvelles immobilisations pour soutenir l'expansion.

Optimisation de la Trésorerie :
- Proposition de solutions pour rémunérer la Trésorerie excédentaire.

Ventes Fuel :
- Financement pour la mise en conformité avec les réglementations environnementales.
- Solutions d'assurance pour couvrir les risques spécifiques liés au stockage et au transport de carburants, y compris les risques environnementaux et les accidents.
- Lignes de crédit flexibles pour s'adapter aux fluctuations des prix du marché des carburants.
- Produits de couverture financière pour se protéger contre la volatilité des prix du carburant.

Planification successorale et de retraite pour les propriétaires d'entreprises :
- Service de planification de la succession pour assurer une transition en douceur de la direction de l'entreprise.
- Solutions de planification de retraite pour les propriétaires pour sécuriser leur avenir financier après le retrait de l'activité.
"""


def display_identification_besoins(data_analysis):

    if "besoins" not in st.session_state:
        st.session_state.besoins = {}
        besoins = [besoin.strip() for besoin in BESOINS.split("\n")]
        for i, besoin in enumerate(besoins):
            if not besoin.startswith("-") and besoin not in ["", " ", "  "]:
                titre = besoin
                st.session_state.besoins[titre] = []
            elif besoin.startswith("-"):
                st.session_state.besoins[titre].append(
                    {"besoin": besoin, "statut": "waiting"}
                )

    if "validated_besoins" not in st.session_state:
        st.session_state.validated_besoins = {}

    tab1, tab2 = st.tabs(["Besoins par thème", "Besoins par priorité"])

    with tab1:
        st.title("")
        for titre in st.session_state.besoins:
            with st.expander(f"**{titre.replace(':', '').strip()}**", True):
                if titre in st.session_state.validated_besoins.keys():
                    for besoin in st.session_state.validated_besoins[titre]:
                        st.success(besoin.replace("-", " "))

                for i, besoin in enumerate(st.session_state.besoins[titre]):
                    my_cols = st.columns((4, 1))
                    if besoin["statut"] == "editing":
                        new_besoin = my_cols[0].text_input(
                            "Edition",
                            besoin["besoin"].replace("-", " "),
                            key=f"text_input_{titre}_{i}",
                        )
                        my_cols[1].markdown("")
                        cols = my_cols[1].columns(3)

                        if cols[1].button("✅", key=f"validate_{titre}_{i}"):
                            st.session_state.besoins[titre].pop(i)
                            if titre not in st.session_state.validated_besoins:
                                st.session_state.validated_besoins[titre] = [new_besoin]
                            else:
                                st.session_state.validated_besoins[titre].append(
                                    new_besoin
                                )
                            st.rerun()

                        if cols[2].button("❌", key=f"delete_{titre}_{i}"):
                            st.session_state.besoins[titre].pop(i)
                            st.rerun()

                    elif besoin["statut"] == "waiting":
                        my_cols[0].info(besoin["besoin"].replace("-", " "))
                        cols = my_cols[1].columns(3)

                        if cols[0].button("✏️", key=f"edit_{titre}_{i}"):
                            besoin["statut"] = "editing"
                            st.rerun()

                        if cols[1].button("✅", key=f"validate_{titre}_{i}"):
                            st.session_state.besoins[titre].pop(i)
                            if titre not in st.session_state.validated_besoins:
                                st.session_state.validated_besoins[titre] = [
                                    besoin["besoin"]
                                ]
                            else:
                                st.session_state.validated_besoins[titre].append(
                                    besoin["besoin"]
                                )
                            st.rerun()

                        if cols[2].button("❌", key=f"delete_{titre}_{i}"):
                            st.session_state.besoins[titre].pop(i)
                            st.rerun()

    with tab2:
        st.title("")
        haute_importance = ["Ventes Fuel :"]
        moyenne_importance = [
            "Optimisation de la Trésorerie :",
            "Financement des investissements :",
        ]
        faible_importance = list(
            set(
                list(st.session_state.validated_besoins.keys())
                + list(st.session_state.besoins.keys())
            ).symmetric_difference(set(haute_importance + moyenne_importance))
        )
        importances = {
            "🟥 **Importance Haute**": haute_importance,
            "🟧 **Importance Moyenne**": moyenne_importance,
            "🟨 **Importance Faible**": faible_importance,
        }

        for importance, titres in importances.items():
            with st.expander(importance, True):
                for titre in titres:

                    if titre in st.session_state.validated_besoins.keys():
                        for besoin in st.session_state.validated_besoins[titre]:
                            st.success(besoin.replace("-", " "))

                    for i, besoin in enumerate(st.session_state.besoins[titre]):
                        my_cols = st.columns((4, 1))
                        if besoin["statut"] == "editing":
                            new_besoin = my_cols[0].text_input(
                                "Edition",
                                besoin["besoin"].replace("-", " "),
                                key=f"text_input_{importance}_{titre}_{besoin}_{i}",
                            )
                            my_cols[1].markdown("")
                            cols = my_cols[1].columns(3)

                            if cols[1].button(
                                "✅", key=f"validate_{titre}_{i}_importance_{besoin}"
                            ):
                                st.session_state.besoins[titre].pop(i)
                                if titre not in st.session_state.validated_besoins:
                                    st.session_state.validated_besoins[titre] = [
                                        new_besoin
                                    ]
                                else:
                                    st.session_state.validated_besoins[titre].append(
                                        new_besoin
                                    )
                                st.rerun()

                            if cols[2].button(
                                "❌", key=f"delete_{titre}_{i}_importance_{besoin}"
                            ):
                                st.session_state.besoins[titre].pop(i)
                                st.rerun()

                        elif besoin["statut"] == "waiting":
                            my_cols[0].info(besoin["besoin"].replace("-", " "))
                            cols = my_cols[1].columns(3)

                            if cols[0].button(
                                "✏️", key=f"edit_{titre}_{i}_importance_{besoin}"
                            ):
                                besoin["statut"] = "editing"
                                st.rerun()

                            if cols[1].button(
                                "✅", key=f"validate_{titre}_{i}_importance_{besoin}"
                            ):
                                st.session_state.besoins[titre].pop(i)
                                if titre not in st.session_state.validated_besoins:
                                    st.session_state.validated_besoins[titre] = [
                                        besoin["besoin"]
                                    ]
                                else:
                                    st.session_state.validated_besoins[titre].append(
                                        besoin["besoin"]
                                    )
                                st.rerun()

                            if cols[2].button(
                                "❌", key=f"delete_{titre}_{i}_importance_{besoin}"
                            ):
                                st.session_state.besoins[titre].pop(i)
                                st.rerun()

    if st.button("Etape suivante", key="next_step_besoins"):
        st.session_state["validated_section_besoins"] = True
        st.success("Besoins validés avec succès")
        st.rerun()
