# Évaluation

L'évaluation se fait avec le script PercepEval de l'INRIA https://gitlab.inria.fr/dlolive/PercepEval

## A utiliser avec PercepEval

  - completed.tpl, export.tpl, index.tpl et DV3.tpl : les fichiers template qui contrôlent le HTML
  - dv3_sysA.csv et dv3_sysB.csv : les paires de systèmes à comparer (_les données ne sont pas incluses dans ce dépôt_)
  - DV3.json : le fichier de configuration de l'évaluation DeepVoice3
  - generate-DV3.sh : le script bash pour générer la plateforme elle même
  - pm_bodies.py : le script Python qui définit le code de la plateforme, plusieurs adaptations y ont été apporté

## Script post-évaluation

Le script récupère les données obtenues pendant l'évaluation réalisée avec PercepEval. Il requiert la base de données de l'évaluation (au format CSV) et le corpus de test utilisé.

Il suffit d'utiliser la commande `python eval.py > resultat.txt`.

Il va générer :
  - resultat.txt : contient les différents résultats sous forme de tableau textuels
  - rank.png : un histogramme de la préférence par paire de système
  - length.png : un histogramme de la préférence par rapport à la longueur de l'extrait
