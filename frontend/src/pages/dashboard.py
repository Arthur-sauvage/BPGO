""" Dashboard for financial data analysis """

import logging
import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.components.points_forts_faibles import display_financial_radar
from src.components.Thermometer import Thermometer
from src.components.kpi import KPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)



def fetch_metric_client_data(client_number, metric):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/metric/",
        params={"numero_client": client_number, "metric": metric},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_marges_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/marges/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def generate_data():
    """Generates synthetic data for customer and sector averages."""
    # Creating example data
    metrics = [
        "Sales",
        "EBITDA",
        "Personnel Costs",
        "Added Value",
        "Current Income",
        "Average Headcount",
    ]
    customer_data = np.random.normal(loc=100, scale=20, size=len(metrics))
    sector_avg = np.random.normal(loc=80, scale=10, size=len(metrics))

    df = pd.DataFrame(
        {"Metric": metrics, "Customer": customer_data, "Sector Average": sector_avg}
    )

    return df


def plot_comparison_bars(data):
    """Creates bar graphs comparing each indicator."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Setting the width and positions for bar groups
    bar_width = 0.35
    x = np.arange(len(data))

    # Creating bars for customer and sector average
    ax.bar(x - bar_width / 2, data["Customer"], width=bar_width, label="Customer")
    ax.bar(
        x + bar_width / 2,
        data["Sector Average"],
        width=bar_width,
        label="Sector Average",
    )

    ax.set_xticks(x)
    ax.set_xticklabels(data["Metric"])
    ax.legend()
    ax.set_title("Customer vs Sector Averages")

    return fig


def plot_ratios(data):
    """Creates a plot showing ratios as a percentage of sales."""
    # Assuming the first metric is 'Sales' for ratio calculation
    sales_value = data.loc[data["Metric"] == "Sales", "Customer"].values[0]

    # Calculating ratios as percentages
    data["Customer Ratio"] = (data["Customer"] / sales_value) * 100

    fig, ax = plt.subplots(figsize=(10, 6))

    # Creating bar chart for ratios
    bar_width = 0.35
    x = np.arange(len(data))

    ax.bar(x, data["Customer Ratio"], width=bar_width, label="Customer Ratio (%)")

    ax.set_xticks(x)
    ax.set_xticklabels(data["Metric"])
    ax.legend()
    ax.set_title("Customer Ratios as Percentage of Sales")

    return fig


def display_dashboard(client_number: int, top_kpis: dict[str, KPI]):
    """Display the dashboard for the financial data analysis"""
    try:
        revenue = fetch_metric_client_data(client_number=client_number, metric="Chiffre d'affaire net total FL")["metric"]
        result_net = fetch_metric_client_data(client_number=client_number, metric="Mt. résultat de l'exercice DI")["metric"]
        effectif = fetch_metric_client_data(client_number=client_number, metric="Effectif moyen du personnel YP")["metric"]
        
        ebe_on_ca = fetch_marges_client_data(client_number)["Marges"]["EBE sur CA"][1] * 100
    except Exception as error:
        logging.error(f"Error fetching data: {error}")
        revenue = 2656
        result_net = 46
        effectif = 7
        ebe_on_ca = 3.01

    with st.expander("", True):
        st.write("### Synthèse Financière")
        st.info(st.session_state["financial_analysis"])

    with st.expander("", True):
        st.write("### KPIs")
        st.title("")
        col1, col2, col3 = st.columns(3)
        col1.metric(
            "Chiffre d'Affaire",
            f"{revenue:,.0f} K€",
        )
        col2.metric(
            "Résultat Net",
            f"{result_net:,.0f} K€",
        )
        col3.metric(
            "Effectif",
            f"{effectif:,.0f}",
        )

        st.title("")
        if client_number == 2:
            benchmark_ebe = 13.6
        elif client_number == 3:
            benchmark_ebe = 25.7
        elif client_number == 4:
            benchmark_ebe = 10.3
        elif client_number == 10:
            benchmark_ebe = 6.6
        else:
            benchmark_ebe = 6.6

        title_scale_ebe = """
        <div style="text-align: center;">
            <h3>EBE sur CA</h3>
        </div>
        """
        st.markdown(title_scale_ebe, unsafe_allow_html=True)
        thermometer = Thermometer(client_value=ebe_on_ca, benchmark_value=benchmark_ebe)
        thermometer.display()


        st.title("")
        st.divider()
        # list_kpis = list(top_kpis.values())
        # col1, col2 = st.columns(2)
        # with col1:
        #     list_kpis[0].display()
        # with col2:
        #     list_kpis[1].display()

        # data = generate_data()

        # # Display bar graph comparing indicators
        # st.subheader("Indicators Comparison")
        # fig1 = plot_comparison_bars(data)
        # st.pyplot(fig1)

        # # Display ratios as percentages
        # st.subheader("Ratios as Percentage of Sales")
        # fig2 = plot_ratios(data)
        # st.pyplot(fig2)

        display_financial_radar()
