""" File that contains the routes for the mails blueprint """

import logging
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.mails_models import model_mail
from src.services.llm_mails_demande import generate_mail

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

mails_ns = Namespace("Mails", description="Mails")

for model in [model_mail]:
    mails_ns.models[model.name] = model


@mails_ns.route("/demandes", methods=["GET"])
class HandleMailsGeneration(BaseRoutesHandler):
    """Class to handle the Mails mail."""
    def process(self, numero_client):
        return generate_mail(numero_client=numero_client)

    @mails_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={"numero_client": "Client number for which to generate Mails mail"},
    )
    @mails_ns.marshal_with(model_mail, code=200)
    def get(self):
        """Get mail for a specific client."""
        return self.process_get()
