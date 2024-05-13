from flask_restx import Resource
from flask import request, jsonify
import logging


class BaseRoutesHandler(Resource):
    """Base class for handling routes."""

    def get_client_number(self):
        """Get the client number from the request arguments."""
        numero_client = request.args.get("numero_client")
        if not numero_client:
            logging.error("numero_client is required")
            return None, {"error": "numero_client is required"}, 400

        try:
            numero_client = int(numero_client)
            if numero_client <= 0 or numero_client > 10:
                logging.error("numero_client must be between 0 and 10")
                return None, {"error": "numero_client must be between 0 and 10"}, 400
            return numero_client, None, None
        except ValueError:
            logging.error("numero_client must be an integer")
            return None, {"error": "numero_client must be an integer"}, 400

    def process(self, numero_client):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def process_get(self):
        """Process the request to calculate the ratios."""
        numero_client, error, status = self.get_client_number()
        if error:
            return error, status

        logging.info(f"Calculating ratios for client {numero_client}...")
        try:
            return self.process(numero_client), 200
        except Exception as error:
            logging.error("An error occurred: %s", str(error))
            return jsonify({"error": str(error)}), 500

    def get(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
