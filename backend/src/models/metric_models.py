""" This module contains the models for the metric. """

from flask_restx import Model, fields

model_metric = Model(
    "Metric",
    {
        "metric": fields.Float(description="The Metric"),
    }
)