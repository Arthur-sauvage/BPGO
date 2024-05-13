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
    "Analyse des flux de trésorerie et du désendettement net": """L'entreprise a un flux de trésorerie d'exploitation de 12.88 K€, indiquant que les opérations génèrent un flux modeste de liquidités. Cela pourrait être perçu comme un point positif, mais il faut le contextualiser par rapport à la taille et aux besoins de l'entreprise. Le désendettement net de -10.12 K€ révèle une réduction nette de la trésorerie, ce qui soulève des préoccupations sur la gestion efficace des flux financiers. Cette situation pourrait indiquer que les liquidités générées par l'exploitation ne sont pas suffisantes pour couvrir pleinement les sorties de fonds, y compris les remboursements de dette, ce qui peut entraîner un risque accru à moyen terme si cette tendance se poursuit.""",
    "Structure du Financement": """Le ratio dette/EBE de 2.56 est inférieur à la valeur critique de 3, ce qui est rassurant quant à la capacité de l'entreprise à gérer son endettement à moyen terme. De plus, le ratio résultat d'exploitation/frais financiers est de 14.15, bien au-dessus de la valeur critique de 3, signalant une très bonne capacité de l'entreprise à couvrir ses frais financiers grâce à ses résultats opérationnels. Ces indicateurs suggèrent que, bien que l'entreprise ait des défis à relever, elle maintient une structure de financement saine.""",
    "Analyse de l'actif économique et des disponibilités": """L'actif économique négatif de -266.70 K€ et un BFR également négatif de -419.00 K€ indiquent que l'entreprise n'a pas besoin de financements significatifs pour couvrir ses opérations courantes, ce qui est généralement un signe positif. Cela suggère que l'entreprise est capable de libérer des fonds de ses activités opérationnelles, ce qui est crucial pour une entreprise qui subit des fluctuations saisonnières ou cycliques typiques du secteur du déménagement. Les disponibilités de 1,029.62 K€ malgré une baisse de 26.56 K€ par rapport à l'année précédente, restent robustes, offrant une marge de sécurité contre des chocs imprévus.""",
    "Synthèse": "L'entreprise dispose de plusieurs points forts, notamment une structure de financement saine et des disponibilités conséquentes. Cependant, le flux de trésorerie d'exploitation modeste et la baisse des disponibilités nécessitent une vigilance. Il est crucial de surveiller les flux de trésorerie futurs et d'optimiser les coûts et les marges pour améliorer la génération de flux de trésorerie.",
}

# model = AzureChatOpenAI(
#                 openai_api_version=os.getenv("OPENAI_API_VERSION"),
#                 azure_deployment=os.getenv("DEPLOIMENT_NAME"),
#                 temperature=0,
#             )

# def generate(prompt):
#     prompt = ChatPromptTemplate.from_template(prompt)

#     analyse_chain = LLMChain(llm=model, prompt=prompt)

#     chain = SequentialChain(
#             chains=[analyse_chain],
#             input_variables=[],
#             verbose=False,
#         )

#     with get_openai_callback() as cb:
#         start_time = time.perf_counter()
#         try:
#             resp = chain.run({})
#             elapsed_time = time.perf_counter() - start_time
#             cost = cb.total_cost
#             logging.info(f"finished | {elapsed_time:.2f} seconds | {cost} $")
#             return resp
#         except Exception as e:
#             logging.error(f"Error during model invocation: {e}", exc_info=True)
#             raise e


def generate_analysis(numero_client, pre_generated=True):
    if pre_generated and numero_client == 10:
        return PRE_GENERATED_ANALYSIS_10

    # if not pre_generated:
    #     generate()
    return None
