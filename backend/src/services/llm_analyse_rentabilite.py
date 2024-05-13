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

PRE_GENERATED_ANALYSIS_10 = {
    "Résultat d'exploitation après impôt et Rentabilité économique": "Avec un actif économique négatif de -266.70 K€, le calcul de la rentabilité économique traditionnelle n'est pas pertinent pour cette entreprise. Toutefois, le résultat d'exploitation après impôt sur le chiffre d'affaires s'élève à 2.07 %, montrant une légère baisse de 0.21 % par rapport à l'année précédente. Cela indique une capacité réduite à générer des bénéfices à partir de ses activités principales. La baisse du résultat opérationnel peut signaler des inefficacités opérationnelles ou une augmentation des coûts qui doivent être surveillées.",
    "Coût de la dette et levier financier": "Le coût des dettes est relativement bas à 1.22 %, même s'il a augmenté de 0.78 % par rapport à l'année précédente. Cela reste en dessous du seuil de 5 %, ce qui est considéré comme très acceptable. Le levier financier élevé à 36.84 %, en hausse de 4.10 %, indique que l'entreprise s'appuie de manière significative sur l'endettement pour financer ses activités. Cela peut augmenter la rentabilité des capitaux propres mais aussi introduire un risque financier accru si la rentabilité opérationnelle diminue.",
    "Rentabilité des capitaux propres": "La rentabilité des capitaux propres est de 5.76 %, avec une légère augmentation de 0.04 % par rapport à l'année précédente. Cette rentabilité, bien que modeste, est maintenue principalement par l'effet du levier financier, étant donné que la rentabilité économique n'est pas calculable directement. L'efficacité de cet effet de levier doit être évaluée en tenant compte des risques associés à une dépendance accrue à l'endettement.",
    "Risques de l'entreprise": "L'entreprise est exposée à plusieurs risques, notamment un risque financier dû à un levier élevé et un risque opérationnel reflété par la baisse de son résultat d'exploitation. L'actif économique négatif et la dépendance à l'endettement augmentent la vulnérabilité aux fluctuations économiques et aux changements des taux d'intérêt. De plus, une trésorerie élevée, bien que réduisant le risque de liquidité, peut impacter négativement la rentabilité globale si elle n'est pas gérée efficacement pour générer des rendements.",
    "Synthèse": "L'entreprise a une structure financière qui repose fortement sur l'effet de levier pour maintenir sa rentabilité des capitaux propres. Bien que le coût de la dette reste bas, la dépendance accrue à l'endettement et la diminution du résultat d'exploitation nécessitent une gestion prudente pour assurer la durabilité financière à long terme."
}

def generate_analysis(numero_client, pre_generated=True):
    if pre_generated and numero_client == 10:
        return PRE_GENERATED_ANALYSIS_10
    
    # if not pre_generated:
    #     generate()
    return None