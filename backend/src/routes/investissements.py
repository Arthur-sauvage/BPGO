""" File that contains the routes for the Investissements blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.investissements_models import (
    model_immobilisations,
    model_ratios_investissements,
    model_investissements,
    model_investissements_analysis
)
from src.services.calcul_investissements import calcul_investsments
from src.services.calcul_bfr import calcul_bfr
from src.services.llm_analyse_investissements import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

investissements_ns = Namespace("Investissements", description="Investissements")

for model in [
    model_immobilisations,
    model_ratios_investissements,
    model_investissements,
    model_investissements_analysis
]:
    investissements_ns.models[model.name] = model


@investissements_ns.route("/ratios")
class HandleInvestissementsRatios(BaseRoutesHandler):
    def process(self, numero_client):
        return calcul_investsments(numero_client=numero_client)
    
    @investissements_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={"numero_client": "Client number for which to calculate Investissements ratios"}
    )
    @investissements_ns.marshal_with(model_investissements, code=200)
    def get(self):
        """ Get Investissements ratios for a specific client. """
        return self.process_get()


@investissements_ns.route("/analysis", methods=["GET"])
class HandleInvestissementsAnalysis(BaseRoutesHandler):
    """Class to handle the Investissements analysis."""
    def process(self, numero_client):
        return generate_analysis(numero_client=numero_client)

    @investissements_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate Investissements analysis"
        },
    )
    @investissements_ns.marshal_with(model_investissements_analysis, code=200)
    def get(self):
        """Get Investissements analysis for a specific client."""
        return self.process_get()