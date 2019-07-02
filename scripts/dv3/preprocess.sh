#!/bin/bash

# Effectue le prétraitement.

cd ../../deepvoice3_by_tg/

# python preprocess.py <nom du corpus> <emplacement du fichier CSV qui contient les données> <emplacement où sauvegarder les données pré-traitées> <preset>
python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/dv3/data --preset=presets/deepvoice3_synpaflex.json

cd ../scripts/dv3/
