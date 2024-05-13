"""
Ce script génère un graphique radar pour comparer la performance financière d'une entreprise
avec la moyenne du secteur.
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def plot_radar_chart(data_company, data_sector, attributes, title):
    color_company = "#299ADC"
    color_sector = "#1E70AA"

    """Plot a radar chart comparing the financial performance of a company with the sector average."""
    # Nombre de variables que nous montrons sur le graphique radar
    num_vars = len(attributes)

    # Calcule les angles de chaque axe sur le radar
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Le graphique radar est un cercle, donc il doit être fermé
    data_company += data_company[:1]
    data_sector += data_sector[:1]
    angles += angles[:1]

    fig, axis = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    axis.fill(angles, data_company, color=color_company, alpha=0.25)
    axis.plot(angles, data_company, color=color_company, label="Client")  # Ligne pour l'entreprise
    axis.fill(angles, data_sector, color=color_sector, alpha=0.25)
    axis.plot(angles, data_sector, color=color_sector, label="Secteur")  # Ligne pour le secteur

    # Améliorations esthétiques
    axis.set_theta_offset(np.pi / 2)
    axis.set_theta_direction(-1)

    # Dessiner un axe par attribut avec des labels
    plt.xticks(angles[:-1], attributes)
    axis.yaxis.grid(True)  # Ajoute des grilles sur les valeurs y

    with st.columns(3)[1]:
        plt.title(title, size=15, color="black", y=1.1)
        plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1))
        st.pyplot(fig)


def display_financial_radar():
    """Display a radar chart comparing financial performance."""
    # Exemple de données pour l'entreprise et le secteur
    attributes = ["Liquidity", "Solvency", "Profitability", "Efficiency", "Growth"]
    company_data = [0.75, 0.60, 0.80, 0.70, 0.85]
    sector_data = [0.70, 0.65, 0.75, 0.65, 0.80]


    plot_radar_chart(company_data, sector_data, attributes, "Comparaison des performances financières")

    # Commentaire sur les points forts et faibles basé sur l'analyse
    st.title("")
    st.columns(3)[1].markdown("**Points forts et points faibles**")
    my_cols_points = st.columns(2)
    my_cols_points[0].success("La comparaison montre que l'entreprise surpasse le secteur en termes de croissance et de rentabilité")
    my_cols_points[1].error("Mais elle reste derrière en termes de solvabilité")
