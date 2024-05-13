""" File that contains the routes for the Financial Synthesis blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.synthese_financiere_models import model_synthese_analysis
from src.services.llm_synthese_financiere import generate_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

synthesis_ns = Namespace("Financial_Synthesis", description="Financial_Synthesis")

for model in [model_synthese_analysis]:
    synthesis_ns.models[model.name] = model


@synthesis_ns.route("/analysis", methods=["GET"])
class HandleFinancialSynthesisAnalysis(BaseRoutesHandler):
    """Class to handle the Financial Synthesis analysis."""

    def process(self, numero_client):
        return generate_analysis(numero_client=numero_client)

    @synthesis_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to generate Financial Synthesis analysis"
        },
    )
    @synthesis_ns.marshal_with(model_synthese_analysis, code=200)
    def get(self):
        """Get Financial Synthesis analysis for a specific client."""
        return self.process_get()
