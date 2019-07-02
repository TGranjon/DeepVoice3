#!/bin/bash

# Effectue une synthèse sur toutes les époques.
# Il est recommandé de choisir un fichier test d'une seule phrase.

cd ../../deepvoice3_by_tg

# Il faut changer l'adresse des checkpoints.
for file in /lium/raid01_b/tgranjon/test/checkpoints/*.pth
do
	echo $file
	# python synthesis.py "$file" <fichier test à synthétiser> <emplacement où sauvegarder les fichiers audio> <preset>
	python synthesis.py "$file" tests/test_fr/learn.txt /lium/raid01_b/tgranjon/test/synthesis --preset=presets/deepvoice3_synpaflex.json
	# Il est possible de sauvegarder le spectrogramme générer avec cette commande.
	#python synthesis_cop.py "$file" tests/test_fr/learn.txt /lium/raid01_b/tgranjon/test/synthesis --preset=presets/deepvoice3_synpaflex.json

done
cd ../scripts/dv3
