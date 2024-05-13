""" File that contains the routes for the BFR blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.bfr_models import (
    model_actif_circulant,
    model_bfr_ratios,
    model_bfr,
    model_bfr_analysis
)
from src.services.calcul_bfr import calcul_bfr
from src.services.llm_analyse_bfr import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

bfr_ns = Namespace("BFR", description="BFR")

for model in [
    model_actif_circulant,
    model_bfr_ratios,
    model_bfr,
    model_bfr_analysis
]:
    bfr_ns.models[model.name] = model

@bfr_ns.route("/ratios")
class HandleBFRRatios(BaseRoutesHandler):
    def process(self, numero_client):
        return calcul_bfr(numero_client=numero_client)
    
    @bfr_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={"numero_client": "Client number for which to calculate BFR ratios"}
    )
    @bfr_ns.marshal_with(model_bfr, code=200)
    def get(self):
        """ Get BFR ratios for a specific client. """
        return self.process_get()


@bfr_ns.route("/analysis", methods=["GET"])
class HandleBFRAnalysis(BaseRoutesHandler):
    """Class to handle the BFR analysis."""
    def process(self, numero_client):
        return generate_analysis(numero_client=numero_client)

    @bfr_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate BFR analysis"
        },
    )
    @bfr_ns.marshal_with(model_bfr_analysis, code=200)
    def get(self):
        """Get BFR analysis for a specific client."""
        return self.process_get()