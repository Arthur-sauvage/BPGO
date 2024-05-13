""" Unit tests for the fill_database module """

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.fill_database import (
    connect_to_db,
    get_excel,
    load_all_excel,
    mapping,
    save_to_db,
    main,
)


class TestFillDatabase(unittest.TestCase):
    """Unit tests for the fill_database module"""

    def setUp(self):
        # Mocking the logging to check log outputs
        self.patcher = patch("utils.fill_database.logging")
        self.mock_logging = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    @patch("utils.fill_database.create_engine")
    @patch("os.getenv")
    def test_connect_to_db(self, mock_getenv, mock_create_engine):
        """Test that the function connects to the database with the correct parameters"""
        # Mocking environment variables
        mock_getenv.side_effect = lambda var: {
            "POSTGRES_USER": "my_user",
            "POSTGRES_PASSWORD": "my_password",
            "POSTGRES_HOST": "localhost",
            "POSTGRES_PORT": "5432",
            "POSTGRES_DB": "my_db",
        }.get(var)

        connect_to_db()

        # Check that create_engine was called with the correct arguments
        mock_create_engine.assert_called_once_with(
            "postgresql://my_user:my_password@localhost:5432/my_db"
        )

    @patch("utils.fill_database.create_engine")
    @patch("os.getenv")
    def test_fail_connect_to_db(self, mock_getenv, mock_create_engine):
        """Test that the function raises an error when an environment variable is missing"""
        # Mocking environment variables
        mock_getenv.side_effect = lambda var: {
            "POSTGRES_PASSWORD": "my_password",
            "POSTGRES_HOST": "localhost",
            "POSTGRES_PORT": "5432",
            "POSTGRES_DB": "my_db",
        }.get(var)

        with self.assertRaises(KeyError):
            connect_to_db()

        # Check that create_engine was not called
        mock_create_engine.assert_not_called()

    @patch("pandas.read_excel")
    def test_valid_file_and_sheet(self, mock_read_excel):
        """Test that the get_excel function returns a dataframe with the expected columns"""
        # Mock dataframe returned by read_excel
        mock_read_excel.return_value = pd.DataFrame(
            {"Champs": ["C1", "C2"], "Détail": ["Revenue", "Profit"]}
        )

        df_test = get_excel("test_file.xlsx", "Glossary")
        self.assertIsNotNone(df_test)
        self.assertEqual(df_test.shape, (2, 2))
        self.assertEqual(list(df_test.columns), ["Champs", "Détail"])

    def test_get_excel_file_not_found(self):
        """Test that the get_excel function raises a FileNotFoundError when the file is not found"""

        with self.assertRaises(FileNotFoundError) as context:
            get_excel("non_existent_file.xlsx", "Glossary")

        self.assertIn("File not found", str(context.exception))

    @patch("utils.fill_database.get_excel")
    def test_all_sheets_loaded(self, mock_get_excel):
        """Test that the function returns a list of dataframes with the expected shapes"""
        # Mock dataframes for each sheet
        df_glossaire = pd.DataFrame(
            {"Champs": ["C1", "C2"], "Détail": ["Revenue", "Profit"]}
        )
        df_bilans_simplifies = pd.DataFrame({"C1": [1, 2], "C2": [3, 4]})
        df_bilans_complets = pd.DataFrame({"C1": [5, 6], "C2": [7, 8]})
        df_indicateurs_commerciaux = pd.DataFrame({"C1": [9, 10]})
        df_flux = pd.DataFrame({"C1": [11, 12]})
        df_equipements = pd.DataFrame({"Equipments": [1, 2, 3]})

        # Set mock return values for get_excel
        mock_get_excel.side_effect = [
            df_glossaire,
            df_bilans_simplifies,
            df_bilans_complets,
            df_indicateurs_commerciaux,
            df_flux,
            df_equipements,
        ]

        result = load_all_excel()

        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].shape, (2, 2))
        self.assertEqual(list(result[0].columns), ["Champs", "Détail"])

    @patch("utils.fill_database.get_excel")
    def test_load_all_excel_file_not_found(self, mock_get_excel):
        """Test that the load_all_excel function raises a FileNotFoundError when get_excel raises it"""
        # Mock get_excel to raise FileNotFoundError
        mock_get_excel.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError) as context:
            load_all_excel()

        self.assertIn("One or more files not found", str(context.exception))

    def test_mapping(self):
        """Test that the function returns a dataframe with the expected columns"""
        df_glossaire = pd.DataFrame(
            {"Champs": ["C1", "C2"], "Détail": ["Revenue", "Profit"]}
        )
        df_to_decode = pd.DataFrame({"C1": [1, 2], "C2": [3, 4]})

        df_decoded = mapping(df_glossaire, df_to_decode)
        self.assertEqual(list(df_decoded.columns), ["Revenue", "Profit"])

    @patch("pandas.DataFrame.to_sql")
    def test_save_to_db(self, mock_to_sql):
        """Test that the function calls to_sql with the correct arguments"""
        df_test = pd.DataFrame({"Revenue": [1000, 2000]})

        engine = MagicMock()
        save_to_db(df_test, "test_table", engine)

        # Check that to_sql was called with the correct arguments
        mock_to_sql.assert_called_once_with(
            "test_table", engine, if_exists="replace", index=False
        )

    @patch("utils.fill_database.connect_to_db")
    @patch("utils.fill_database.load_all_excel")
    @patch("utils.fill_database.mapping")
    @patch("pandas.DataFrame.to_sql")
    def test_main_valid_data(
        self, mock_to_sql, mock_mapping, mock_load_all_excel, mock_connect_to_db
    ):
        """Test that the main function calls the correct functions with the expected arguments"""
        # Mocked dataframes
        df_glossaire = pd.DataFrame(
            {"Champs": ["C1", "C2"], "Détail": ["Revenue", "Profit"]}
        )
        df_bilans_simplifies = pd.DataFrame({"C1": [1, 2], "C2": [3, 4]})
        df_bilans_complets = pd.DataFrame({"C1": [5, 6], "C2": [7, 8]})
        df_indicateurs_commerciaux = pd.DataFrame({"C1": [9, 10]})
        df_flux = pd.DataFrame({"C1": [11, 12]})
        df_equipements = pd.DataFrame({"Equipments": [1, 2, 3]})

        # Mocking load_all_excel to return these dataframes
        mock_load_all_excel.return_value = (
            df_glossaire,
            df_bilans_simplifies,
            df_bilans_complets,
            df_indicateurs_commerciaux,
            df_flux,
            df_equipements,
        )

        # Mock mapping to transform dataframes
        mock_mapping.side_effect = lambda df1, df2: df2.rename(
            columns=dict(zip(df1["Champs"], df1["Détail"]))
        )

        # Mocked database engine
        engine = MagicMock()
        mock_connect_to_db.return_value = engine

        # Run the main function
        main()

        # Assertions for each function call
        mock_connect_to_db.assert_called_once()
        mock_load_all_excel.assert_called_once()
        mock_to_sql.assert_any_call(
            "bilans_simplifies", engine, if_exists="replace", index=False
        )
        mock_to_sql.assert_any_call(
            "bilans_complets", engine, if_exists="replace", index=False
        )
        mock_to_sql.assert_any_call(
            "indicateurs_commerciaux", engine, if_exists="replace", index=False
        )
        mock_to_sql.assert_any_call("flux", engine, if_exists="replace", index=False)
        mock_to_sql.assert_any_call(
            "equipements", engine, if_exists="replace", index=False
        )

    @patch("utils.fill_database.load_all_excel")
    def test_main_file_not_found(self, mock_load_all_excel):
        """Test that the main function raises a FileNotFoundError when a file is not found."""
        # Mock load_all_excel to raise FileNotFoundError
        mock_load_all_excel.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError) as context:
            main()

        self.assertIn("One or more files not found", str(context.exception))


if __name__ == "__main__":
    unittest.main()
