""" File that contains the routes for the Marges blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.marges_models import (
    model_compte_de_resultat,
    sub_model_retraitement,
    model_retraitement,
    model_marges,
    model_points_morts,
    model_all_combined,
    model_marge_analysis
)
from src.services.calcul_marges import calcul_marges
from src.services.llm_analyse_marges import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

marges_ns = Namespace("Marges", description="Marges")

for model in [
    model_compte_de_resultat,
    sub_model_retraitement,
    model_retraitement,
    model_marges,
    model_points_morts,
    model_all_combined,
    model_marge_analysis
]:
    marges_ns.models[model.name] = model


@marges_ns.route("/ratios", methods=["GET"])
class HandleMargesRatios(BaseRoutesHandler):
    """Class to handle the marges ratios."""
    def process(self, numero_client):
        ratios = calcul_marges(numero_client=numero_client)
        return ratios

    @marges_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to calculate marges ratios"
        },
    )
    @marges_ns.marshal_with(model_all_combined, code=200)
    def get(self):
        """Get Marges ratios for a specific client."""
        return self.process_get()


@marges_ns.route("/analysis", methods=["GET"])
class HandleMargesAnalysis(BaseRoutesHandler):
    """Class to handle the marges analysis."""
    def process(self, numero_client):
        analysis = generate_analysis(numero_client=numero_client)
        return analysis

    @marges_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate marges analysis"
        },
    )
    @marges_ns.marshal_with(model_marge_analysis, code=200)
    def get(self):
        """Get Marges analysis for a specific client."""
        return self.process_get()