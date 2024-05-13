""" This module contains the models for the Investissements calculation. """

from flask_restx import Model, fields

model_immobilisations = Model(
    "Immobilisations",
    {
        "Immobilisations nettes": fields.Float(description="The net investments"),
        "Variation immobilisations nettes": fields.Float(description="The net investments variation"),
        "Immobilisations brutes": fields.Float(description="The gross investments"),
        "Dotations amortissement": fields.Float(description="The amortization provisions"),
        "Investissements": fields.Float(description="The investments"),
        "Disponibilités": fields.Float(description="The availabilities"),
        "Capital": fields.Float(description="The capital"),
        "Dettes financières": fields.Float(description="The financial debts")
    }
)

model_ratios_investissements = Model(
    "Investissements",
    {
        "actif_economique": fields.Float(description="The economic assets"),
        "degre_usure": fields.Float(description="The wear degree"),
        "taux_amortissement": fields.Float(description="The amortization rate")
    }
)

model_investissements = Model(
    "Investissements",
    {
        "data_immobilisations": fields.Nested(model_immobilisations),
        "investissements": fields.Nested(model_ratios_investissements)
    }
)

model_investissements_analysis = Model(
    "InvestissementsAnalysis",
    {
        "Analyse de la politique d'investissements": fields.String(description="The investments policy analysis"),
        "Synthèse et points d'attentions": fields.String(description="The synthesis and attention points")
    }
)