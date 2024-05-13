QUERY_SIMPLIFIE = """
    SELECT
        "{metric}" AS metric
    FROM
        bilans_simplifies
    WHERE
        numero_client = %(numero_client)s
"""

QUERY_COMPLET = """
    SELECT
        "{metric}" AS metric
    FROM
        bilans_complets
    WHERE
        numero_client = %(numero_client)s
"""

QUERY_TRESORERIE_SIMPLIFIE = """
        SELECT
            "Mt. total actif circulant CJ" AS actif_circulant,
            "Mt. total des dettes (total IV) EC" AS dettes_courantes,
            "Mt. disponibilités CF" AS cash,
            "Mt. clients et comptes rattachés BX" AS receivables_1,
            "Mt. autres créances BZ" AS receivables_2,
            "Dettes fourn. et cptes rattachés DX" AS payables_1,
            "Mt. mat. premières & approv. BL" AS stock_1,
            "Mt. en cours de prod. de biens BN" AS stock_2,
            "Mt. en cours de prod. de services BP" AS stock_3,
            "Mt. produits intermed. et finis BR" AS stock_4,
            "Mt. marchandises BT" AS stock_5
        FROM
            bilans_simplifies
        WHERE
            numero_client = %(numero_client)s
    """


QUERY_TRESORERIE_COMPLET = """
        SELECT
            "Mt. total actif circulant CJ" AS actif_circulant,
            "Mt. total des dettes (total IV) EC" AS dettes_courantes,
            "Mt. disponibilités CF" AS cash,
            "Mt. clients et comptes rattachés BX" AS receivables_1,
            "Mt. autres créances BZ" AS receivables_2,
            "Dettes fourn. et cptes rattachés DX" AS payables_1,
            "Mt. mat. premières & approv. BL" AS stock_1,
            "Mt. en cours de prod. de biens BN" AS stock_2,
            "Mt. en cours de prod. de services BP" AS stock_3,
            "Mt. produits intermed. et finis BR" AS stock_4,
            "Mt. marchandises BT" AS stock_5
        FROM
            bilans_complets
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_STRUCTURE_FINANCEMENT_SIMPLIFIE = """
        SELECT
            "Mt. total des fonds propres DL" AS fonds_propres,
            "Mt. total des dettes (total IV) EC" AS dettes_courantes,
            "Emprunts & dettes chez ets crédit DU" AS lt_dettes_financieres_1,
            "Emprunts & dettes financières div DV" AS lt_dettes_financieres_2,
            "Mt. Résultat d'exploitation GG" AS resultat_exploitation,
            "Total des charges financières GU" AS interets,
            "Mt. total général actif CO" AS total_actif
        FROM
            bilans_simplifies
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_STRUCTURE_FINANCEMENT_COMPLET = """
        SELECT
            "Mt. total des fonds propres DL" AS fonds_propres,
            "Mt. total des dettes (total IV) EC" AS dettes_courantes,
            "Emprunts & dettes chez ets crédit DU" AS lt_dettes_financieres_1,
            "Emprunts & dettes financières div DV" AS lt_dettes_financieres_2,
            "Mt. Résultat d'exploitation GG" AS resultat_exploitation,
            "Total des charges financières GU" AS interets,
            "Mt. total général actif CO" AS total_actif
        FROM
            bilans_complets
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_RENTABILITE_SIMPLIFIE = """
        SELECT
            "Mt. résultat de l'exercice DI" AS profit,
            "Mt. total des fonds propres DL" AS equity,
            "Mt. total général actif CO" AS total_assets,
            "Mt. Résultat d'exploitation GG" AS resultat_exploitation,
            "Chiffre d'affaire net total FL" AS revenue
        FROM
            bilans_simplifies
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_RENTABILITE_COMPLET = """
        SELECT
            "Mt. résultat de l'exercice DI" AS profit,
            "Mt. total des fonds propres DL" AS equity,
            "Mt. total général actif CO" AS total_assets,
            "Mt. Résultat d'exploitation GG" AS resultat_exploitation,
            "Chiffre d'affaire net total FL" AS revenue
        FROM
            bilans_complets
        WHERE
            numero_client = %(numero_client)s
    """


QUERY_INVESTISSEMENT_SIMPLIFIE = """
        SELECT
            "Mt. résultat de l'exercice DI" AS profit,
            "Mt. total actif immobilisé BJ" AS fixed_assets,
            "Chiffre d'affaire net total FL" AS revenue,
            "Am. total actif immobilisé BK" AS amortization
        FROM
            bilans_simplifies
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_INVESTISSEMENT_COMPLET = """
        SELECT
            "Mt. résultat de l'exercice DI" AS profit,
            "Mt. total actif immobilisé BJ" AS fixed_assets,
            "Chiffre d'affaire net total FL" AS revenue,
            "Am. total actif immobilisé BK" AS amortization
        FROM
            bilans_complets
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_OPERATIONNEL_SIMPLIFIE = """
        SELECT
            "Total des produits HL" AS revenue,
            "Total des charges d'exploitation GF" AS operating_costs
        FROM
            bilans_simplifies
        WHERE
            numero_client = %(numero_client)s
    """

QUERY_OPERATIONNEL_COMPLET = """
        SELECT
            "Total des produits HL" AS revenue,
            "Total des charges d'exploitation GF" AS operating_costs
        FROM
            bilans_complets
        WHERE
            numero_client = %(numero_client)s
    """
