""" This module contains the models for the rentabilite calculation. """

from flask_restx import Model, fields

model_input_rentabilite = Model(
    "InputRentabilite",
    {
        "Chiffre d'affaires": fields.List(fields.Float, description="The revenues"),
        "resultat_exploitation": fields.List(
            fields.Float, description="The operating result"
        ),
        "taux imposition": fields.Float(description="The tax rate"),
        "Actif Economique": fields.Float(description="The economic asset"),
        "Charges financieres": fields.List(
            fields.Float, description="The financial charges"
        ),
        "Endettement net": fields.List(fields.Float, description="The net debt"),
        "Capitaux Propres": fields.List(fields.Float, description="The equity"),
        "Résultat net": fields.List(fields.Float, description="The net result"),
        "Résultat exceptionnel": fields.List(
            fields.Float, description="The exceptional result"
        ),
        "disponibilité": fields.List(fields.Float, description="The availability"),
    },
)

model_rentabilite = Model(
    "OutputRentabilite",
    {
        "var_disponibilite": fields.Float(description="The tresory variation"),
        "resultat_exploitation_apre_impot_sur_ca": fields.Float(
            description="The operating result after tax on sales"
        ),
        "var_resultat_exploitation_apre_impot_sur_ca": fields.Float(
            description="The operating result after tax on sales variation"
        ),
        "ca_sur_actif_economique": fields.Float(
            description="The sales on the economic asset"
        ),
        "rentabilite_economique": fields.Float(
            description="The economic profitability"
        ),
        "cout_dettes": fields.Float(description="The debt cost"),
        "var_cout_dettes": fields.Float(description="The debt cost variation"),
        "levier_financier": fields.Float(description="The financial leverage"),
        "var_levier_financier": fields.Float(
            description="The financial leverage variation"
        ),
        "rentabilite_capitaux_propres": fields.Float(
            description="The equity profitability"
        ),
        "var_rentabilite_capitaux_propres": fields.Float(
            description="The equity profitability variation"
        ),
        "part_rentabilite_capitaux_propres_levier": fields.Float(
            description="The equity profitability part of the financial leverage"
        ),
    },
)

model_global = Model(
    "GlobalRentabilite",
    {
        "data_input_rentabilite": fields.Nested(model_input_rentabilite),
        "data_rentabilite": fields.Nested(model_rentabilite),
    },
)

model_rentabilite_analysis = Model(
    "RentabiliteAnalysis",
    {
        "Résultat d'exploitation après impôt et Rentabilité économique": fields.String(
            description="The operating result after tax and economic profitability"
        ),
        "Coût de la dette et levier financier": fields.String(
            description="The debt cost and financial leverage"
        ),
        "Rentabilité des capitaux propres": fields.String(
            description="The equity profitability"
        ),
        "Risques de l'entreprise": fields.String(description="The company risks"),
        "Synthèse": fields.String(description="The synthesis"),
    },
)
