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

ANALYSE_BFR = """
L'entreprise cliente présente un BFR négatif de -58 jours de CA, ce qui est une situation très favorable. En effet, cela signifie que l'entreprise finance une partie de son cycle d'exploitation par ses fournisseurs et/ou ses clients. C'est une situation très avantageuse car elle permet de libérer de la trésorerie. Cependant, il est important de noter que cette situation est assez rare et peut être le signe d'une gestion très serrée des délais de paiement. 

En comparaison avec le secteur du déménagement, l'entreprise se distingue nettement. En effet, le secteur présente un BFR de 28 jours de CA, ce qui est nettement supérieur à celui de l'entreprise. De plus, l'entreprise a un délai de rotation du crédit fournisseur plus long que la moyenne du secteur (66 jours contre 28 jours), ce qui signifie qu'elle paie ses fournisseurs plus tardivement. Cela peut être un avantage en termes de trésorerie, mais peut également être le signe de tensions avec les fournisseurs.
"""

SYNTHESE = """
L'entreprise présente une gestion du BFR très favorable avec un BFR négatif et des délais de paiement fournisseurs plus longs que la moyenne du secteur. Cependant, cette situation peut être le signe de tensions avec les fournisseurs et nécessite une vigilance particulière. 
"""

PRE_GENERATED_ANALYSIS_10 = {
    "Analyse du Besoin en Fonds de Roulement (BFR)": ANALYSE_BFR,
    "Synthèse et points d'attentions": SYNTHESE
}

def generate_analysis(numero_client, pre_generated=True):
    if pre_generated and numero_client == 10:
        return PRE_GENERATED_ANALYSIS_10
    
    # if not pre_generated:
    #     generate()
    return None