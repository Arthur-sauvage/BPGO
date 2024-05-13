""" This module contains the models for the financial synthesis. """

from flask_restx import Model, fields

model_synthese_analysis = Model(
    "SyntheseAnalysis",
    {
        "Vue Ensemble": fields.String(description="The financial analysis overview"),
        "Synthèse": fields.String(description="The financial analysis synthesis")
    },
)