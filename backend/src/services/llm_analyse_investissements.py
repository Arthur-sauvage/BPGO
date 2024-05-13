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

ANALYSE_INVESTISSEMENTS = """
L'entreprise présente un degré d'usure de l'outil industriel de 77.28%, ce qui est assez élevé. Cela signifie que l'entreprise a déjà amorti une grande partie de ses immobilisations et qu'elle pourrait avoir besoin de renouveler son outil de production. Cependant, les investissements de l'entreprise sont inférieurs aux dotations aux amortissements, ce qui indique une politique d'investissement plutôt de retrait. 
"""

SYNTHESE = """
En ce qui concerne la politique d'investissement, l'entreprise semble être en retrait avec des investissements inférieurs aux dotations aux amortissements et un degré d'usure élevé de l'outil industriel. Il serait donc pertinent pour l'entreprise de réfléchir à une politique d'investissement plus dynamique pour renouveler son outil de production et maintenir sa compétitivité.
"""

PRE_GENERATED_ANALYSIS_10 = {
    "Analyse de la politique d'investissements": ANALYSE_INVESTISSEMENTS,
    "Synthèse et points d'attentions": SYNTHESE
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

