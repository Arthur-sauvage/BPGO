""" This module contains the models for the mails generation. """

from flask_restx import Model, fields

model_mail = Model(
    "Mail",
    {
        "Subject": fields.String(description="The mail subject"),
        "Body": fields.String(description="The mail body"),
    },
)