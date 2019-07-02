#!/bin/bash

# Effectue le prétraitement.

cd ../../../deepvoice3_world/

# python preprocess.py <nom du corpus> <emplacement du fichier CSV qui contient les données> <emplacement où sauvegarder les données pré-traitées> --preset=<preset>

python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/dv3/world/data --preset=../../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json

cd ../scripts/dv3/world
