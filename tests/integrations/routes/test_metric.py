""" Integration tests for the Metric route """

import unittest
from flask import Flask
from flask_restx import Api
from flask_testing import TestCase
from backend.src.routes.metric import metric_ns


class TestIntegrationMetricRoute(TestCase):
    """Tests for the metric route"""

    def create_app(self):
        """Creates the Flask app with namespaces."""
        app = Flask(__name__)
        api = Api(app, doc="/docs")

        api.add_namespace(metric_ns, path="/metric")

        return app

    def test_get_valid_client(self):
        """Tests a valid client number request"""
        response = self.client.get(
            "/metric/", query_string={"numero_client": 5, "metric": "Mt. disponibilités CF"}
        )
        self.assertEqual(response.status_code, 200)

        data = response.json
        self.assertIn("metric", data)

    def test_complet_valid_request(self):
        """Test a valid request to the Metric route with a bilan complet client"""
        response = self.client.get(
            "/metric/", query_string={"numero_client": 9, "metric": "Mt. résultat de l'exercice DI"}
        )
        self.assertEqual(response.status_code, 200)

        data = response.json
        self.assertIn("metric", data)


    def test_missing_client(self):
        """Test a request with missing `numero_client` parameter"""
        response = self.client.get(
            "/metric/",
        )
        self.assertEqual(response.status_code, 400)

        # data = response.json()
        # self.assertIn("error", data)
        # self.assertEqual(data["error"], "numero_client is required")

    def test_invalid_client(self):
        """Test a request with an invalid `numero_client`"""
        response = self.client.get(
            "/metric/", query_string={"numero_client": -5}
        )

        self.assertEqual(response.status_code, 400)

        # data = response.json()
        # self.assertIn("error", data)
        # self.assertEqual(data["error"], "numero_client must be between 0 and 10")

    def test_non_integer_client(self):
        """Test a request with a non-integer `numero_client`"""
        response = self.client.get(
            "/metric/", query_string={"numero_client": "abc"}
        )
        self.assertEqual(response.status_code, 400)

        # data = response.json()
        # self.assertIn("error", data)
        # self.assertEqual(data["error"], "numero_client must be an integer")


if __name__ == "__main__":
    unittest.main()
