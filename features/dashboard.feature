Feature: The frontend for financial analyzes
    As a Conseiller Pro
    I need a WebApp accessible
    So that I can select a client and get my analyzes

Scenario: Select a specific client
    Given I visit the homepage
    When I click on select a specific numero_client
    Then I have the dashboard displayed for the right client

Scenario: Select the "Analyse de la Trésorerie"
    Given I am in the dashboard for a specific client
    When I click on "Analyse de la Trésorerie"
    Then I have the markdown "Analyse de la Trésorerie"
    And I have a metric for "Analyse Besoins en Fonds de Roulement"

Scenario: Select the "Analyse de la Structure de Financement"
    Given I am in the dashboard for a specific client
    When I click on "Analyse de la Structure de Financement"
    Then I have the markdown "Analyse de la Structure de Financement"
    And I have a metric for "Ratio de couverture des intérêts"

Scenario: Select the "Analyse de la Rentabilité"
    Given I am in the dashboard for a specific client
    When I click on "Analyse de la Rentabilité"
    Then I have the markdown "Analyse de la Rentabilité"
    And I have a metric for "Return on Assets"

Scenario: Select the "Analyse des Investissements"
    Given I am in the dashboard for a specific client
    When I click on "Analyse des Investissements"
    Then I have the markdown "Analyse des Investissements"
    And I have a metric for "Ammortissements sur Investissements"