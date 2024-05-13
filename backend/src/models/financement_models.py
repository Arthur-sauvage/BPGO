""" This module contains the models for the financement calculation. """

from flask_restx import Model, fields

model_input_financement = Model(
    "InputFinancement",
    {
        "Capitaux Propres": fields.Float(description="The equity"),
        "Endettement net": fields.Float(description="The net debt"),
        "EBE": fields.List(fields.Float, description="The EBE"),
        "Résultat d'exploitation": fields.Float(description="The operating result"),
        "Frais financiers": fields.List(fields.Float, description="The financial charges"),
        "Actif Economique": fields.Float(description="The economic asset"),
        "Actif immobilisé net": fields.List(fields.Float, description="The net fixed assets"),
        "Besoins en fonds de roulement": fields.List(fields.Float, description="The working capital requirements"),
        "Dotations aux amortissements": fields.List(fields.Float, description="The amortization provisions"),
        "Impots sur les sociétés": fields.List(fields.Float, description="The corporation taxes"),
        "Dividendes": fields.List(fields.Float, description="The dividends"),
        "disponibilité": fields.List(fields.Float, description="The availability")
    }
)

model_output_financement = Model(
    "OutputFinancement",
    {
        "ratio_endettement": fields.Float(description="The debt ratio"),
        "dettes_sur_ebe": fields.Float(description="The debt on the EBE"),
        "res_exploit_sur_frais_financiers": fields.Float(description="The operating result on the financial charges"),
        "caf": fields.Float(description="The cash flow"),
        "var_caf": fields.Float(description="The cash flow variation"),
        "var_bfr": fields.Float(description="The working capital requirements variation"),
        "flux_treso_exploitation": fields.Float(description="The operating cash flow"),
        "flux_investissements": fields.Float(description="The investment cash flow"),
        "desendettement_net": fields.Float(description="The net disinvestment")
    }
)

model_global = Model(
    "GlobalFinancement",
    {
        "data_input_financement": fields.Nested(model_input_financement),
        "data_financement": fields.Nested(model_output_financement)
    }
)

model_financement_analysis = Model(
    "FinancementAnalysis",
    {
        "Analyse des flux de trésorerie et du désendettement net": fields.String(description="The cash flow and net disinvestment analysis"),
        "Structure du Financement": fields.String(description="The financing structure"),
        "Analyse de l'actif économique et des disponibilités": fields.String(description="The economic asset and availability analysis"),
        "Synthèse": fields.String(description="The synthesis")
    }
)