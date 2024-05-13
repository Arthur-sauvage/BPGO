""" This script fills the database with the data from the excel files """

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def connect_to_db():
    """Connect to the database"""
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise KeyError("One or more environment variables are missing")

    engine = create_engine(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    return engine


def get_excel(file_name, sheet):
    """Get the glossary from the excel file"""
    try:
        df_glossaire = pd.read_excel(io=file_name, sheet_name=sheet)
    except FileNotFoundError:
        logging.error("File not found", exc_info=True)
        raise FileNotFoundError("File not found")
    return df_glossaire


def load_all_excel():
    """Load all the excel files"""
    try:
        df_glossaire = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Dictionnaire données",
        )
        df_bilans_simplifies = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Bilans simplifiés",
        )
        df_bilans_complets = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Bilans complets",
        )
        df_indicateurs_commerciaux = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Indicateurs_commerciaux",
        )
        df_flux = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Flux",
        )
        df_equipements = get_excel(
            file_name="documents/Dossier Equinoxe/fichier_appui_pro_26APR24.xlsx",
            sheet="Equipement",
        )
    except FileNotFoundError:
        logging.error("One or more files not found", exc_info=True)
        raise FileNotFoundError("One or more files not found")

    return (
        df_glossaire,
        df_bilans_simplifies,
        df_bilans_complets,
        df_indicateurs_commerciaux,
        df_flux,
        df_equipements,
    )


def mapping(df_glossaire, df_to_decode):
    """Decode the dataframe using the glossary"""
    mapping_dict = dict(zip(df_glossaire["Champs"], df_glossaire["Détail"]))
    df_decoded = df_to_decode.rename(columns=mapping_dict)
    logging.info("Dataframe decoded")
    return df_decoded


def save_to_db(df_to_save, table_name, engine):
    """Save the dataframe to the database"""
    df_to_save.to_sql(table_name, engine, if_exists="replace", index=False)
    logging.info("Dataframe saved to database")


def main():
    """Main function"""
    engine = connect_to_db()

    try:
        (
            df_glossaire,
            df_bilans_simplifies,
            df_bilans_complets,
            df_indicateurs_commerciaux,
            df_flux,
            df_equipements,
        ) = load_all_excel()
    except FileNotFoundError:
        raise FileNotFoundError("One or more files not found")

    # Save the bilans simplifies to the db
    df_bilans_simplifies_decoded = mapping(df_glossaire, df_bilans_simplifies)
    save_to_db(df_bilans_simplifies_decoded, "bilans_simplifies", engine)

    # Save the bilans complets to the db
    df_bilans_complets_decoded = mapping(df_glossaire, df_bilans_complets)
    save_to_db(df_bilans_complets_decoded, "bilans_complets", engine)

    # Save the indicateurs commerciaux
    df_indicateurs_commerciaux_decoded = mapping(
        df_glossaire, df_indicateurs_commerciaux
    )
    save_to_db(df_indicateurs_commerciaux_decoded, "indicateurs_commerciaux", engine)

    # Save the flux
    df_flux_decoded = mapping(df_glossaire, df_flux)
    save_to_db(df_flux_decoded, "flux", engine)

    # Save the Equipements
    save_to_db(df_equipements, "equipements", engine)


if __name__ == "__main__":
    main()
