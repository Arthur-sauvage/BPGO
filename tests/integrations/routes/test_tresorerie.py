""" Tests for the tresorerie route. """

import unittest
from flask import Flask
from flask_restx import Api
from flask_testing import TestCase
from backend.src.routes.tresorerie import tresorerie_ns


class TestRatiosRoute(TestCase):
    """Tests for the tresorerie route."""

    def create_app(self):
        """Creates the Flask app with namespaces."""
        app = Flask(__name__)
        api = Api(app, doc="/docs")

        api.add_namespace(tresorerie_ns, path="/tresorerie")

        return app

    def test_get_valid_client(self):
        """Tests a valid client number request."""
        response = self.client.get(
            "/tresorerie/ratios", query_string={"numero_client": 5}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("fond de roulement", response.json)

    def test_get_missing_client(self):
        """Tests request with no client number."""
        response = self.client.get("/tresorerie/ratios")
        self.assertEqual(response.status_code, 400)
        # self.assertIn("error", response.json)
        # self.assertEqual(response.json["error"], "numero_client is required")

    def test_get_invalid_client(self):
        """Tests request with an invalid client number."""
        response = self.client.get(
            "/tresorerie/ratios", query_string={"numero_client": 15}
        )
        self.assertEqual(response.status_code, 400)
        # self.assertIn("error", response.json)
        # self.assertEqual(
        #     response.json["error"], "numero_client must be between 0 and 10"
        # )

    def test_get_non_integer_client(self):
        """Tests request with a non-integer client number."""
        response = self.client.get(
            "/tresorerie/ratios", query_string={"numero_client": "abc"}
        )
        self.assertEqual(response.status_code, 400)
        # self.assertIn("error", response.json)
        # self.assertEqual(response.json["error"], "numero_client must be an integer")


if __name__ == "__main__":
    unittest.main()
