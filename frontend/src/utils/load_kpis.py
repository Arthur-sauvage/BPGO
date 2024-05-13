""" This module is responsible for loading all KPIs from the backend. """

from typing import Dict
import requests
from src.components.kpi import KPI


def fetch_tresorerie_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/tresorerie/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def fetch_structure_financement_client_data(client_number):
    """Fetches data for a given client number from the Flask API."""
    response = requests.get(
        "http://localhost:8001/structure_financement/ratios",
        params={"numero_client": client_number},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()

    return {"error": response.json().get("error", "Unknown error")}


def load_kpis(client_number: int) -> Dict[str, KPI]:
    """Loads all KPIs for a given client."""
    all_kpis: Dict[str, KPI] = {}

    # tresorerie_data: dict = fetch_tresorerie_client_data(client_number)

    # fond_de_roulement = tresorerie_data["fond de roulement"]["value"]
    # all_kpis["fond de roulement"] = KPI(
    #     name="fond de roulement",
    #     type_graph="metric",
    #     value=fond_de_roulement,
    #     good_above=True,
    # )

    # structure_financement_data: dict = fetch_structure_financement_client_data(client_number)

    # ratio_endettement = structure_financement_data["Ratio d'endettement"]["value"]

    benchmark_endettement = 1.5
    benchmark_solvabilite = 0.5
    if client_number in [2, 3]:  # Opticien & bijouterie
        benchmark_endettement = 2
    if client_number in [4, 10]:  # Traiteur
        benchmark_endettement = 1.5

    # all_kpis["Ratio d'Endettement"] = KPI(
    #     name="Ratio d'Endettement",
    #     type_graph="hist",
    #     value=ratio_endettement,
    #     benchmark=benchmark_endettement,
    #     good_above=False,
    # )

    # ratio_solvabilite = structure_financement_data["Ratio de solvabilité"]["value"]
    # all_kpis["Ratio de Solvabilité"] = KPI(
    #     name="Ratio de Solvabilité",
    #     type_graph="hist",
    #     value=ratio_solvabilite,
    #     benchmark=benchmark_solvabilite,
    #     good_above=True,
    # )

    return all_kpis
