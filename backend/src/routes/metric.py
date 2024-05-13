""" File that contains the routes for the Metric blueprint """

import logging
from flask import request
from flask_restx import Namespace
from src.routes.base_routes_handler import BaseRoutesHandler
from src.models.metric_models import model_metric
from src.services.get_metric import get_metric

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

metric_ns = Namespace("Metric", description="Metric")

metric_ns.models[model_metric.name] = model_metric


@metric_ns.route("/", methods=["GET"])
class HandleMetric(BaseRoutesHandler):
    """Class to handle the metrics"""

    def process(self, numero_client):
        return get_metric(numero_client=numero_client, metric=self.metric)

    @metric_ns.doc(
        responses={
            200: "Success",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        params={
            "numero_client": "Client number for which to extract the metric",
            "metric": "The metric to get",
        },
    )
    @metric_ns.marshal_with(model_metric, code=200)
    def get(self):
        """Get the specified metric for a specific client."""
        self.metric = request.args.get("metric")
        return self.process_get()
