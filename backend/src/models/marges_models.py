""" This module contains the models for the marges calculation. """

from flask_restx import Model, fields

model_compte_de_resultat = Model(
    "CompteDeResultat",
    {
        "Chiffre d'affaires": fields.List(fields.Float, description="The revenue"),
        "Production stockée": fields.List(fields.Float, description="The stored production"),
        "Produits d'exploitation": fields.List(fields.Float, description="The operating products"),
        "Achats de marchandises et de matières premières": fields.List(fields.Float, description="The goods purchases"),
        "Variation de stocks": fields.List(fields.Float, description="The stock variation"),
        "Autres charges externes": fields.List(fields.Float, description="The other external charges"),
        "Impôts et taxes": fields.List(fields.Float, description="The taxes"),
        "Charges de personnel": fields.List(fields.Float, description="The personnel charges"),
        "Dotations aux amortissements": fields.List(fields.Float, description="The amortization provisions"),
        "Dotations aux provisions": fields.List(fields.Float, description="The provisions"),
        "Charges d'exploitation": fields.List(fields.Float, description="The operating charges"),
        "Résultat d'exploitation": fields.List(fields.Float, description="The operating result"),
        "Produits financiers": fields.List(fields.Float, description="The financial products"),
        "Charges financières": fields.List(fields.Float, description="The financial charges"),
        "Résultat financier": fields.List(fields.Float, description="The financial result"),
        "Résultat exceptionnel": fields.List(fields.Float, description="The exceptional result"),
        "Impôts sur les sociétés": fields.List(fields.Float, description="The corporation taxes"),
        "Résultat net": fields.List(fields.Float, description="The net result")
    }
)

sub_model_retraitement = Model(
    "Retraitement_Metric",
    {
        "valeurs": fields.List(fields.Float, description="The reprocessing value"),
        "croissance": fields.Float(description="The reprocessing growth")
    }
)

model_retraitement = Model(
    "Retraitement",
    {
        "Chiffre d'affaires": fields.Nested(sub_model_retraitement),
        "Consommations": fields.Nested(sub_model_retraitement),
        "Marge brute": fields.Nested(sub_model_retraitement),
        "EBE": fields.Nested(sub_model_retraitement),
        "Résultat d'exploitation": fields.Nested(sub_model_retraitement),
        "Charges financières nettes": fields.Nested(sub_model_retraitement),
        "Résultat net": fields.Nested(sub_model_retraitement)
    }
)

model_marges = Model(
    "Marges",
    {
        "Consommations": fields.List(fields.Float, description="The consumptions on the revenue"),
        "Valeur ajoutée": fields.List(fields.Float, description="The added value"),
        "Autres charges externes sur CA": fields.List(fields.Float, description="The other external charges on the revenue"),
        "Impôts sur CA": fields.List(fields.Float, description="The tax on the revenue"),
        "Charges de personnel sur CA": fields.List(fields.Float, description="The personnel charges on the revenue"),
        "Dotations aux provisions sur CA": fields.List(fields.Float, description="The provisions on the revenue"),
        "EBE sur CA": fields.List(fields.Float, description="The EBE on the revenue"),
        "Dotations aux amortissements sur CA": fields.List(fields.Float, description="The amortization provisions on the revenue"),
        "Résultat d'exploitation sur CA": fields.List(fields.Float, description="The operating result on the revenue"),
        "Charges financières sur CA": fields.List(fields.Float, description="The financial charges on the revenue"),
        "Résultat exceptionnel sur CA": fields.List(fields.Float, description="The exceptional result on the revenue"),
        "Impôts sur les sociétés sur CA": fields.List(fields.Float, description="The corporation taxes on the revenue"),
        "Résultat net sur CA": fields.List(fields.Float, description="The net result on the revenue")
    }
)

model_points_morts = Model(
    "Points Morts",
    {
        "Points morts opérationnel": fields.List(fields.Float, description="The operational break-even point in absolute"),
        "CA sur Points morts opérationnel": fields.List(fields.Float, description="The operational break-even point relative on CA"),
        "Points morts totaux": fields.List(fields.Float, description="The break-even point in absolute"),
        "CA sur Points morts totaux": fields.List(fields.Float, description="The break-even point relative on CA")
    }
)

model_all_combined = Model(
    "AllCombined",
    {
        "Compte de résultat": fields.Nested(model_compte_de_resultat),
        "Retraitement": fields.Nested(model_retraitement),
        "Marges": fields.Nested(model_marges),
        "Points Morts": fields.Nested(model_points_morts)
    }
)

model_marge_analysis = Model(
    "MargeAnalysis",
    {
        "Chiffre d'affaire": fields.String(description="The revenue Analysis"),
        "Valeur ajoutée": fields.String(description="The added value Analysis"),
        "Charges de Personnel": fields.String(description="The personnel charges Analysis"),
        "Point mort": fields.String(description="The break-even point Analysis"),
        "Resultat d'exploitation": fields.String(description="The operating result Analysis"),
        "Résultat Net": fields.String(description="The net result Analysis"),
        "Synthèse": fields.String(description="The synthesis Analysis")
    }
)