
SUBJECT = "Objet : Demande de documents nécessaires pour votre dossier"

BODY = """
Cher Mr. Dupont,

En préparation de notre prochaine rencontre, je suis en train de rassembler tous les documents nécessaires pour compléter votre dossier et pour mieux évaluer les besoins spécifiques de votre entreprise.

Pour avancer dans cette démarche, il me manque actuellement deux documents importants : un extrait K-bis de moins de trois mois et une copie de votre passeport. Pourriez-vous s'il vous plaît me faire parvenir ces documents dès que possible ? Leur réception en temps utile permettra d'assurer que notre entretien soit le plus complet et efficace possible.

Je vous remercie par avance de votre coopération et reste à votre disposition pour toute question ou assistance supplémentaire.

Cordialement,
"""

def generate_mail(numero_client, pre_generated=True):
    if pre_generated and numero_client == 10:
        return {"Subject": SUBJECT, "Body": BODY}

    # if not pre_generated:
    #     generate()
    return None