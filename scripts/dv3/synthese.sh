#!/bin/bash

cd ../../deepvoice3_by_tg

# python synthesis.py <adresse du checkpoint> <adresse du fichier texte à synthétiser> <emplacement où sauvegarder les fichiers audio> --preset=<preset>
python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/average.pth tests/test_fr/learn.txt /lium/raid01_b/tgranjon/dv3/synthesis --preset=presets/deepvoice3_synpaflex.json
# Version pour un checkpoint spécifique (pas une moyenne). Il faut alors spécifier en ligne de commande le numéro du checkpoint (i.e. 000670000).
#python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/checkpoint_step$1.pth tests/test_fr/roman.txt /lium/raid01_b/tgranjon/dv3/synthesis --preset=presets/deepvoice3_synpaflex.json
# Version utilisant le vocodeur WaveNet.
# On ajoute l'emplacement du checkpoint WaveNet à utiliser en fin de ligne avec l'option --checkpoint_wavenet=.
#python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/average.pth tests/test_fr/phrase.txt /lium/raid01_b/tgranjon/dv3/synthesis --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth

cd ../scripts/dv3
