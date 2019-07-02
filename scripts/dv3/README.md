# Scripts de Deep Voice 3

Les scripts du répertoire actuel contrôle Deep Voice 3 avec Griffin-Lim ou avec WaveNet. Les commandes pour la version WORLD sont le répertoire spécifique mais elle ne diffèrent presque pas de celles du programme principal.

Tous ces scripts ont une ligne d'instructions à l'intérieur.

Par ordre d'utilisation, les scripts sont :
  - preprocess.sh : Lance le pré-traitement.
  - train.sh : Lance l'apprentissage.
  - checkpoint.sh : Lance l'apprentissage à partir d'un checkpoint spécifique.
  - average.py : Crée un checkpoint moyen à partir de tous les checkpoints générés.
  - synthese.sh : Lance la synthèse.
  - synthese_all.sh : Lance la synthèse de tous les modèles utilisés pour l'évaluation.
  - epoques.sh : Lance une synthèse sur tous les checkpoints d'un modèle (pour observer l'évolution du modèle).
