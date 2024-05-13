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
    "Chiffre d'affaire": "L'entreprise cliente a réalisé un chiffre d'affaires de 2,656 K€, en croissance de 7,84% par rapport à l'année précédente. Cette croissance est supérieure à celle du secteur du déménagement, qui est de 6,60%. Cela indique que l'entreprise a réussi à gagner des parts de marché et à augmenter ses ventes plus rapidement que ses concurrents.",
    "Valeur ajoutée": "La valeur ajoutée de l'entreprise est de 35,13% du chiffre d'affaires, en baisse de 3,44% par rapport à l'année précédente. Cela est inférieur à la moyenne du secteur qui est de 43,1%. Cela pourrait indiquer que l'entreprise a des coûts de production plus élevés que ses concurrents ou qu'elle n'a pas réussi à augmenter ses prix autant qu'eux.",
    "Charges de Personnel": "Les charges de personnel de l'entreprise représentent 21,80% du chiffre d'affaires, en baisse de 5,64% par rapport à l'année précédente. Cela est inférieur à la moyenne du secteur qui est de 35%. Cela pourrait indiquer que l'entreprise a réussi à contrôler ses coûts de personnel plus efficacement que ses concurrents.",
    "Point mort": "Le ratio chiffre d'affaires sur point mort de l'entreprise est de 105,40%, en baisse de 0,28% par rapport à l'année précédente. Cela indique que l'entreprise est légèrement au-dessus de son point mort, ce qui signifie qu'elle couvre ses coûts et génère un petit bénéfice. Cependant, comme ce ratio est proche de 100%, l'entreprise est relativement risquée car une petite baisse de son chiffre d'affaires pourrait la faire passer en dessous de son point mort.",
    "Resultat d'exploitation": "Le résultat d'exploitation de l'entreprise est de 1,66% du chiffre d'affaires, en baisse de 7,27% par rapport à l'année précédente. Cela est inférieur à la moyenne du secteur qui est de 6,3%. Cela pourrait indiquer que l'entreprise a des coûts d'exploitation plus élevés que ses concurrents ou qu'elle n'a pas réussi à augmenter ses prix autant qu'eux.",
    "Résultat Net": "Le résultat net de l'entreprise est de 0,90% du chiffre d'affaires, en baisse de 28,21% par rapport à l'année précédente. Cela indique que l'entreprise a eu des coûts non opérationnels ou des charges fiscales plus élevées que l'année précédente.",
    "Synthèse": "En synthèse, l'entreprise a réussi à augmenter son chiffre d'affaires plus rapidement que le secteur, mais ses marges sont inférieures à celles de ses concurrents. Elle a réussi à contrôler ses coûts de personnel, mais ses coûts de production et d'exploitation sont plus élevés. Elle est légèrement au-dessus de son point mort, ce qui la rend relativement risquée. Ses résultats d'exploitation et nets sont en baisse, ce qui pourrait indiquer des problèmes de coûts non opérationnels ou de charges fiscales."
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

