""" This module contains the models for the BFR calculation. """

from flask_restx import Model, fields


model_actif_circulant = Model(
    "ActifCirculant",
    {
        "Encours Clients": fields.Float(description="The clients balance"),
        "Encours Fournisseurs": fields.Float(description="The suppliers balance"),
        "CA": fields.Float(description="The revenue"),
        "Achats": fields.Float(description="The purchases"),
        "stocks": fields.Float(description="The stocks"),
        "bfr": fields.Float(description="The bfr"),
        "variation bfr": fields.Float(description="The bfr variation"),
        "Disponibilités": fields.Float(description="The cash")
    }
)

model_bfr_ratios = Model(
    "BFRRatios",
    {
        "rotation_credit_client": fields.Float(description="The clients credit rotation"),
        "rotation_credit_fournisseur": fields.Float(description="The suppliers credit rotation"),
        "rotation_stock": fields.Float(description="The stock rotation"),
        "rotation_bfr": fields.Float(description="The bfr rotation"),
        "rotation_var_bfr": fields.Float(description="The bfr variation rotation")
    }
)

model_bfr = Model(
    "BFR",
    {
        "data_actif_circulant": fields.Nested(model_actif_circulant),
        "bfr_ratios": fields.Nested(model_bfr_ratios)
    }
)

model_bfr_analysis = Model(
    "BFRInvestissementsAnalysis",
    {
        "Analyse du Besoin en Fonds de Roulement (BFR)": fields.String(description="The BFR analysis"),
        "Synthèse et points d'attentions": fields.String(description="The synthesis and attention points")
    }
)