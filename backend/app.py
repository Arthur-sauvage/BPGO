"""
Define the Flask app.
"""

from flask import Flask
from flask_restx import Api
from src.routes.rentabilite import rentabilite_ns
from src.routes.marges import marges_ns
from src.routes.bfr import bfr_ns
from src.routes.investissements import investissements_ns
from src.routes.financements import financements_ns
from src.routes.metric import metric_ns
from src.routes.synthese_financiere import synthesis_ns
from src.routes.mails import mails_ns

app = Flask(__name__)

api = Api(
    app,
    title="API - Appui Pro",
    version="1.0",
    description="API for the Appui PRO",
    doc="/docs",
)

api.add_namespace(marges_ns, path="/marges")
api.add_namespace(bfr_ns, path="/bfr")
api.add_namespace(investissements_ns, path="/investissements")
api.add_namespace(financements_ns, path="/financements")
api.add_namespace(rentabilite_ns, path="/rentabilite")
api.add_namespace(metric_ns, path="/metric")
api.add_namespace(synthesis_ns, path="/synthese")
api.add_namespace(mails_ns, path="/mails")

if __name__ == "__main__":
    app.run(port=8001)
