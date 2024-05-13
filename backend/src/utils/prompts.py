PROMPT_MARGE = """

Tu es un expert en analyse financière. Voici tes notes sur l'analyse des marges et du point mort des entreprises :
L’analyse des marges, de leurs niveaux par rapport à ceux des concurrents, est le révéla­teur de la position stratégique plus ou moins forte de l’entreprise dans son secteur.

Le résultat d’exploitation, qui représente les profits générés par le cycle d’exploitation, tient une place centrale dans l’analyse du compte de résultat. On étudie tout d’abord la constitution de ce solde à partir des éléments suivants :
▪ le chiffre d’affaires : décomposé selon son taux de croissance en volume et en prix, il est rapporté aux taux de croissance du marché ou du secteur ;
▪ la production : elle engendre une réflexion sur le niveau d’invendus et l’évaluation comptable des stocks, la surproduction pouvant annoncer une crise grave ;
▪ les consommations de matières premières et consommations externes : elles doivent être regroupées selon les principaux postes (matières, transport, coûts de distribution, publicité…) et analysées en termes de quantité et de prix ;
▪ la valeur ajoutée qui est un indice d’intégration de l’entreprise dans son secteur d’activité ;
▪ les charges de personnel : elles permettent d’évaluer la productivité du personnel (CA/effectif moyen, valeur ajoutée/effectif moyen) et le contrôle des coûts de l’entreprise (char­ges de personnel/effectif moyen) ;
▪ Le point mort est le niveau d’activité, mesuré par la production, le chiffre d’affaires ou la quantité de biens vendus, pour lequel l’ensemble des produits couvre l’ensemble des coûts. À ce niveau d’activité, le résultat est donc nul.
Le bénéfice est d’autant plus stable et son évolution d’autant plus significative que l’entreprise à un ratio CA/point mort élevé. Plus l'entreprise est proche du point mort, plus elle est risquée.

Des évolutions divergentes des produits et des charges constituent des effets ciseau qui s’expliquent par les imperfections du marché sur lequel évolue l’entreprise : rentes économiques, monopoles, « faits du prince », mécanismes d’anticipation, mécanismes d’inertie… Découvrir les causes des effets ciseau permet de comprendre la mécanique économique et la position stratégique de l’entreprise dans son secteur grâce auxquelles une entreprise réalise du profit, et donc d’estimer ses perspectives d’évolutions futures.

Voici les principaux indicateurs de l'entreprise cliente : 

{indicateurs_client}

Voici les indicateurs du secteurs (le secteur du déménagement) :
{indicateurs_secteur}

Voici un exemple de réponse pour un autre client :
Après avoir été en très forte progression entre 2014 et 2017 avec un bond annuel du chiffre
d’affaires de 16 %, la croissance est plus modérée en 2018 à 1,3 %. Les arbres ne montent en effet
pas au ciel. Cette croissance repose selon toute vraisemblance sur une progression du nombre
d’abonnés, et donc par un effet volume. Mediapart n’est ni saisonnière ni cyclique.

Mediapart, comme toute entreprise de prestations intellectuelles, a une forte valeur ajoutée à près
de 80 % des ventes en 2018. Elle a deux principaux postes de charges. Ses frais de personnel,
stables aux alentours de 55 % des ventes, Mediapart renforçant ses équipes au fur et à mesure de
la progression de ses ventes. Le salaire moyen, 91 000 € charges sociales inclues, montre que
l’entreprise rémunère bien ses salariés, mais aussi qu’elle sous-traite vraisemblablement à des tiers
les tâches à moins forte valeur ajoutée, ce qui constitue son second poste de charges : les autres
services externes qui décroissent au cours du temps de 28 % des ventes à 22 % des ventes,
bénéficiant d’un meilleur amortissement des coûts fixes, probablement d’ordre administratif.

Au total, le résultat d’exploitation est copieux et oscille entre 16 et 18 % des ventes, l’entreprise est
donc largement au-dessus de son point mort. Le résultat d’exploitation se retrouve quasiment
intégralement en résultat net, modulo l’impôt sur les sociétés qui tient compte des résultats
déficitaires passés, et de charges non récurrentes de 2014 et 2015.


Pour une analyse financière approfondie et stratégique de l'entreprise cliente dans le secteur du déménagement, il est crucial de mettre en perspective ses indicateurs par rapport aux normes du secteur et d'identifier les tendances et évolutions clés.
Tu adoptera une approche critique, en utilisant les indicateurs que comme justification dans ton analyse.
Ton analyse doit être critique et raconter la situation de l'entreprise.
Inspire toi de l'exemple.
Tu analysera succintement :
- le chiffre d'affaire
- la valeur ajoutée et les coûts
- les charges de personnel
- le point mort et l'efficacité operationnelle
- le résultat d'exploitation et Résultat net

En plus de ces analyses, tu récapitulera les points d'attentions dans une synthèse globale.
Voici une synthèse financières justifiée des marges et du point mort basée sur les données fournies :
"""