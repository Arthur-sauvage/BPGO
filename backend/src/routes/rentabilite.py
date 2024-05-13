""" File that contains the routes for the Rentabilite blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.rentabilite_models import (
    model_input_rentabilite,
    model_rentabilite,
    model_global,
    model_rentabilite_analysis,
)
from src.services.calcul_rentabilite import calcul_rentabilite
from src.services.llm_analyse_rentabilite import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

rentabilite_ns = Namespace("Rentabilite", description="Rentabilite")

for model in [
    model_input_rentabilite,
    model_rentabilite,
    model_global,
    model_rentabilite_analysis,
]:
    rentabilite_ns.models[model.name] = model


@rentabilite_ns.route("/ratios", methods=["GET"])
class HandleRentabiliteRatios(BaseRoutesHandler):
    """Class to handle the Rentabilite ratios."""

    def process(self, numero_client):
        return calcul_rentabilite(numero_client=numero_client)

    @rentabilite_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to calculate Rentabilite ratios"
        },
    )
    @rentabilite_ns.marshal_with(model_global, code=200)
    def get(self):
        """Get Rentabilite ratios for a specific client."""
        return self.process_get()


@rentabilite_ns.route("/analysis", methods=["GET"])
class HandleRentabiliteAnalysis(BaseRoutesHandler):
    """Class to handle the Rentabilite analysis."""

    def process(self, numero_client):
        return generate_analysis(numero_client=numero_client)

    @rentabilite_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate Rentabilite analysis"
        },
    )
    @rentabilite_ns.marshal_with(model_rentabilite_analysis, code=200)
    def get(self):
        """Get Rentabilite analysis for a specific client."""
        return self.process_get()
