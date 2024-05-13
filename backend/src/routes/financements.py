""" File that contains the routes for the Financements blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.financement_models import (
    model_input_financement,
    model_output_financement,
    model_global,
    model_financement_analysis,
)
from src.services.calcul_financements import calcul_financements
from src.services.llm_analyse_financement import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

financements_ns = Namespace("Financements", description="Financements")

for model in [
    model_input_financement,
    model_output_financement,
    model_global,
    model_financement_analysis,
]:
    financements_ns.models[model.name] = model


@financements_ns.route("/ratios", methods=["GET"])
class HandleFinancementsRatios(BaseRoutesHandler):
    """Class to handle the Financements ratios."""

    def process(self, numero_client):
        ratios =  calcul_financements(numero_client=numero_client)
        logging.info("Ratios calculated successfully : %s", ratios)
        return ratios

    @financements_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to calculate Financements ratios"
        },
    )
    @financements_ns.marshal_with(model_global, code=200)
    def get(self):
        """Get Financements ratios for a specific client."""
        return self.process_get()


@financements_ns.route("/analysis", methods=["GET"])
class HandleFinancementsAnalysis(BaseRoutesHandler):
    """Class to handle the Financements analysis."""
    def process(self, numero_client):
        analysis = generate_analysis(numero_client=numero_client)
        logging.info("Financements analysis generated successfully : %s", analysis)
        return analysis

    @financements_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate Financements analysis"
        },
    )
    @financements_ns.marshal_with(model_financement_analysis, code=200)
    def get(self):
        """Get Financements analysis for a specific client."""
        return self.process_get()
