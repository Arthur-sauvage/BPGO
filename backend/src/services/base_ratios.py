class BaseRatios():
    def __init__(self):
        self.data_compte_de_resultat = {
            "Chiffre d'affaires": [2463.0, 2656.0],
            "Production stockée": [0.0, 0.0],
            "Produits d'exploitation": [2478.0, 2677.0],
            "Achats de marchandises et de matières premières": [1582.0, 1743.0],
            "Variation de stocks": [-15.0, -20.0],
            "Autres charges externes": [235.0, 266.0],
            "Impôts et taxes": [8.0, 8.0],
            "Charges de personnel": [569.0, 579.0],
            "Dotations aux amortissements": [40.0, 36.0],
            "Dotations aux provisions": [0.0, 0.0],
            "Charges d'exploitation": [2419.0, 2611.0],
            "Résultat d'exploitation": [60.0, 66.0],
            "Produits financiers": [0.0, 0.0],
            "Charges financières": [2.0, 3.0],
            "Résultat financier": [-1.0, -3.0],
            "Résultat exceptionnel": [0.0, -8.0],
            "Impôts sur les sociétés": [11.0, 9.0],
            "Résultat net": [47.0, 46.0],
        }

        self.data_actif_circulant = {
            "Encours Clients": 249.921,
            "Encours Fournisseurs": 315.749,
            "CA": 2656.0,
            "Achats": 1743.0,
            "stocks": 42.323,
            "bfr": -418.506,
            "variation bfr": 55.706,
        }

        self.data_immobilisations = {
            "Immobilisations nettes": 151.808,
            "Variation immobilisations nettes": -13.0,
            "Immobilisations brutes": 668.313,
            "Dotations amortissement": 36.122,
            "Investissements": 21.49,
            "Disponibilités": 1018.13,
            "Capital": 555.885,
            "Dettes financières": 204.812,
        }

        self.data_input_financement = {
            "Capitaux Propres": 555.885,
            "Endettement net": 204.812,
            "EBE": [85.0, 80.0],
            "Résultat d'exploitation": 44.089,
            "Frais financiers": [1.0, 3.116],
            "Actif Economique": -266.698,
            "Actif immobilisé net": [165.0, 152.0],
            "Besoins en fonds de roulement": [-474.0, -419.0],
            "Dotations aux amortissements": [40.0, 36.0],
            "Impots sur les sociétés": [11.0, 9.0],
            "Dividendes": [0.0, 50.0],
            "disponibilité": [1056.185, 1029.624],
        }

        self.data_input_rentabilite = {
            "Chiffre d'affaires": [2463.0, 2656.0],
            "resultat_exploitation": [45.0, 44.089],
            "taux imposition": 0.20,
            "Actif Economique": -266.698,
            "Charges financieres": [1.0, 3.116],
            "Endettement net": [183.446, 204.812],
            "Capitaux Propres": [560.216, 555.885],
            "Résultat net": [32.0, 24.0],
            "Résultat exceptionnel": [0.0, -8.0],
            "disponibilité": [1056.185, 1029.624],
        }

        