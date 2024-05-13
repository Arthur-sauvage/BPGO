import os
import logging
import time
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)

load_dotenv()

VUE_ENSEMBLE = """
Bien que l'entreprise ait montré une capacité à augmenter son chiffre d'affaires au-dessus de la moyenne du secteur, des défis importants persistent en termes de marges, de gestion de trésorerie, et d'investissements, qui nécessitent une attention particulière pour évaluer les risques et les opportunités associés à sa structure de dette."""

SYNTHESE = """
Le client présente une situation de risque modéré avec des opportunités potentielles si certaines mesures sont prises. Il est conseillé de réexaminer les coûts opérationnels et de production pour améliorer les marges, de renégocier ou de diversifier les accords avec les fournisseurs pour réduire le risque opérationnel, et d'élaborer une stratégie proactive d'investissements pour moderniser l'outil industriel. Par ailleurs, une stratégie financière visant à réduire progressivement la dépendance au levier tout en soutenant la croissance par des capitaux propres pourrait équilibrer le risque et renforcer la santé financière à long terme.

En conclusion, bien que l'entreprise ait démontré une capacité à générer des revenus au-delà de la croissance sectorielle, elle doit aborder avec prudence ses vulnérabilités en termes de coûts, de gestion des fournisseurs, et de dépendance à l'endettement pour maintenir une trajectoire de croissance durable et réduire les risques financiers associés.
"""

PRE_GENERATED_ANALYSIS_10 = {"Vue Ensemble": VUE_ENSEMBLE, "Synthèse": SYNTHESE}


def generate_analysis(numero_client, pre_generated=True):
    if pre_generated and numero_client == 10:
        return PRE_GENERATED_ANALYSIS_10

    # if not pre_generated:
    #     generate()
    return None
